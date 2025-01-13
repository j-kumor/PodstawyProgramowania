import csv

province_dict = {}
with open('province.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header
    for row in csv_reader:
        letter, name = row
        province_dict[letter] = {'province': name, 'vehicle_count': 0}

#  Read vehicle registration numbers from vehicle.txt and count matching vehicles
with open('vehicle.txt', mode='r', encoding='utf-8') as file:
    for line in file:
        # Get the first letter of the registration number
        registration_number = line.strip()
        if registration_number:  # Skip empty lines
            first_letter = registration_number[0].upper()
            if first_letter in province_dict:
                province_dict[first_letter]['vehicle_count'] += 1

# Print the count of vehicles per province
for province in province_dict.values():
    print(f"Province: {province['province']}, Vehicles: {province['vehicle_count']}")
