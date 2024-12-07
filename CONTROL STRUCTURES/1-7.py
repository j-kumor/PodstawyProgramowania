###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#

basic_salary = 5000
total_salary = 0
bonus = 0.15  # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included? {"Yes" if is_bonus else "No"}')
print(f'Total salary: {total_salary} PLN')

# Case 1: No bonus
no_bonus_salary = basic_salary
print(f'Case 1 - No bonus: {no_bonus_salary} PLN')

# Case 2: Bonus of 30%
bonus_30_percent = basic_salary * 0.30
salary_with_30_percent_bonus = basic_salary + bonus_30_percent
print(f'Case 2 - 30% bonus: {salary_with_30_percent_bonus} PLN')