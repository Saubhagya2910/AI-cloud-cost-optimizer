PROMPT_PROFILE = """Extract structured project profile from this description:

{description}

Output ONLY JSON with these exact fields:
- name: Project name (string)
- budget_inr_per_month: Monthly budget in INR (number)
- description: Short summary (string)  
- tech_stack: Object with frontend/backend/database/etc keys
- non_functional_requirements: Array of strings like ["scalability"]"""

PROMPT_BILLING = """Generate 12-20 realistic AWS billing records for this project:

{profile}

Requirements:
- Months: 2025-01 to 2025-05 (spread across)
- Services: EC2, RDS, S3, Lambda, CloudWatch, etc.
- Region: ap-south-1 
- Total cost: 80-120% of budget"""

PROMPT_REPORT = """Analyze costs and generate optimization report:

Project: {profile}
Billing: {billing}

Compute: total_monthly_cost, service_costs, budget_variance, 6-10 recommendations"""

