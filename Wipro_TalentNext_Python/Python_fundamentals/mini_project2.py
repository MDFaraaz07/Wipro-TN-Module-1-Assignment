
# Hosting cost per hour
cost_per_hour = 0.51

# Calculate costs
cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

# With $918 budget, how many days can we operate?
budget = 918
days_with_budget = budget / cost_per_day

# Display the results
print(f"Cost to operate one server per day: ${cost_per_day:.2f}")
print(f"Cost to operate one server per week: ${cost_per_week:.2f}")
print(f"Cost to operate one server per month: ${cost_per_month:.2f}")
print(f"With ${budget}, you can operate one server for {days_with_budget:.2f} days.")
