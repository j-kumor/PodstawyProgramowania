# tv_show.py file
import tv

def main():
    # Create a TV set
    my_tv = tv.TV()

    # Set the list of available channels (7 TV stations)
    available_channels = [
        "TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "National Geographic"
    ]
    my_tv.set_channels(available_channels)

    # Turn the TV on and show the status with the channel number and volume level
    my_tv.turn_on()
    my_tv.show_status()

    # Increase volume by 2 and show status
    my_tv.increase_volume()
    my_tv.increase_volume()
    my_tv.show_status()

    # Decrease volume by 1 and show status
    my_tv.decrease_volume()
    my_tv.show_status()

    # Set the TV channel to 4 (TVN) and show the status
    my_tv.set_channel(4)
    my_tv.show_status()

    # Try increasing the volume to the maximum (volume 10)
    for _ in range(9):  # Increase volume 9 more times to reach 10
        my_tv.increase_volume()

    # Try to increase the volume beyond 10
    my_tv.increase_volume()
    my_tv.show_status()

    # Decrease the volume to 0 and show status
    for _ in range(10):  # Decrease volume 10 times to reach 0
        my_tv.decrease_volume()

    # Try to decrease the volume below 0
    my_tv.decrease_volume()
    my_tv.show_status()

    # Turn the TV off and show the status
    my_tv.turn_off()
    my_tv.show_status()

if __name__ == "__main__":
    main()
