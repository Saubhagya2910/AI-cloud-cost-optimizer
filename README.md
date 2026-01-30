🛠️ Tech Stack
Language: Python 3.10+

LLM API: Groq (Model: llama-3.3-70b-versatile)

CLI Framework: rich for formatted console output

Environment Management: python-dotenv

🚀 Setup & Installation
Clone the Repository:

Bash
git clone <your-repo-url>
cd cloud-cost-optimizer
Create a Virtual Environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables: Create a .env file in the root directory and add your Groq API key:

Code snippet
GROQ_API_KEY=your_api_key_here
📂 Project Structure
main.py: The central orchestrator for the CLI and logic flow.

llm.py: Handles communication with the Groq API.

prompts.py: Contains the system instructions for Profile Extraction, Billing, and Reports.

config.py: Manages file paths and API settings.

outputs/: Directory where all generated JSON and text artifacts are stored.

🔄 Workflow
Step 1: Profile Extraction – Converts a free-form description into project_profile.json.

Step 2: Billing Generation – Creates 12–20 realistic, budget-aware records in mock_billing.json.

Step 3: Cost Analysis – Compares spending against budget and generates cost_optimization_report.json.

Step 4: Recommendations – Provides 6–10 actionable multi-cloud and open-source alternatives.

📝 Example Artifacts
After running the analysis, you can find the following in the outputs/ folder:

project_description.txt: The raw user input.

project_profile.json: Structured tech stack and budget data.

mock_billing.json: Detailed synthetic resource usage.

cost_optimization_report.json: Final analysis and savings suggestions.
