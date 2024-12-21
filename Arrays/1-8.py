computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Sort the list alphabetically
computer_games.sort()

# Initialize a counter for numbering
index = 1

# Use a while loop to print the sorted games with numbers
while index <= len(computer_games):
    print(f"{index}. {computer_games[index - 1]}")
    index += 1
