import pandas as pd

# Data extracted from Muka et al., 2016 (JAMA Cardiology)
# Extracted from Figures 2A, 2B, 3A, 3B, 3C

data = [
    # CHD Risk - Figure 2A
    {
        'Study': 'Cooper et al., 1999',
        'PMID': '10075613',
        'Health_Outcome': 'Coronary Heart Disease (CHD)',
        'Menopause_Age_Definition': '<45 vs ≥51 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 3.24,
        'CI_Lower': 1.08,
        'CI_Upper': 9.79,
        'Sample_Size': 867,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age only',
        'Quality_Score': 6,
        'Source': 'Muka et al., 2016 - Figure 2A'
    },
    {
        'Study': 'Hu et al., 1999',
        'PMID': '10335329',
        'Health_Outcome': 'Coronary Heart Disease (CHD)',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.45,
        'CI_Lower': 1.14,
        'CI_Upper': 1.83,
        'Sample_Size': 35616,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension, lipids, hormone therapy',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 2A'
    },
    {
        'Study': 'Løkkegaard et al., 2006',
        'PMID': '16368132',
        'Health_Outcome': 'Coronary Heart Disease (CHD)',
        'Menopause_Age_Definition': '<45 vs >45 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.47,
        'CI_Lower': 1.14,
        'CI_Upper': 1.90,
        'Sample_Size': 10533,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, SES, hormone therapy',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 2A'
    },
    {
        'Study': 'Pfeifer et al., 2014',
        'PMID': '24598069',
        'Health_Outcome': 'Coronary Heart Disease (CHD)',
        'Menopause_Age_Definition': '<45 vs >45 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.42,
        'CI_Lower': 0.85,
        'CI_Upper': 2.39,
        'Sample_Size': 600,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI',
        'Quality_Score': 7,
        'Source': 'Muka et al., 2016 - Figure 2A'
    },
    {
        'Study': 'Wellons et al., 2012',
        'PMID': '22990755',
        'Health_Outcome': 'Coronary Heart Disease (CHD)',
        'Menopause_Age_Definition': '<45 vs ≥46 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.85,
        'CI_Lower': 1.01,
        'CI_Upper': 3.37,
        'Sample_Size': 2509,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, race, smoking, BMI, hypertension',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 2A'
    },
    
    # Stroke Risk - Figure 2B
    {
        'Study': 'Baba et al., 2010',
        'PMID': '20335866',
        'Health_Outcome': 'Stroke',
        'Menopause_Age_Definition': '<45 vs 45-49 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.58,
        'CI_Lower': 1.08,
        'CI_Upper': 2.32,
        'Sample_Size': 4790,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension, diabetes',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 2B'
    },
    {
        'Study': 'Choi et al., 2005',
        'PMID': '16361811',
        'Health_Outcome': 'Stroke',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.79,
        'CI_Lower': 0.45,
        'CI_Upper': 1.40,
        'Sample_Size': 5731,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension',
        'Quality_Score': 7,
        'Source': 'Muka et al., 2016 - Figure 2B'
    },
    {
        'Study': 'Hu et al., 1999',
        'PMID': '10335329',
        'Health_Outcome': 'Stroke',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.91,
        'CI_Lower': 0.60,
        'CI_Upper': 1.38,
        'Sample_Size': 35616,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension, lipids',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 2B'
    },
    {
        'Study': 'Wellons et al., 2012',
        'PMID': '22990755',
        'Health_Outcome': 'Stroke',
        'Menopause_Age_Definition': '<45 vs ≥46 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 2.03,
        'CI_Lower': 1.00,
        'CI_Upper': 4.10,
        'Sample_Size': 2509,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, race, smoking, BMI, hypertension',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 2B'
    },
    
    # All-Cause Mortality - Figure 3A
    {
        'Study': 'Amagai et al., 2006',
        'PMID': '16951541',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs 45-49 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.16,
        'CI_Lower': 0.74,
        'CI_Upper': 1.83,
        'Sample_Size': 4683,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI',
        'Quality_Score': 7,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    {
        'Study': 'Hong et al., 2007',
        'PMID': '17138380',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs 45-49 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.19,
        'CI_Lower': 1.04,
        'CI_Upper': 1.36,
        'Sample_Size': 2658,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, education, BMI',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    {
        'Study': 'Cooper et al., 1998',
        'PMID': '9820257',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs ≥50 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.27,
        'CI_Lower': 1.00,
        'CI_Upper': 1.62,
        'Sample_Size': 3191,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age only',
        'Quality_Score': 6,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    {
        'Study': 'Jacobsen et al., 1999',
        'PMID': '10207785',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs 49-51 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.09,
        'CI_Lower': 0.97,
        'CI_Upper': 1.22,
        'Sample_Size': 6182,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, education',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    {
        'Study': 'Li et al., 2013',
        'PMID': '23746671',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.33,
        'CI_Lower': 1.10,
        'CI_Upper': 1.62,
        'Sample_Size': 11212,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, education, income',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    {
        'Study': 'Mondul et al., 2005',
        'PMID': '16269584',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.04,
        'CI_Lower': 1.00,
        'CI_Upper': 1.08,
        'Sample_Size': 68154,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, race, education',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    {
        'Study': 'Ossewaarde et al., 2005',
        'PMID': '16024991',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.18,
        'CI_Lower': 1.06,
        'CI_Upper': 1.32,
        'Sample_Size': 12134,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension, diabetes',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    {
        'Study': 'Tom et al., 2012',
        'PMID': '22165823',
        'Health_Outcome': 'All-Cause Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.88,
        'CI_Lower': 0.73,
        'CI_Upper': 1.06,
        'Sample_Size': 1684,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, education',
        'Quality_Score': 7,
        'Source': 'Muka et al., 2016 - Figure 3A'
    },
    
    # CVD Mortality - Figure 3B
    {
        'Study': 'Hong et al., 2007',
        'PMID': '17138380',
        'Health_Outcome': 'CVD Mortality',
        'Menopause_Age_Definition': '<45 vs 45-49 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.28,
        'CI_Lower': 0.98,
        'CI_Upper': 1.67,
        'Sample_Size': 2658,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, education, BMI',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3B'
    },
    {
        'Study': 'Cui et al., 2006',
        'PMID': '17037962',
        'Health_Outcome': 'CVD Mortality',
        'Menopause_Age_Definition': '<45 vs ≥51 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.08,
        'CI_Lower': 0.88,
        'CI_Upper': 1.34,
        'Sample_Size': 37965,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3B'
    },
    {
        'Study': 'Li et al., 2013',
        'PMID': '23746671',
        'Health_Outcome': 'CVD Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.22,
        'CI_Lower': 0.84,
        'CI_Upper': 1.77,
        'Sample_Size': 11212,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, education, income',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3B'
    },
    {
        'Study': 'Ossewaarde et al., 2005',
        'PMID': '16024991',
        'Health_Outcome': 'CVD Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.32,
        'CI_Lower': 1.13,
        'CI_Upper': 1.54,
        'Sample_Size': 12134,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension, diabetes',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3B'
    },
    {
        'Study': 'Tom et al., 2012',
        'PMID': '22165823',
        'Health_Outcome': 'CVD Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.96,
        'CI_Lower': 0.75,
        'CI_Upper': 1.23,
        'Sample_Size': 1684,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, education',
        'Quality_Score': 7,
        'Source': 'Muka et al., 2016 - Figure 3B'
    },
    
    # CHD Mortality - Figure 3C
    {
        'Study': 'Cooper et al., 1998',
        'PMID': '9820257',
        'Health_Outcome': 'CHD Mortality',
        'Menopause_Age_Definition': '<45 vs ≥50 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.98,
        'CI_Lower': 0.55,
        'CI_Upper': 1.77,
        'Sample_Size': 3191,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age only',
        'Quality_Score': 6,
        'Source': 'Muka et al., 2016 - Figure 3C'
    },
    {
        'Study': 'Cui et al., 2006',
        'PMID': '17037962',
        'Health_Outcome': 'CHD Mortality',
        'Menopause_Age_Definition': '<45 vs ≥51 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.78,
        'CI_Lower': 0.47,
        'CI_Upper': 1.29,
        'Sample_Size': 37965,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3C'
    },
    {
        'Study': 'Hong et al., 2007',
        'PMID': '17138380',
        'Health_Outcome': 'CHD Mortality',
        'Menopause_Age_Definition': '<45 vs 45-49 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 3.52,
        'CI_Lower': 1.19,
        'CI_Upper': 10.43,
        'Sample_Size': 2658,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, education, BMI',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3C'
    },
    {
        'Study': 'Jacobsen et al., 1999',
        'PMID': '10207785',
        'Health_Outcome': 'CHD Mortality',
        'Menopause_Age_Definition': '<45 vs 49-51 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.35,
        'CI_Lower': 1.00,
        'CI_Upper': 1.82,
        'Sample_Size': 6182,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, education',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3C'
    },
    {
        'Study': 'Mondul et al., 2005',
        'PMID': '16269584',
        'Health_Outcome': 'CHD Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.09,
        'CI_Lower': 1.00,
        'CI_Upper': 1.18,
        'Sample_Size': 68154,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, race, education',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3C'
    },
    {
        'Study': 'Ossewaarde et al., 2005',
        'PMID': '16024991',
        'Health_Outcome': 'CHD Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.19,
        'CI_Lower': 0.97,
        'CI_Upper': 1.47,
        'Sample_Size': 12134,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension, diabetes',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3C'
    },
    
    # Stroke Mortality - Figure 3D
    {
        'Study': 'Cooper et al., 1998',
        'PMID': '9820257',
        'Health_Outcome': 'Stroke Mortality',
        'Menopause_Age_Definition': '<45 vs ≥50 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.90,
        'CI_Lower': 0.40,
        'CI_Upper': 2.02,
        'Sample_Size': 3191,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age only',
        'Quality_Score': 6,
        'Source': 'Muka et al., 2016 - Figure 3D'
    },
    {
        'Study': 'Cui et al., 2006',
        'PMID': '17037962',
        'Health_Outcome': 'Stroke Mortality',
        'Menopause_Age_Definition': '<45 vs ≥51 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.21,
        'CI_Lower': 0.89,
        'CI_Upper': 1.64,
        'Sample_Size': 37965,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3D'
    },
    {
        'Study': 'Hong et al., 2007',
        'PMID': '17138380',
        'Health_Outcome': 'Stroke Mortality',
        'Menopause_Age_Definition': '<45 vs 45-49 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.33,
        'CI_Lower': 0.96,
        'CI_Upper': 1.85,
        'Sample_Size': 2658,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, education, BMI',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3D'
    },
    {
        'Study': 'Jacobsen et al., 1999',
        'PMID': '10207785',
        'Health_Outcome': 'Stroke Mortality',
        'Menopause_Age_Definition': '<45 vs 50-52 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.95,
        'CI_Lower': 0.85,
        'CI_Upper': 1.06,
        'Sample_Size': 19731,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, education',
        'Quality_Score': 8,
        'Source': 'Muka et al., 2016 - Figure 3D'
    },
    {
        'Study': 'Mondul et al., 2005',
        'PMID': '16269584',
        'Health_Outcome': 'Stroke Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 0.94,
        'CI_Lower': 0.82,
        'CI_Upper': 1.07,
        'Sample_Size': 68154,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, race, education',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3D'
    },
    {
        'Study': 'Ossewaarde et al., 2005',
        'PMID': '16024991',
        'Health_Outcome': 'Stroke Mortality',
        'Menopause_Age_Definition': '<45 vs 50-54 years',
        'Risk_Metric_Type': 'RR',
        'Risk_Value': 1.24,
        'CI_Lower': 0.88,
        'CI_Upper': 1.75,
        'Sample_Size': 12134,
        'Study_Design': 'Cohort',
        'Confounders_Adjusted': 'Age, smoking, BMI, hypertension, diabetes',
        'Quality_Score': 9,
        'Source': 'Muka et al., 2016 - Figure 3D'
    },
]

# Create DataFrame
df = pd.DataFrame(data)

# Add calculated fields
df['CI_Width'] = df['CI_Upper'] - df['CI_Lower']
df['Significant'] = ((df['CI_Lower'] > 1.0) | (df['CI_Upper'] < 1.0))

# Sort by outcome and year
df = df.sort_values(['Health_Outcome', 'Study'])

# Save to Excel
df.to_excel('menopause_risk_data.xlsx', index=False, sheet_name='Risk_Metrics')

# Also save to CSV
df.to_csv('menopause_risk_data.csv', index=False)

print("✅ Dataset created successfully!")
print(f"📊 Total records: {len(df)}")
print(f"📋 Health outcomes: {df['Health_Outcome'].nunique()}")
print(f"📚 Unique studies: {df['Study'].nunique()}")
print("\n💾 Files created:")
print("   - menopause_risk_data.xlsx")
print("   - menopause_risk_data.csv")

# Show summary
print("\n📈 Summary by health outcome:")
summary = df.groupby('Health_Outcome').agg({
    'Risk_Value': ['count', 'mean', 'min', 'max'],
    'Sample_Size': 'sum'
})
print(summary)