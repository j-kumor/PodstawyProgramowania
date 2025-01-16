# tv.py file
class TV:
    def __init__(self):
        # Initially, the TV is turned off and set to channel 1, volume is set to 0
        self.is_on = False
        self.channel_no = 1
        self.channels = []  # List of available TV channels
        self.volume = 0  # Initial volume level is 0

    def turn_on(self):
        # Turn the TV on
        self.is_on = True

    def turn_off(self):
        # Turn the TV off
        self.is_on = False

    def set_channel(self, new_channel_no):
        # Set the TV channel number
        if self.is_on and new_channel_no <= len(self.channels) and new_channel_no > 0:
            self.channel_no = new_channel_no
            print(f"Channel changed to {self.channels[self.channel_no - 1]}")
        else:
            print("Cannot change channel. Either the TV is off or the channel number is invalid.")

    def set_channels(self, channels_list):
        # Set the list of available channels
        self.channels = channels_list
        print("Channel list has been updated.")

    def show_channels(self):
        # Show the list of available channels
        if self.channels:
            print("Channel list:")
            for index, channel in enumerate(self.channels, 1):
                print(f"{index}. {channel}")
        else:
            print("No channels available.")

    def increase_volume(self):
        # Increase the volume by 1 (up to 10)
        if self.volume < 10:
            self.volume += 1
            print(f"Volume increased to {self.volume}")
        else:
            print("Volume is already at the maximum level (10).")

    def decrease_volume(self):
        # Decrease the volume by 1 (down to 0)
        if self.volume > 0:
            self.volume -= 1
            print(f"Volume decreased to {self.volume}")
        else:
            print("Volume is already at the minimum level (0).")

    def show_status(self):
        # Show the current status of the TV with the channel number and volume level if it's on
        if self.is_on:
            if 0 < self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), Volume {self.volume}")
            else:
                print(f"TV is on, but the selected channel number {self.channel_no} is invalid. Volume {self.volume}")
        else:
            print(f"TV is off, Volume {self.volume}")
