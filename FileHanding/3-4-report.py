###
# Calculates the total value of money spent
#
import re 

email_file = 'report.txt'

with open(email_file, 'r', encoding='utf8') as f:
    email = f.read()

# regular expression pattern
# for amounts
pattern = '€(\d+)'

amounts = re.findall(pattern, email)

total_amount = 0
for amount in amounts:
    total_amount += int(amount)

print(f'Total spendings: €{total_amount}')
