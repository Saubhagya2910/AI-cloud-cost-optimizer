import os
import json
from config import *
from llm import call_llm
import prompts

def save_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        if isinstance(content, (dict, list)):
            json.dump(content, f, indent=4)
        else:
            f.write(content)

def load_json(path):
    if not os.path.exists(path): return None
    with open(path, "r") as f: return json.load(f)

def run_full_pipeline():
    if not os.path.exists(DESCRIPTION_FILE):
        print(" Error: No description found. Please option 1 first.")
        return

    with open(DESCRIPTION_FILE, "r") as f:
        desc = f.read()

    print(" 1/3 Extracting Profile...")
    profile = call_llm(prompts.PROMPT_PROFILE.format(description=desc))
    save_file(PROFILE_FILE, profile)

    print(" 2/3 Generating Synthetic Billing...")
    billing = call_llm(prompts.PROMPT_BILLING.format(profile=json.dumps(profile)))
    save_file(BILLING_FILE, billing)

    print(" 3/3 Analyzing Costs & Recommendations...")
    report = call_llm(prompts.PROMPT_REPORT.format(profile=json.dumps(profile), billing=json.dumps(billing)))
    save_file(REPORT_FILE, report)
    print(f" Full Analysis Complete! Report saved to {REPORT_FILE}")

def main():
    while True:
        print("\n--- CLOUD COST OPTIMIZER (2026) ---")
        print("1.  Enter Project Description")
        print("2.  Run Complete Cost Analysis")
        print("3.  View Recommendations")
        print("4.  Exit")
        choice = input("Select [1-4]: ")

        if choice == "1":
            desc = input("Enter project details: ")
            save_file(DESCRIPTION_FILE, desc)
            print("✅ Description saved.")
        elif choice == "2":
            run_full_pipeline()
        elif choice == "3":
            report = load_json(REPORT_FILE)
            if report:
                for rec in report.get("recommendations", []):
                    print(f"\n💡 {rec['title']} (Save: ₹{rec['potential_savings']})")
                    print(f"   {rec['description']}")
            else:
                print("No report found. Run analysis first.")
        elif choice == "4":
            break

if __name__ == "__main__":
    main()