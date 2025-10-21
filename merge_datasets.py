import pandas as pd

# Read both datasets
df1 = pd.read_excel('menopause_risk_data.xlsx')
df2 = pd.read_excel('osteoporosis_risk_data.xlsx')

# Combine datasets
df_combined = pd.concat([df1, df2], ignore_index=True)

# Sort by Health_Outcome and Risk_Value
df_combined = df_combined.sort_values(['Health_Outcome', 'Risk_Value'], ascending=[True, False])

# Save combined dataset
df_combined.to_excel('combined_menopause_data.xlsx', index=False, sheet_name='All_Data')
df_combined.to_csv('combined_menopause_data.csv', index=False)

print("✅ Datasets merged successfully!")
print(f"📊 Total records: {len(df_combined)}")
print(f"📋 Health outcomes: {df_combined['Health_Outcome'].nunique()}")
print(f"📚 Unique studies: {df_combined['Study'].nunique()}")
print(f"👥 Total sample size: {df_combined['Sample_Size'].sum():,.0f}")

# Show summary by health outcome
print("\n📈 Summary by health outcome:")
summary = df_combined.groupby('Health_Outcome').agg({
    'Risk_Value': ['count', 'mean', 'min', 'max'],
    'Sample_Size': 'sum'
})
print(summary)