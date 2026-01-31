import os
import json
import prompts
from llm import call_llm
from config import *

def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def run_pipeline():
    desc_path = "outputs/description.txt"
    if not os.path.exists(desc_path):
        print("\n❌ Error: Please enter a description first (Option 1)!")
        return

    with open(desc_path, "r", encoding="utf-8") as f:
        desc = f.read()

    print("\n🚀 Step 1: Extracting Multi-Cloud Profile...")
    profile = call_llm(prompts.PROMPT_PROFILE.format(description=desc))
    save_json(PROFILE_FILE, profile)

    print("🚀 Step 2: Generating Cross-Cloud Billing...")
    billing = call_llm(prompts.PROMPT_BILLING.format(profile=json.dumps(profile)))
    save_json(BILLING_FILE, billing)

    print("🚀 Step 3: Creating Optimization Report...")
    report = call_llm(prompts.PROMPT_REPORT.format(profile=json.dumps(profile), billing=json.dumps(billing)))
    save_json(REPORT_FILE, report)
    
    print("\n✅ Success! Analysis complete. View results in Option 3.")

def show_recommendations():
    if not os.path.exists(BILLING_FILE) or not os.path.exists(REPORT_FILE):
        print("\n⚠️ No data found! Please run Option 2 (Analysis) first.")
        return

    # 1. Display Billing Breakdown Table
    with open(BILLING_FILE, "r", encoding="utf-8") as f:
        billing_data = json.load(f)
    
    print("\n" + "="*65)
    print(f"{'PROVIDER':<10} | {'SERVICE':<20} | {'REGION':<15} | {'COST (INR)':<10}")
    print("-" * 65)
    total = 0
    for item in billing_data:
        cost = item.get('cost_inr', 0)
        total += cost
        print(f"{item.get('provider'):<10} | {item.get('service'):<20} | {item.get('region'):<15} | ₹{cost:<10}")
    print("-" * 65)
    print(f"{'TOTAL ESTIMATED MONTHLY BILL:':<49} | ₹{total:<10}")
    print("="*65)

    # 2. Display AI Recommendations
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        report = json.load(f)
        print("\n💡 MULTI-CLOUD OPTIMIZATION STRATEGY:")
        recs = report.get('recommendations', [])
        for i, rec in enumerate(recs, 1):
            if isinstance(rec, dict):
                print(f"\n{i}. {rec.get('title', 'Recommendation').upper()}")
                print(f"   {rec.get('description', '')}")
                print(f"   Estimated Monthly Savings: ₹{rec.get('savings', 'N/A')}")
            else:
                print(f"\n{i}. {rec}")

def main():
    while True:
        print("\n--- CLOUD COST OPTIMIZER (Multi-Cloud v2.0) ---")
        print("1. Enter Project Description")
        print("2. Run Complete Analysis")
        print("3. View Billing & Recommendations")
        print("4. Exit")
        
        choice = input("\nSelect [1-4]: ").strip()
        
        if choice == "1":
            d = input("\nDescribe your project (e.g., tech stack, budget, users): ").strip()
            os.makedirs("outputs", exist_ok=True)
            with open("outputs/description.txt", "w", encoding="utf-8") as f:
                f.write(d)
            print("✅ Description saved successfully.")
        elif choice == "2":
            run_pipeline()
        elif choice == "3":
            show_recommendations()
        elif choice == "4":
            print("\nExiting. Thank you for using the Optimizer! 👋")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()