import queue

# create a visited_websites stack
visited_websites = queue.LifoQueue()

# some previously visited websites
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    website = input('Enter website name (0 for back): ')

    if website == '0':
        # If stack is not empty, go back to the previous website
        if visited_websites.empty():
            print("No more websites in history.")
            break
        else:
            print('<-- Going back to a previously visited website')
            website = visited_websites.get()  # Pop the last visited website from the stack
    elif website != "":  # If it's not an empty string
        # Add the new website to the stack
        visited_websites.put(website)

    # Print the name of the website you are currently viewing
    print('You are currently viewing:', website)
    print()
