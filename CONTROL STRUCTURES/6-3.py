# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house

light_switch1 = False  # False - switch off, True - switch on
light_switch2 = False  # False - switch off, True - switch on
bulbs_on = 0

# Check the state of switch 1
if light_switch1:
    bulbs_on += 1

# Check the state of switch 2
if light_switch2:
    bulbs_on += 2  # Switch 2 turns on two bulbs

print(f"Number of bulbs lit: {bulbs_on}")