from estimator import estimate


def run_billing(profile):
    total, breakdown = estimate(profile)

    billing = {
        "total_monthly_cost": total,
        "within_budget": total <= profile["budget"],
        "cost_breakdown": breakdown
    }

    return billing
