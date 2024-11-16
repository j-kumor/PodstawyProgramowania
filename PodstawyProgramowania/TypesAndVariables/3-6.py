# zadanie 3.6
#The distance to the horizon depends on the height of the observer above the ground. The higher you are, the farther away the horizon is. For most situations, you can use the following formula:

#d = 3.57 × √h

#Where:

#d is the distance to the horizon in kilometers
#h is the height of the observer in meters
#Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:

#You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
#You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.
#In the year 2022, the world population was approximately 8 billion. The Northern Hemisphere has 7.2 billion people. Write a program that calculates and prints:

#The number of people and percentage of the total population living in the Northern Hemisphere
#The number of people and percentage of the total population living in the Southern Hemisphere
#
import math

h = int(input('Podaj swoja wysokosc: '))
d = 3.57 * math.sqrt(h)

print('Dystans do horyzontu z podanej wysokosci wynosi: ', d,'km')

