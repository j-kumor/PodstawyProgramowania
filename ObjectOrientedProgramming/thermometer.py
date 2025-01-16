# thermometer.py
import random

class Thermometer:
    def __init__(self):
        self.is_on = False  # Thermometer is initially off
        self.temperature = 0.0  # Initial temperature (undefined)

    def turn_on(self):
        """Turn the thermometer on."""
        self.is_on = True

    def turn_off(self):
        """Turn the thermometer off."""
        self.is_on = False

    def measure_temperature(self):
        """Generate a random temperature between 34.0 and 42.0 degrees Celsius."""
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)  # Random temperature with 0.1 accuracy
        else:
            print("Please turn on the thermometer first.")
            self.temperature = None

    def display_temperature(self):
        """Display the current temperature and a message if applicable."""
        if self.temperature is not None:
            print(f"Temperature: {self.temperature}C", end=" ")
            if self.temperature >= 37.0:
                print("(fever)", end=" ")
            if self.temperature >= 41.0:
                print("CRITICAL TEMPERATURE!!", end=" ")
            print()  # Newline after the message
        else:
            print("Temperature not measured. Please turn on the thermometer and measure.")
