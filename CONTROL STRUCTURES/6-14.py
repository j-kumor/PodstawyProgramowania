# Boolean variables indicating whether the person has accounts
facebook = input("Do you have a Facebook account? (True/False): ") ==  'True'
twitter = input("Do you have a Twitter account? (True/False): ") ==  'True'
instagram = input("Do you have an Instagram account? (True/False): ") ==  'True'

# Count how many social networks the person has accounts on
accounts_count = sum([facebook, twitter, instagram])

# Check if the person is a good influencer (has at least two accounts)
if accounts_count >= 2:
    print("You are a good influencer!")
else:
    print("You are not a good influencer.")