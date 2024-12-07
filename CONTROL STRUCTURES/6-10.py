# Program to calculate dog's age in dog's years
human_years = int(input("Enter the dog's age in human years: "))

if human_years <= 2:
    # First two years are equal to 10.5 human years each
    dog_years = human_years * 10.5
else:
    # First two years are equal to 21 human years (2 * 10.5)
    # After that, each year equals 4 human years
    dog_years = 21 + (human_years - 2) * 4

print(f"The dog's age in dog's years is {int(dog_years)} years.")