###
# A function that returns acronym of the sentence
#

def f(name):
    acronym = ''
    words = name.split(' ')
    for i in words:
        acronym += i[0]
    return acronym


print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))
