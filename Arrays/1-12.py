categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Find the index of the maximum expense
max_expense_index = expenses.index(max(expenses))

most_expensive_category = categories[max_expense_index]
most_expensive_expense = expenses[max_expense_index]

print("The most expensive category is:", most_expensive_category)
print("The expense in this category is:", most_expensive_expense)
