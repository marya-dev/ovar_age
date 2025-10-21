import pandas as pd

# Data extracted from Long et al., 2023 - Table 2
# Meta-analysis of osteoporotic fracture predictors in postmenopausal women

data = [
    # Age at menopause < 40
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': '<40 years vs normal',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 1.23,
        'CI_Lower': 1.19,
        'CI_Upper': 1.28,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, education, parity, hypertension, diabetes, alcohol, smoking',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.17,
        'Specificity': 0.86
    },
    
    # Age at menopause > 50 (protective)
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': '>50 years vs normal',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 0.96,
        'CI_Lower': 0.95,
        'CI_Upper': 0.97,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, education, parity, hypertension, diabetes, alcohol, smoking',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.33,
        'Specificity': 0.65
    },
    
    # Age at menarche ≥ 15
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'Menarche ≥15 years vs <15',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 1.34,
        'CI_Lower': 1.03,
        'CI_Upper': 1.73,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, education, parity, hypertension, diabetes',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.24,
        'Specificity': 0.83
    },
    
    # Parity ≥ 3 (protective)
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'Parity ≥3 vs <3',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 0.74,
        'CI_Lower': 0.58,
        'CI_Upper': 0.94,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, education, menopause age',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': None,
        'Specificity': None
    },
    
    # Estrogen use (protective)
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'Estrogen use vs no use',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 0.53,
        'CI_Lower': 0.28,
        'CI_Upper': 0.87,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, menopause age, smoking, alcohol',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.18,
        'Specificity': 0.71
    },
    
    # Vitamin D supplements
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'Vitamin D use vs no use',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 1.75,
        'CI_Lower': 1.35,
        'CI_Upper': 2.28,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, menopause age, calcium intake',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.25,
        'Specificity': 0.81
    },
    
    # History of hypertension
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'Hypertension vs no hypertension',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 1.20,
        'CI_Lower': 1.19,
        'CI_Upper': 1.22,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, diabetes, smoking, alcohol',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.38,
        'Specificity': 0.69
    },
    
    # History of diabetes mellitus
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'Diabetes vs no diabetes',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 1.19,
        'CI_Lower': 1.17,
        'CI_Upper': 1.20,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, hypertension, smoking, alcohol',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.07,
        'Specificity': 0.93
    },
    
    # History of alcohol intake (protective)
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'Alcohol use vs no alcohol',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 0.89,
        'CI_Lower': 0.88,
        'CI_Upper': 0.90,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, smoking, education',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.27,
        'Specificity': 0.78
    },
    
    # BMI (continuous variable - lower BMI = higher risk)
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'BMI (per unit decrease)',
        'Risk_Metric_Type': 'MD',
        'Risk_Value': -0.69,
        'CI_Lower': -1.31,
        'CI_Upper': -0.07,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, menopause age, smoking, alcohol',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.43,
        'Specificity': 0.59
    },
    
    # Senior high school and above (protective)
    {
        'Study': 'Long et al., 2023 (Meta-analysis)',
        'PMID': '37596654',
        'Health_Outcome': 'Osteoporotic Fracture',
        'Menopause_Age_Definition': 'High school+ vs lower education',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 1.76,
        'CI_Lower': 1.34,
        'CI_Upper': 2.32,
        'Sample_Size': 1287021,
        'Study_Design': 'Meta-analysis (10 studies)',
        'Confounders_Adjusted': 'Age, BMI, menopause age, lifestyle factors',
        'Quality_Score': 10,
        'Source': 'Long et al., 2023 - Table 2',
        'Sensitivity': 0.44,
        'Specificity': 0.70
    },
    
    # Smoking (hip fractures subgroup)
    {
        'Study': 'Long et al., 2023 (Meta-analysis - hip fractures)',
        'PMID': '37596654',
        'Health_Outcome': 'Hip Fracture',
        'Menopause_Age_Definition': 'Smoking vs non-smoking',
        'Risk_Metric_Type': 'OR',
        'Risk_Value': 1.76,
        'CI_Lower': 1.20,
        'CI_Upper': 2.58,
        'Sample_Size': None,
        'Study_Design': 'Meta-analysis (subgroup)',
        'Confounders_Adjusted': 'Age, BMI, alcohol, education',
        'Quality_Score': 9,
        'Source': 'Long et al., 2023 - Table 2 (subgroup)',
        'Sensitivity': None,
        'Specificity': None
    },
]

# Create DataFrame
df = pd.DataFrame(data)

# Add calculated fields
df['CI_Width'] = df['CI_Upper'] - df['CI_Lower']
df['Significant'] = ((df['CI_Lower'] > 1.0) | (df['CI_Upper'] < 1.0))

# Sort by risk value
df = df.sort_values('Risk_Value', ascending=False)

# Save to Excel
df.to_excel('osteoporosis_risk_data.xlsx', index=False, sheet_name='Osteoporosis_Risk')

# Also save to CSV
df.to_csv('osteoporosis_risk_data.csv', index=False)

print("✅ Osteoporosis dataset created successfully!")
print(f"📊 Total records: {len(df)}")
print(f"📋 Health outcomes: {df['Health_Outcome'].nunique()}")
print("\n💾 Files created:")
print("   - osteoporosis_risk_data.xlsx")
print("   - osteoporosis_risk_data.csv")

# Show summary
print("\n📈 Summary by risk metric:")
print("\n🔴 RISK FACTORS (OR/RR > 1.0):")
risk_factors = df[(df['Risk_Value'] > 1.0) & (df['Significant'] == True)]
for idx, row in risk_factors.iterrows():
    print(f"   • {row['Menopause_Age_Definition']}: OR={row['Risk_Value']:.2f} ({row['CI_Lower']:.2f}-{row['CI_Upper']:.2f})")

print("\n🟢 PROTECTIVE FACTORS (OR/RR < 1.0):")
protective = df[(df['Risk_Value'] < 1.0) & (df['Significant'] == True)]
for idx, row in protective.iterrows():
    print(f"   • {row['Menopause_Age_Definition']}: OR={row['Risk_Value']:.2f} ({row['CI_Lower']:.2f}-{row['CI_Upper']:.2f})")

print("\n" + "="*60)
print("🎯 Ready to merge with main dataset!")
print("="*60)