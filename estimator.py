def estimate(profile):
    users = profile["users_per_month"]

    breakdown = {
        "AWS Lambda": users * 2,
        "Amazon RDS (PostgreSQL)": 40000,
        "Amazon S3": 20000,
        "Monitoring & Analytics": 10000
    }

    total = sum(breakdown.values())
    return total, breakdown
