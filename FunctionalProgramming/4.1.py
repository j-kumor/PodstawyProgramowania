# List of employees
employees = [
    "SMITH Lucy", "JONES Janet", "LEE Jerry", 
    "JACKSON Peter", "JOHNSON Rick", "LEWIS Terry", 
    "CLARKE Robin"
]

# Filter employees whose surname starts with 'J'
emp_J = list(filter(lambda e: e.split()[0].startswith('J'), employees))

# Display the filtered list
for emp in emp_J:
    print(emp)
