AI-Powered Cloud Cost Optimizer 🚀
LLM-Driven Multi-Cloud Cost Optimization Tool
Converts plain-English project descriptions into structured project profiles, generates realistic cloud billing data, and produces actionable multi-cloud cost optimization recommendations via a menu-driven CLI.

✨ Key Features

✅ LLM-Based Project Profile Extraction
Parses free-form descriptions into structured JSON.

✅ Synthetic Billing Data Generation
Generates 12–20 realistic cloud billing records based on project scope and budget.

✅ Cost Optimization Recommendations
Produces 6–10 actionable recommendations with:
Cost savings estimation
Implementation effort
Risk level
Multi-cloud alternatives

✅ Menu-Driven CLI
Simple, Windows-friendly command-line interface.

✅ Multi-Cloud Coverage
AWS, Azure, GCP, and open-source alternatives.

✅ Production-Ready Design
Includes error handling, LLM retry logic, and JSON validation.

🧭 Workflow Overview
User enters project description
↓
LLM generates project_profile.json
↓
Synthetic billing data → mock_billing.json
↓
Cost analysis & recommendations → cost_optimization_report.json

🚀 Quick Start
🔹 Prerequisites
   Python 3.10+
   Hugging Face account (free API token)

🔹 Setup
1. Clone the repository
   git clone https://github.com/Saubhagya2910/AI-cloud-cost-optimizer.git
   cd AI_CLOUD_COST_OPTIMIZER

2. Install dependencies
   python -m pip install -r requirements.txt

3. Configure environment variables
   cp .env.example .env

   Edit .env:
   HF_TOKEN=your_huggingface_token_here

4. Run the CLI
   python cost_optimizer.py

📁 Project Structure
AI_CLOUD_COST_OPTIMIZER/
├── cost_optimizer.py
├── llm_client.py
├── prompts.py
├── utils.py
├── project_description.txt
├── outputs/
│   ├── project_profile.json
│   ├── mock_billing.json
│   └── cost_optimization_report.json
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

🎮 CLI Menu
=== AI-Powered Cloud Cost Optimizer ===
1. Enter Project Description
2. Run Complete Cost Analysis
3. View Recommendations
4. Export Report
5. Exit

📝 Sample Input
We are building a food delivery app for 10,000 users per month.
Budget: ₹50,000 per month.
Tech stack: Node.js backend, PostgreSQL database,
object storage for images, monitoring, and analytics.
Non-functional requirements: scalability and cost efficiency.

📤 Generated Outputs

project_profile.json
mock_billing.json
cost_optimization_report.json

📊 Sample Project Profile
{
  "name": "Food Delivery App",
  "budget_inr_per_month": 50000,
  "description": "Scalable food delivery platform for ~10k users",
  "tech_stack": {
    "backend": "Node.js",
    "database": "PostgreSQL",
    "storage": "Object Storage",
    "monitoring": "Basic monitoring"
  },
  "non_functional_requirements": [
    "Scalability",
    "Cost efficiency"
  ]
}

💡 Sample Recommendation
{
  "title": "Switch to Reserved Instances",
  "service": "Compute",
  "current_cost": 15000,
  "potential_savings": 4000,
  "recommendation_type": "reserved_instances",
  "implementation_effort": "Low",
  "risk_level": "Low",
  "cloud_providers": ["AWS", "Azure", "GCP"],
  "steps": [
    "Analyze compute usage patterns",
    "Purchase reserved instances for stable workloads"
  ]
}

🛠️ Tech Stack
Component	Technology
LLM	Meta-Llama-3-8B-Instruct
Language	Python 3.10+
Interface	CLI
Data	JSON

📌 Submission Note
Built for OpenText Internship Assignment
✔ All mandatory features implemented
✔ Ready for evaluation

👉 Run python cost_optimizer.py
