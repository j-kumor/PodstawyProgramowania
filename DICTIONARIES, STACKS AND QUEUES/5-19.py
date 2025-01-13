import json

# Load the reservations data from the JSON file
def load_reservations():
    with open('reservations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['reservations']

# Function to get the number of rooms (unique room numbers)
def get_number_of_rooms(reservations):
    rooms = set()
    for reservation in reservations:
        rooms.add(reservation['room_number'])
    return len(rooms)

# Function to count the number of paid and unpaid reservations
def count_paid_unpaid_reservations(reservations):
    paid_count = 0
    unpaid_count = 0
    for reservation in reservations:
        if reservation['paid']:
            paid_count += 1
        else:
            unpaid_count += 1
    return paid_count, unpaid_count

# Function to calculate the total value of paid reservations
def total_paid_value(reservations):
    total_paid = 0.0
    for reservation in reservations:
        if reservation['paid']:
            total_paid += reservation['price_per_night'] * reservation['nights']
    return total_paid

# Function to calculate the total value of unpaid reservations
def total_unpaid_value(reservations):
    total_unpaid = 0.0
    for reservation in reservations:
        if not reservation['paid']:
            total_unpaid += reservation['price_per_night'] * reservation['nights']
    return total_unpaid

# Main function to display the summary information
def print_summary(reservations):
    number_of_rooms = get_number_of_rooms(reservations)
    paid_count, unpaid_count = count_paid_unpaid_reservations(reservations)
    total_paid = total_paid_value(reservations)
    total_unpaid = total_unpaid_value(reservations)

    print("Number of rooms:", number_of_rooms)
    print("Number of paid reservations:", paid_count)
    print("Number of unpaid reservations:", unpaid_count)
    print("Total value of paid reservations: {:.2f}".format(total_paid))
    print("Total value of unpaid reservations: {:.2f}".format(total_unpaid))

reservations = load_reservations()
print_summary(reservations)
