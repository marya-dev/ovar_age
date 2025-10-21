import json
import time
from typing import Any, Dict, List, Optional

import pandas as pd
from tqdm import tqdm

from config import CLAUDE_API_KEY, EMAIL

# Biopython imports for PubMed
from Bio import Entrez, Medline

# Anthropic (Claude) SDK
import anthropic


def search_pubmed(term: str, start_year: int, end_year: int, retmax: int = 20) -> List[str]:
    """Search PubMed and return a list of PMIDs as strings."""
    Entrez.email = EMAIL
    # Optional: obey NCBI usage policy by sleeping between requests if needed
    handle = Entrez.esearch(
        db="pubmed",
        term=term,
        mindate=str(start_year),
        maxdate=str(end_year),
        datetype="pdat",
        retmax=retmax,
        sort="relevance",
    )
    results = Entrez.read(handle)
    handle.close()
    id_list = results.get("IdList", [])
    return id_list


def fetch_pubmed_records(pmids: List[str]) -> List[Dict[str, Any]]:
    """Fetch PubMed records in MEDLINE format and extract key fields."""
    if not pmids:
        return []
    # Fetch all in one call for efficiency
    handle = Entrez.efetch(db="pubmed", id=",".join(pmids), rettype="medline", retmode="text")
    records = list(Medline.parse(handle))
    handle.close()

    extracted: List[Dict[str, Any]] = []
    for rec in records:
        pmid = rec.get("PMID")
        title = rec.get("TI")
        abstract = rec.get("AB")
        journal = rec.get("JT") or rec.get("TA")
        # Year may be in DP (Date of Publication) like "2019 Jan" or in "PHST"; prefer "DP"
        year: Optional[int] = None
        dp = rec.get("DP")
        if isinstance(dp, str) and len(dp) >= 4 and dp[:4].isdigit():
            year = int(dp[:4])
        elif rec.get("EDAT"):
            # EDAT example: '2019/01/15 06:00'
            edat = rec.get("EDAT")
            if isinstance(edat, list) and edat:
                edat = edat[0]
            if isinstance(edat, str) and len(edat) >= 4 and edat[:4].isdigit():
                year = int(edat[:4])

        extracted.append(
            {
                "pmid": pmid,
                "title": title,
                "abstract": abstract,
                "journal": journal,
                "year": year,
            }
        )
    return extracted


def build_claude_prompt(abstract: str) -> str:
    """Create an instruction for Claude to extract structured values as JSON."""
    return (
        "You are a biomedical information extraction assistant. "
        "From the study abstract below, extract the following fields if present. "
        "If a field is not clearly present, set it to null (or empty list for confounders).\n\n"
        "Required JSON schema: {\n"
        "  health_outcome: string,\n"
        "  menopause_timing: string,\n"
        "  metric_type: string,  // one of OR, HR, RR\n"
        "  metric_value: number,\n"
        "  ci_lower: number,\n"
        "  ci_upper: number,\n"
        "  sample_size: integer,\n"
        "  study_design: string,\n"
        "  confounders: string[]\n"
        "}\n\n"
        "Abstract:\n" + abstract
    )


def extract_with_claude(client: anthropic.Anthropic, abstract: Optional[str]) -> Dict[str, Any]:
    """Call Claude to extract fields from the abstract. Returns a dict following the schema."""
    empty_result: Dict[str, Any] = {
        "health_outcome": None,
        "menopause_timing": None,
        "metric_type": None,
        "metric_value": None,
        "ci_lower": None,
        "ci_upper": None,
        "sample_size": None,
        "study_design": None,
        "confounders": [],
    }

    if not abstract or not abstract.strip():
        return empty_result

    try:
        prompt = build_claude_prompt(abstract)
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=800,
            temperature=0,
            system=(
                "Extract biomedical study metadata as strict JSON only. "
                "Respond with a single JSON object matching the schema."
            ),
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
        )

        text = ""
        if hasattr(response, "content") and response.content:
            # Anthropic SDK returns a list of content blocks
            # Extract the first text block
            for block in response.content:
                if getattr(block, "type", None) == "text":
                    text = block.text
                    break
        # Fallback if structure differs
        if not text and hasattr(response, "text"):
            text = getattr(response, "text")

        data = json.loads(text)

        # Normalize and coerce types safely
        def to_float(x: Any) -> Optional[float]:
            try:
                return float(x) if x is not None else None
            except Exception:
                return None

        def to_int(x: Any) -> Optional[int]:
            try:
                # Some papers report large Ns; ensure we handle numeric-like strings
                return int(float(x)) if x is not None else None
            except Exception:
                return None

        result: Dict[str, Any] = {
            "health_outcome": data.get("health_outcome"),
            "menopause_timing": data.get("menopause_timing"),
            "metric_type": data.get("metric_type"),
            "metric_value": to_float(data.get("metric_value")),
            "ci_lower": to_float(data.get("ci_lower")),
            "ci_upper": to_float(data.get("ci_upper")),
            "sample_size": to_int(data.get("sample_size")),
            "study_design": data.get("study_design"),
            "confounders": data.get("confounders") or [],
        }
        # Ensure confounders is a list of strings
        if not isinstance(result["confounders"], list):
            result["confounders"] = []
        else:
            result["confounders"] = [str(c) for c in result["confounders"] if c is not None]

        return result
    except Exception:
        # On any error (API, parsing), return empty schema
        return empty_result


def run_pipeline() -> None:
    """End-to-end pipeline: search PubMed, extract fields with Claude, export to Excel."""
    # 1) Build PubMed query for menopause timing and health outcomes (2015-2025)
    query_terms = [
        "menopause timing",
        "age at menopause",
        "early menopause",
        "premature menopause",
        "late menopause",
        "cardiovascular disease",
        "osteoporosis",
        "dementia",
        "breast cancer",
        "health outcome",
    ]
    # Combine with AND/OR logic; bias towards menopause timing + any of the outcomes
    pubmed_query = (
        "(early menopause OR premature menopause) "
    "AND (cardiovascular OR stroke OR myocardial infarction OR osteoporosis OR fracture OR dementia) "
    "AND (odds ratio OR hazard ratio OR relative risk OR OR OR HR OR RR) "
    "AND (cohort[Title/Abstract] OR case-control[Title/Abstract])"
    )

    # 2) Search and fetch records
    pmids = search_pubmed(term=pubmed_query, start_year=2015, end_year=2025, retmax=20)
    # Respect NCBI rate limits
    time.sleep(0.34)
    records = fetch_pubmed_records(pmids)

    # 3) Initialize Anthropic client
    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

    # 4) For each record, call Claude to extract structured data
    rows: List[Dict[str, Any]] = []
    for rec in tqdm(records, desc="Processing abstracts with Claude", unit="paper"):
        extracted = extract_with_claude(client, rec.get("abstract"))
        row = {
            "pmid": rec.get("pmid"),
            "title": rec.get("title"),
            "abstract": rec.get("abstract"),
            "journal": rec.get("journal"),
            "year": rec.get("year"),
            **extracted,
        }
        rows.append(row)
        # Gentle pacing for API stability
        time.sleep(0.2)

    # 5) Save to Excel
    df = pd.DataFrame(rows, columns=[
        "pmid",
        "title",
        "abstract",
        "journal",
        "year",
        "health_outcome",
        "menopause_timing",
        "metric_type",
        "metric_value",
        "ci_lower",
        "ci_upper",
        "sample_size",
        "study_design",
        "confounders",
    ])
    output_path = "menopause_data.xlsx"
    try:
        df.to_excel(output_path, index=False)
        print(f"Saved {len(df)} records to {output_path}")
    except Exception as exc:
        # Fall back to CSV if Excel writer not available
        fallback_path = "menopause_data.csv"
        print(f"Failed to save Excel ({exc}). Saving CSV to {fallback_path} instead.")
        df.to_csv(fallback_path, index=False)


if __name__ == "__main__":
    run_pipeline()


