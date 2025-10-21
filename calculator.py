import pandas as pd

class OvarianAgingCalculator:
    def __init__(self, discount_rate=0.03):
        """Initialize calculator with discount rate"""
        self.discount_rate = discount_rate
        self.risks = None
        self.baseline = None
        self.costs = None
        
    def load_data(self):
        """Load data from Excel files"""
        print("Loading data...")
        self.risks = pd.read_excel('datasets/combined_menopause_data.xlsx')
        self.baseline = pd.read_excel('datasets/baseline_incidence_rates.xlsx')
        self.costs = pd.read_excel('datasets/disease_treatment_costs.xlsx')
        print("Data loaded successfully")
        print(f"  - Risks: {len(self.risks)} records")
        print(f"  - Baseline rates: {len(self.baseline)} records")
        print(f"  - Costs: {len(self.costs)} records")
        
    def calculate_discount_factor(self, years):
        """Calculate Present Value Factor: PV = [1 - (1+r)^(-years)] / r"""
        return (1 - (1 + self.discount_rate) ** (-years)) / self.discount_rate
    
    def _map_disease_name(self, disease_name, dataset_type):
        """Map disease names to match different datasets"""
        mappings = {
            'baseline': {
                'Type 2 Diabetes Mellitus (T2DM)': 'Type_2_Diabetes',
                'Dementia (any type)': 'Dementia',
            },
            'costs': {
                'Type 2 Diabetes Mellitus (T2DM)': 'Type_2_Diabetes',
                'Dementia (any type)': 'Dementia',
            }
        }
        return mappings.get(dataset_type, {}).get(disease_name, disease_name)

    def calculate_disease(self, disease_name, years_of_benefit):
        """Calculate health and economic impact for a single disease"""

        # Step 1: Get Baseline Rate (incidence per 100K women)
        baseline_name = self._map_disease_name(disease_name, 'baseline')
        baseline_rate = self.baseline[
            self.baseline['Disease'] == baseline_name
        ]['Rate_per_100K'].values[0]

        # Step 2: Get Risk Ratio for early menopause
        risk_ratio = self.risks[
            self.risks['Health_Outcome'] == disease_name
        ]['Risk_Value'].values[0]
        
        # Step 2: Calculate Early Menopause Rate
        early_rate = baseline_rate * risk_ratio
        
        # Step 3: Calculate Cases Prevented
        cases_prevented = early_rate - baseline_rate
        
        # Step 4: Get Annual Treatment Cost
        cost_name = self._map_disease_name(disease_name, 'costs')
        annual_cost = self.costs[
            self.costs['Disease'] == cost_name
        ]['Amount_USD'].values[0]
        
        # Step 5: Calculate Discount Factor
        pv_factor = self.calculate_discount_factor(years_of_benefit)
        
        # Step 5: Calculate Total Economic Value
        economic_value = cases_prevented * annual_cost * pv_factor
        
        return {
            'disease': disease_name,
            'baseline_rate': baseline_rate,
            'risk_ratio': risk_ratio,
            'early_rate': early_rate,
            'cases_prevented': cases_prevented,
            'annual_cost': annual_cost,
            'years': years_of_benefit,
            'pv_factor': pv_factor,
            'economic_value': economic_value
        }
    
    def calculate_net_benefit(self, benefits_list, risks_list):
        """
        Calculate total net benefit from delaying menopause
        
        Args:
            benefits_list: List of tuples [('CHD', 6), ('Stroke', 6), ...]
            risks_list: List of tuples [('Breast_Cancer', 6), ...]
        
        Returns:
            Dictionary with total benefits, costs, and net benefit
        """
        
        print("\n" + "="*60)
        print("CALCULATING BENEFITS OF 5-YEAR MENOPAUSE DELAY")
        print("="*60)
        
        # Calculate Benefits
        print("\n=== POSITIVE EFFECTS (Benefits) ===")
        total_benefits = 0
        benefit_results = []
        
        for disease, years in benefits_list:
            result = self.calculate_disease(disease, years)
            benefit_results.append(result)
            total_benefits += result['economic_value']
            
            print(f"\n[+] {disease}:")
            print(f"   Baseline rate: {result['baseline_rate']:.0f} per 100K")
            print(f"   Risk ratio: {result['risk_ratio']:.2f}")
            print(f"   Cases prevented: {result['cases_prevented']:.0f} per 100K women")
            print(f"   Annual cost: ${result['annual_cost']:,.0f}")
            print(f"   Economic value: ${result['economic_value']:,.0f}")
        
        # Calculate Risks
        print("\n=== NEGATIVE EFFECTS (Risks) ===")
        total_costs = 0
        risk_results = []
        
        for disease, years in risks_list:
            result = self.calculate_disease(disease, years)
            risk_results.append(result)
            total_costs += result['economic_value']
            
            print(f"\n[-] {disease}:")
            print(f"   Baseline rate: {result['baseline_rate']:.0f} per 100K")
            print(f"   Risk ratio: {result['risk_ratio']:.2f}")
            print(f"   Cases added: {result['cases_prevented']:.0f} per 100K women")
            print(f"   Annual cost: ${result['annual_cost']:,.0f}")
            print(f"   Economic cost: ${result['economic_value']:,.0f}")
        
        # Calculate Net Benefit
        net_benefit = total_benefits - total_costs
        
        print("\n" + "="*60)
        print("FINAL RESULTS")
        print("="*60)
        print(f"[+] Total Benefits:  ${total_benefits:>15,.0f}")
        print(f"[-] Total Costs:     ${total_costs:>15,.0f}")
        print("-" * 60)
        print(f"NET BENEFIT:         ${net_benefit:>15,.0f} per 100K women")
        print("="*60)
        
        return {
            'total_benefits': total_benefits,
            'total_costs': total_costs,
            'net_benefit': net_benefit,
            'benefit_results': benefit_results,
            'risk_results': risk_results
        }


# ============================================
# MAIN CODE - Runs when you execute: python calculator.py
# ============================================

if __name__ == "__main__":
    
    # 1. Create calculator instance
    calc = OvarianAgingCalculator()
    
    # 2. Load data from Excel files
    calc.load_data()
    
    # 3. Define diseases for calculation
    
    # Positive effects (Benefits)
    benefits = [
        ('Coronary Heart Disease (CHD)', 6),      # Coronary Heart Disease
        ('Stroke', 6),                            # Stroke
        ('Osteoporotic Fracture', 6),             # Osteoporotic Fracture
        ('Dementia (any type)', 6),               # Dementia
        ('Type 2 Diabetes Mellitus (T2DM)', 6),   # Type 2 Diabetes
    ]
    
    # Negative effects (Risks)
    risks = [
        # ('Breast_Cancer', 6),  # Uncomment when you add this data
    ]
    
    # 4. Run calculation
    result = calc.calculate_net_benefit(benefits, risks)
    
    # 5. Show scaled results
    print(f"\n\nFor 1 million women this would be:")
    print(f"   ${result['net_benefit'] * 10:,.0f}")