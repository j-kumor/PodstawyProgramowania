###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():  # Sprawdzamy, czy znak jest literą
        # Zmieniamy literę, przesuwając ją o jeden w prawo
        encrypted_char = chr(ord(char) + 1) if char != 'z' and char != 'Z' else chr(ord(char) - 25)
    else:
        # Jeśli to nie litera, dodajemy znak bez zmian
        encrypted_char = char

    encrypted_text += encrypted_char

print(plain_text)
print(encrypted_text)