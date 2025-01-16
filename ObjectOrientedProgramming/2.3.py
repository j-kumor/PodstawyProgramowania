class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km  # Value in € (e.g., €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Receipt:")
        print(f"Distance: {self.distance} km")
        print(f"Rate: €{self.rate_per_km} per km")
        print(f"Fare: €{self.fare:.2f}")
        print("------------------")

def main():
    ride1 = TaxiRide(rate_per_km=2)  # Rate €2 per km
    ride1.calculate_fare(distance=10)  # Distance 10 km
    print("Ride 1:")
    ride1.print_receipt()

    ride2 = TaxiRide(rate_per_km=1.5)  # Rate €1.5 per km
    ride2.calculate_fare(distance=15)  # Distance 15 km
    print("Ride 2:")
    ride2.print_receipt()

if __name__ == "__main__":
    main()
