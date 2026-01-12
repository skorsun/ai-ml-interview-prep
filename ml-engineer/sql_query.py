"""
SQL Query Example - User Purchase Pattern Analysis

This query analyzes user purchase patterns and calculates typical pace between purchases.

The original query had an error on line 21:
ERROR: function round(interval, integer) does not exist
LINE 21:     ROUND(p.avg_days_between, 1) as typical_pace_days,

PostgreSQL's ROUND function doesn't work directly with INTERVAL types.
Solution: Convert interval to days (numeric) first, then round.
"""

# Original query with error (commented out)
ORIGINAL_QUERY = """
WITH purchase_intervals AS (
    SELECT 
        user_id,
        purchase_date,
        LAG(purchase_date) OVER (PARTITION BY user_id ORDER BY purchase_date) as prev_purchase_date
    FROM purchases
),
user_pace AS (
    SELECT 
        user_id,
        AVG(purchase_date - prev_purchase_date) as avg_days_between
    FROM purchase_intervals
    WHERE prev_purchase_date IS NOT NULL
    GROUP BY user_id
)
SELECT 
    u.user_id,
    u.username,
    ROUND(p.avg_days_between, 1) as typical_pace_days,  -- ERROR: function round(interval, integer) does not exist
    COUNT(pur.purchase_id) as total_purchases
FROM users u
LEFT JOIN user_pace p ON u.user_id = p.user_id
LEFT JOIN purchases pur ON u.user_id = pur.user_id
GROUP BY u.user_id, u.username, p.avg_days_between
ORDER BY typical_pace_days;
"""

# Fixed query - Convert interval to days before rounding
FIXED_QUERY = """
WITH purchase_intervals AS (
    SELECT 
        user_id,
        purchase_date,
        LAG(purchase_date) OVER (PARTITION BY user_id ORDER BY purchase_date) as prev_purchase_date
    FROM purchases
),
user_pace AS (
    SELECT 
        user_id,
        AVG(purchase_date - prev_purchase_date) as avg_days_between
    FROM purchase_intervals
    WHERE prev_purchase_date IS NOT NULL
    GROUP BY user_id
)
SELECT 
    u.user_id,
    u.username,
    ROUND(EXTRACT(EPOCH FROM p.avg_days_between) / 86400, 1) as typical_pace_days,  -- Fixed: Convert interval to days
    COUNT(pur.purchase_id) as total_purchases
FROM users u
LEFT JOIN user_pace p ON u.user_id = p.user_id
LEFT JOIN purchases pur ON u.user_id = pur.user_id
GROUP BY u.user_id, u.username, p.avg_days_between
ORDER BY typical_pace_days;
"""

# Alternative solution using EXTRACT(DAY) - simpler but less precise for intervals > 1 month
ALTERNATIVE_QUERY = """
WITH purchase_intervals AS (
    SELECT 
        user_id,
        purchase_date,
        LAG(purchase_date) OVER (PARTITION BY user_id ORDER BY purchase_date) as prev_purchase_date
    FROM purchases
),
user_pace AS (
    SELECT 
        user_id,
        AVG(purchase_date - prev_purchase_date) as avg_days_between
    FROM purchase_intervals
    WHERE prev_purchase_date IS NOT NULL
    GROUP BY user_id
)
SELECT 
    u.user_id,
    u.username,
    ROUND((EXTRACT(EPOCH FROM p.avg_days_between) / 86400.0)::numeric, 1) as typical_pace_days,  -- Alternative with explicit casting
    COUNT(pur.purchase_id) as total_purchases
FROM users u
LEFT JOIN user_pace p ON u.user_id = p.user_id
LEFT JOIN purchases pur ON u.user_id = pur.user_id
GROUP BY u.user_id, u.username, p.avg_days_between
ORDER BY typical_pace_days;
"""


def get_query():
    """Returns the fixed SQL query"""
    return FIXED_QUERY


if __name__ == "__main__":
    print("Fixed SQL Query:")
    print("=" * 80)
    print(FIXED_QUERY)
    print("\n" + "=" * 80)
    print("\nKey Fix:")
    print("Changed: ROUND(p.avg_days_between, 1)")
    print("To:      ROUND(EXTRACT(EPOCH FROM p.avg_days_between) / 86400, 1)")
    print("\nExplanation:")
    print("- EXTRACT(EPOCH FROM interval) returns total seconds")
    print("- Divide by 86400 to convert seconds to days")
    print("- ROUND() then works on the numeric value")
