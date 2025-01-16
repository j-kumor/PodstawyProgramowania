# List of test results
test_results = [
    {"name": "Peter", "result": 27},
    {"name": "Anna", "result": 63},
    {"name": "Robert", "result": 92},
    {"name": "Paul", "result": 46},
    {"name": "Barbara", "result": 52}
]

# Use filter() and lambda function to get students with scores between 50 and 70
filtered_students = list(filter(lambda student: 50 <= student["result"] <= 70, test_results))

# Display the result
for student in filtered_students:
    print(f"{student['name']} - {student['result']} points")
