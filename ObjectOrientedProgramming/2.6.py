class Phone:
    def __init__(self, brand, model, battery_percentage):
        # States
        self.brand = brand
        self.model = model
        self.battery_percentage = battery_percentage

    # Behaviors
    def make_call(self, contact):
        if self.battery_percentage > 5:
            print(f"Calling {contact} from {self.model}...")
            self.battery_percentage -= 5  # Simulate battery drain
        else:
            print(f"Battery too low to make a call on {self.model}.")

    def send_message(self, contact, message):
        if self.battery_percentage > 3:
            print(f"Sending message to {contact}: {message}")
            self.battery_percentage -= 3  # Simulate battery drain
        else:
            print(f"Battery too low to send a message on {self.model}.")

    def charge_phone(self, amount):
        self.battery_percentage += amount
        if self.battery_percentage > 100:
            self.battery_percentage = 100
        print(f"The phone is now charged to {self.battery_percentage}%.")

    def display_info(self):
        # Displays the phone's details
        print(f"Phone Details:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Battery: {self.battery_percentage}%")

# Main function
def main():
    # Create a smartphone object
    my_phone = Phone("Apple", "iPhone 13", 20)

    # Display initial phone information
    my_phone.display_info()

    # Call some behaviors
    my_phone.make_call("Alice")
    my_phone.send_message("Bob", "Hey, how are you?")
    my_phone.charge_phone(50)

    # Display updated phone information
    print("\nAfter using the phone:")
    my_phone.display_info()

if __name__ == "__main__":
    main()
