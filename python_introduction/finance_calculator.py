monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings: {monthly_savings:.2f}")
print(f"Your projected savings after one year with 5% interest: {projected_savings:.2f}")
