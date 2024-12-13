###
# Function that returns True at least 3 people were in the room at the same time
# The + sign means a person entering a room and the - sign a person leaving a room
#

def f(detector):
    people_in_room = 0
    for i in detector:
        if people_in_room >= 3:
            return True
        else:
            if i == '+':
                people_in_room += 1
            else:
                people_in_room -= 1
    return False


print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))