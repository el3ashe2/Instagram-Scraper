import instaloader

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Login to Instagram (Optional, for private profiles)
USERNAME = "your_username"
PASSWORD = "your_password"
L.login(USERNAME, PASSWORD)

# Function to scrape an Instagram profile
def scrape_profile(profile_name):
    profile = instaloader.Profile.from_username(L.context, profile_name)
    print(f"Username: {profile.username}")
    print(f"Full Name: {profile.full_name}")
    print(f"Bio: {profile.biography}")
    print(f"Number of posts: {profile.mediacount}")
    print(f"Number of followers: {profile.followers}")
    print(f"Number of following: {profile.followees}")
    
    posts = profile.get_posts()
    for index, post in enumerate(posts, 1):
        print(f"\nPost {index}:")
        print(f"Post Date: {post.date_utc}")
        print(f"Caption: {post.caption}")
        print(f"Likes: {post.likes}")
        print(f"Comments: {post.comments}")
        L.download_post(post, target=profile_name)  # Downloads the post

# Specify the Instagram profile you want to scrape
scrape_profile('instagram_profile_name')
