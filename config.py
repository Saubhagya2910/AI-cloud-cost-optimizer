import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"

OUTPUT_DIR = "outputs"
DESCRIPTION_FILE = f"{OUTPUT_DIR}/project_description.txt"
PROFILE_FILE = f"{OUTPUT_DIR}/project_profile.json"
BILLING_FILE = f"{OUTPUT_DIR}/mock_billing.json"
REPORT_FILE = f"{OUTPUT_DIR}/cost_optimization_report.json"