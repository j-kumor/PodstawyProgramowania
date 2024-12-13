###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter surname: ')
age = keyboard.input_integer('Enter your age: ')
salary = keyboard.input_real('Enter your salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Surname', last_name)
print('Age', age)
if is_salary_hidden:
    print('Salary is hidden')
else:
    print('Salary', salary)
