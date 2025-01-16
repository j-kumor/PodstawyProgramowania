# main.py
from thermometer import Thermometer

def main():
    # Create a thermometer object
    my_thermometer = Thermometer()

    # Turn the thermometer on
    my_thermometer.turn_on()

    # Measure the temperature
    my_thermometer.measure_temperature()

    # Display the measured temperature
    my_thermometer.display_temperature()

    # Turn the thermometer off
    my_thermometer.turn_off()

if __name__ == "__main__":
    main()
