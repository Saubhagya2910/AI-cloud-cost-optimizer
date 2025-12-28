#!/usr/bin/env python3
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from llm_client import LLMClient
from prompts import PROMPT_PROFILE, PROMPT_BILLING, PROMPT_REPORT
from utils import save_json, load_json

load_dotenv()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def safe_print_report(report):
    """SAFE version - handles list/dict errors"""
    print("\n=== RECOMMENDATIONS ===")
    try:
        if isinstance(report, dict) and 'analysis' in report:
            analysis = report['analysis']
            print(f"Total Cost: ₹{analysis.get('total_monthly_cost', 'N/A'):,}")
            print(f"Budget: ₹{analysis.get('budget', 'N/A'):,}")
            print(f"Variance: ₹{analysis.get('budget_variance', 'N/A'):,}")
            print(f"Over Budget: {'YES' if analysis.get('is_over_budget') else 'NO'}\n")
            
            recs = report.get('recommendations', [])
            for i, rec in enumerate(recs[:5], 1):
                print(f"{i}. {rec.get('title', 'No title')}")
                print(f"   Savings: ₹{rec.get('potential_savings', 0):,}")
                print()
        else:
            print("📊 Report structure: OK")
            print(json.dumps(report, indent=2)[:500] + "...")
    except Exception as e:
        print(f"Report preview: {json.dumps(report, indent=2)[:300]}...")

def main():
    client = LLMClient()
    outputs_dir = Path("outputs")
    outputs_dir.mkdir(exist_ok=True)
    
    while True:
        clear_screen()
        print("=== AI-Powered Cloud Cost Optimizer ===\n")
        print("1. Enter new project description")
        print("2. Run Complete Cost Analysis")
        print("3. View Recommendations")
        print("4. Export Report")
        print("5. Exit")
        
        choice = input("\nEnter choice (1-5): ").strip()
        
        if choice == '1':
            desc = input("\nEnter project description:\n")
            with open('project_description.txt', 'w', encoding='utf-8') as f:
                f.write(desc)
            
            print("\nGenerating project profile...")
            profile = client.generate(PROMPT_PROFILE.format(description=desc))
            save_json(outputs_dir / "project_profile.json", profile)
            print("✅ Profile saved!")
            input("\nPress Enter...")
            
        elif choice == '2':
            if not (outputs_dir / "project_profile.json").exists():
                print("❌ Run option 1 first!")
                input("Press Enter...")
                continue
                
            profile = load_json(outputs_dir / "project_profile.json")
            
            print("Generating synthetic billing...")
            billing = client.generate(PROMPT_BILLING.format(profile=json.dumps(profile, indent=2)))
            save_json(outputs_dir / "mock_billing.json", billing)
            
            print("Generating cost analysis...")
            report = client.generate(PROMPT_REPORT.format(
                profile=json.dumps(profile, indent=2),
                billing=json.dumps(billing, indent=2)
            ))
            save_json(outputs_dir / "cost_optimization_report.json", report)
            
            print("✅ COMPLETE PIPELINE SUCCESS!")
            print("Files in /outputs/ folder ✓")
            input("\nPress Enter...")
            
        elif choice == '3':
            if not (outputs_dir / "cost_optimization_report.json").exists():
                print("❌ Run option 2 first!")
                input("Press Enter...")
                continue
                
            report = load_json(outputs_dir / "cost_optimization_report.json")
            safe_print_report(report)
            input("\nPress Enter...")
            
        elif choice == '4':
            print("✅ Reports in /outputs/:")
            for f in outputs_dir.glob("*.json"):
                print(f"   📄 {f.name}")
            input("\nPress Enter...")
            
        elif choice == '5':
            print("✅ Ready for GitHub submission!")
            break
            
        else:
            input("Invalid choice. Press Enter...")

if __name__ == "__main__":
    main()

