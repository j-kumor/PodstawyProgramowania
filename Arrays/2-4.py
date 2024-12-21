# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
               "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   meals = meal_plan[day_number - 1]  # Select meals for the specific day
   return ", ".join(meals)  # Join the meals with a comma and space

# Prints weekly meal plan
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

for i in range(1, 8):  # Loop through days 1 to 7
   day_name = weekday(i)  # Get the name of the day
   meal_plan_for_day = day_meal_plan(meal_plan, i)  # Get the meal plan for that day
   print(f"{day_name}: {meal_plan_for_day}")  # Print the day and meal plan
