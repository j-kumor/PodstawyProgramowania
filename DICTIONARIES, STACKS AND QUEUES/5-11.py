import json
import os

# File path for voting data
file_path = 'voting.json'

# Read the existing voting data (if the file exists)
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        voting_data = json.load(file)
else:
    voting_data = {}

person_name = input('Name of the person you are voting for: ')

# Update the vote count for the given person
if person_name in voting_data:
    voting_data[person_name] += 1
else:
    voting_data[person_name] = 1

#  Save the updated voting data back to the json file
with open(file_path, 'w') as file:
    json.dump(voting_data, file, indent=4)


print(f"Updated voting results: {voting_data}")
