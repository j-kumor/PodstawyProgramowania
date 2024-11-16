###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = cm // 30.48 # // operator dzielenia bez reszty
inches = (cm % 30.48) / 2.54 # % operator obliczajacy reszte z dzielenia

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')