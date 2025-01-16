class SocialMediaProfile:
    def __init__(self, username):
        # Initialize the user's profile with a username and an empty list of posts
        self.username = username
        self.posts = []

    def add_post(self, content):
        # Add a post to the user's list of posts
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        # Display the user's timeline with their name and numbered posts
        print(f"Timeline for {self.username}:")
        if not self.posts:
            print("No posts yet.")
        else:
            for index, post in enumerate(self.posts, start=1):
                print(f"{index}. {post}")

def main():
    # Create a social media profile for 'johndoe'
    user = SocialMediaProfile(username="johndoe")

    # Add posts to the user's timeline
    user.add_post("Hello, world!")
    user.add_post("Had a great day at the park!")
    user.add_post("What's up, Natalie? How are you?")

    # Display the user's timeline
    print("\nUser Timeline:")
    user.display_timeline()

if __name__ == "__main__":
    main()
