# Survey questions
interested_in_computer_science = input("Are you interested in computer science? (y/n): ").strip().lower() == 'y'
likes_computer_games = input("Do you like playing computer games? (y/n): ").strip().lower() == 'y'
has_instagram_account = input("Do you have an Instagram account? (y/n): ").strip().lower() == 'y'

# Printing survey results
print("\nSURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if interested_in_computer_science else 'No'}")
print(f"Playing computer games: {'Yes' if likes_computer_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram_account else 'No'}")