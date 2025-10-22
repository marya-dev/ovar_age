**Quantifying the Value of Delayed Ovarian Aging**
**Team**: OAV  
**Participant**: Maria Fomina  
**Prize Track**: Female Longevity - LifeAhead

**Executive Summary**
Delaying menopause by 5 years could prevent **4,340 cases of serious disease per million women** and generate **$609 million in economic value** over 6 years.

Top impact areas:
- Osteoporotic fractures (30.7%)
- Coronary heart disease (26.5%) 
- Stroke (23.2%)

**Project Structure**

**Multi-Agent System:**
1. `agent.py` - PubMed search agent
2. `create_dataset.py` - Data extraction agent
3. `create_osteoporosis_data.py` - Osteoporosis data agent
4. `data-collector.md` - Incidence & costs search
5. `calculator.py` - Economic calculation agent

**Datasets:**
- `combined_menopause_data.xls` - Filtered high-quality studies (Quality Score ≥8)
- `baseline_incidence_rates.xls` - Disease rates for age 50-54
- `disease_treatment_costs.xls` - Healthcare costs per disease

**Key Findings**
Women with early menopause (<45 years) face:
- 1.58× higher stroke risk
- 1.45× higher heart disease risk
- Significantly elevated osteoporosis risk

**Data Sources**
- CDC/ARIC Study (baseline incidence)
- HCUP Database (treatment costs)
- Published meta-analyses (risk ratios)

License: MIT

**FINAL REPORT.pdf** https://github.com/marya-dev/ovar_age/blob/main/FINAL%20REPORT.pdf 
