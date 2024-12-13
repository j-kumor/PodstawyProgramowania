###
# A function that removes spaces from sentences
#

def f(sentence):
    text = ''
    for i in sentence:
        if i == ' ':
            continue
        else:
            text += i
    return text


print(f("integrated development environment"))
print(f("A programming language is a system of notation for writing computer programs"))
