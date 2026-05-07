import pandas as pd
from datetime import datetime

def audit_vendor_soc_reports():
    """
    Third-Party Risk Management (TPRM) Audit Tool.
    Flags vendors with expired SOC reports or missing Complementary User Entity Controls (CUECs).
    """
    print("--- Initiating Vendor Risk Assessment ---")
    
    # Mock Vendor Database (Information Produced by Entity)
    vendors = pd.DataFrame({
        'Vendor_Name': ['AWS', 'Salesforce', 'Stripe', 'LegacyHR_App'],
        'Service_Type': ['Cloud Hosting', 'CRM', 'Payment Gateway', 'HRMS'],
        'SOC_Expiry_Date': ['2024-12-31', '2024-11-15', '2024-10-01', '2023-05-20'],
        'CUECs_Mapped': ['Yes', 'Yes', 'Yes', 'No']
    })

    vendors['SOC_Expiry_Date'] = pd.to_datetime(vendors['SOC_Expiry_Date'])
    today = pd.to_datetime('2023-10-25') # Simulated audit date

    # Logic: Find Expired Reports OR Unmapped CUECs
    expired = vendors[vendors['SOC_Expiry_Date'] < today]
    unmapped = vendors[vendors['CUECs_Mapped'] == 'No']

    print(f"Total Vendors Audited: {len(vendors)}")
    
    if not expired.empty:
        print("\n[!] DEFICIENCY: Expired SOC Reports Detected!")
        for _, row in expired.iterrows():
            print(f" - {row['Vendor_Name']} ({row['Service_Type']}) expired on {row['SOC_Expiry_Date'].date()}")
            
    if not unmapped.empty:
        print("\n[!] DEFICIENCY: CUECs Not Mapped for the following vendors:")
        for _, row in unmapped.iterrows():
            print(f" - {row['Vendor_Name']}")

if __name__ == "__main__":
    audit_vendor_soc_reports()
