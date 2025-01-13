basic_data = {
   "name": "Barbara",
   "age": 21
}

advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Create the 'person' dictionary by merging basic_data and advanced_data
person = basic_data.copy()  # Start with a copy of basic_data
person.update(advanced_data)  # Add data from advanced_data

print(person)
