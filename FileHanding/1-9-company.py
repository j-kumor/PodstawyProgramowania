# Prints employees employed in a specified position.
#

file_name = 'it_company.csv'

job_title = 'Software Engineer'

with open(file_name, 'r') as file:
    lines = file.readlines()

employee_number = 1

for line in lines:
    if job_title in line:
        print(f"{employee_number}. {line.strip()}")
        employee_number += 1