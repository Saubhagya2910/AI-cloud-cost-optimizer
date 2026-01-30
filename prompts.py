PROMPT_PROFILE = """
Extract a structured project profile from this description:
{description}

Return ONLY a JSON object with:
- name
- budget_inr_per_month (integer)
- description (summary)
- tech_stack (frontend, backend, database, proxy, hosting)
- non_functional_requirements (list)
"""

PROMPT_BILLING = """
Based on this profile: {profile}
Generate 12-20 realistic synthetic cloud billing records for the current month.
Return ONLY a JSON list of objects. Each object must have:
month, service, resource_id, region, usage_type, usage_quantity, unit, cost_inr, desc.
Ensure total cost is realistic relative to the tech stack.
"""

PROMPT_REPORT = """
Profile: {profile}
Billing: {billing}

Analyze the costs. Return ONLY a JSON object:
- project_name
- analysis (total_monthly_cost, budget, budget_variance, service_costs, high_cost_services, is_over_budget)
- recommendations (list of objects with: title, service, current_cost, potential_savings, recommendation_type, description, implementation_effort, risk_level, steps, cloud_providers)
- summary (total_potential_savings, savings_percentage, recommendations_count)
Provide 6-10 recommendations including open-source and multi-cloud options.
"""