class Statistics:
    def __init__(self):
        """Initializes an empty list to store numbers."""
        self.numbers = []

    def add_number(self, number):
        """Adds a number to the list."""
        self.numbers.append(number)

    def display_numbers(self):
        """Displays all numbers in the list, separated by a space."""
        print("Numbers:", " ".join(map(str, self.numbers)))

    def get_max(self):
        """Returns the greatest number in the list."""
        return max(self.numbers)

    def get_min(self):
        """Returns the smallest number in the list."""
        return min(self.numbers)

    def get_mean(self):
        """Calculates the arithmetic mean of the numbers."""
        return sum(self.numbers) / len(self.numbers)

    def get_median(self):
        """Calculates the median of the numbers."""
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        if n % 2 == 1:
            return sorted_numbers[n // 2]
        else:
            middle1 = sorted_numbers[(n // 2) - 1]
            middle2 = sorted_numbers[n // 2]
            return (middle1 + middle2) / 2

    def print_statistics(self):
        """Prints all calculated statistics."""
        print(f"Maximum: {self.get_max()}")
        print(f"Minimum: {self.get_min()}")
        print(f"Arithmetic Mean: {self.get_mean():.2f}")
        print(f"Median: {self.get_median()}")

def main():
    # Numbers to be processed
    numbers = [12, 37, 6, 9, 17]

    # Create an instance of the Statistics class
    stats = Statistics()

    # Add numbers to the statistics object
    for number in numbers:
        stats.add_number(number)

    # Display all numbers
    stats.display_numbers()

    # Print calculated statistics
    stats.print_statistics()

if __name__ == "__main__":
    main()
