###
# A function that returns the given text with all characters separated by a dash sign
#

def f(text):
    if text:
        dash_sign_text = text[0]  # first letter
        for i in range(1, len(text)):
            dash_sign_text += '-' + text[i]
        return dash_sign_text
    return ''

print(f("Univesity"))
print(f('UE'))
print(f('x'))
print(f(''))
