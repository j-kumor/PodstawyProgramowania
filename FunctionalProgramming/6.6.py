# List of employee data (last name, first name)
employees = [
    ("Smith", "Lucy"), ("Jones", "Janet"), ("Lee", "Jerry"),
    ("Jackson", "Peter"), ("Johnson", "Rick"),
    ("Lewis", "Terry"), ("Clarke", "Robin")
]

# Use map() to format the employee names
formatted_employees = list(map(lambda e: f"{e[0].upper()}, {e[1]}", employees))

# Display the result
for emp in formatted_employees:
    print(emp)
