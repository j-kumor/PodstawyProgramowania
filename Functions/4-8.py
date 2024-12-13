###
# A program that returns the given number of hours and the number of minutes,
# returns a string specifying the time in the given format
# '24' for 24-hour time and '12' for 12-hour format
#


def time_string(hours, minutes, time_format):
    time_str = ''
    if time_format == '24':
        if hours < 10:
            time_str += '0' + str(hours)
        else:
            time_str += str(hours)
        time_str += ':'
        if minutes < 10:
            time_str += '0' + str(minutes)
        else:
            time_str += str(minutes)
    elif time_format == '12':
        if 12 < hours <= 24:
            time_str += str(hours - 12)
        elif hours == 0:
            time_str += '12'
        else:
            time_str += str(hours)

        time_str += ':'
        if minutes < 10:
            time_str += '0' + str(minutes)
        else:
            time_str += str(minutes)

        if hours >= 12:
            time_str += 'PM'
        else:
            time_str += 'AM'
    else:
        return 'Wrong format'
    return time_str


print(f'{time_string(15, 38, "24")}')
print(f'{time_string(8, 3, "24")}')
print(f'{time_string(0, 5, "24")}')
print(f'{time_string(11, 15, "12")}')
print(f'{time_string(0, 7, "12")}')
print(f'{time_string(7, 30, "12")}')
print(f'{time_string(12, 46, "12")}')
print(f'{time_string(13, 10, "12")}')
#  print(f'{time_string(19, 02, "12")}')


"""
        elif 12 < hours <= 23:
            time_str = str(hours - 12) + ':' + str(minutes) + 'PM'
        elif 12 < hours <= 23 and minutes < 10:
            time_str = str(hours - 12) + ':' + '0' + str(minutes) + 'PM'
        elif hours == 12 and minutes == 0:
            time_str = str(hours) + ':' + '0' + str(minutes) + 'PM'
        elif hours < 12 and minutes < 10:
            time_str = str(hours) + ':' + '0' + str(minutes) + 'AM'
        elif hours == 0:

        elif hours < 12:
            time_str = str(hours) + ':' + str(minutes) + 'AM'
"""