# Sums numbers entered by user and calculates the arithmetic mean

total_sum = 0
count = 0  # To count the number of numbers entered

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    
    total_sum += number
    count += 1  # Increment the count for each number entered

# Calculate the arithmetic mean
if count > 0:
    mean = total_sum / count
    print(f"The total sum of the numbers is: {total_sum}")
    print(f"The arithmetic mean of the numbers is: {mean}")
else:
    print("No numbers were entered.")