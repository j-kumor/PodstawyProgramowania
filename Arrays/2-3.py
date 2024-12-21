# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

total_food = 0
total_transport = 0
total_utilities = 0

# Initialize variables to store total expenses for each week
week_totals = []

# Calculate expenses for each category and each week
for week in monthly_expenses:
    total_food += week[0]
    total_transport += week[1]
    total_utilities += week[2]
    week_totals.append(sum(week))  # Calculate and store the total expenses for the week

total_monthly_expenses = total_food + total_transport + total_utilities

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:', monthly_expenses[0][0] + monthly_expenses[0][1] + monthly_expenses[0][2])
print('Week 2:', monthly_expenses[1][0] + monthly_expenses[1][1] + monthly_expenses[1][2])
print('Week 3:', monthly_expenses[2][0] + monthly_expenses[2][1] + monthly_expenses[2][2])
print('Week 4:', monthly_expenses[3][0] + monthly_expenses[3][1] + monthly_expenses[3][2])
print('---------------')
print('TOTAL:', total_monthly_expenses)
