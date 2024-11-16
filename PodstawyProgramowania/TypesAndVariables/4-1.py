#zadanie 4.1
#Modify the program to print the student's age and height in addition to the name, as below.

#My name is Adam.
#I am ... years old, and my height is ... cm.
#In 6 years I will be ... years old.  

name = input('Podaj imie: ')
wzrost = int(input('Podaj wzrost w cm: '))
wiek = int(input('Podaj wiek: '))

print(f'My name is {name}.')
print(f'I am {wiek} years old, and my height is {wzrost} cm.')
print(f'In 6 years I will be {wiek + 6} years old.')
