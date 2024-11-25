# Import necessary libraries
# You need to install the `tweepy` library before running this code. Use `pip install tweepy`.
# Also, ensure you have created a Twitter Developer account and obtained API keys and tokens.
import tweepy
import time

# Twitter API credentials (replace with your own keys and tokens)
consumer_key = ''  # Enter your Consumer Key here
consumer_secret = ''  # Enter your Consumer Secret here
access_token = ''  # Enter your Access Token here
access_token_secret = ''  # Enter your Access Token Secret here

# Authenticate with the Twitter API using OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  # Set up OAuth handler
auth.set_access_token(access_token, access_token_secret)  # Set access token and secret
api = tweepy.API(auth)  # Create an API object to interact with Twitter

# Fetch and print details of the authenticated user
user = api.me()  # Get the authenticated user's details
print(user.name)  # Print the user's name
print(user.screen_name)  # Print the user's screen name (Twitter handle)
print(user.followers_count)  # Print the number of followers

# Define a search term and the number of tweets to interact with
search = "zerotomastery"  # Keyword to search for in tweets
numberOfTweets = 2  # Number of tweets to interact with

# Function to handle rate limits when using Tweepy cursors
def limit_handle(cursor):
    """A generator function to handle rate limits by pausing execution."""
    while True:
        try:
            yield cursor.next()  # Yield the next item from the cursor
        except tweepy.RateLimitError:  # Handle rate limit errors
            time.sleep(1000)  # Wait for a while before retrying

# Follow back specific users (be nice to your followers!)
for follower in limit_handle(tweepy.Cursor(api.followers).items()):  # Iterate through followers
    if follower.name == 'Usernamehere':  # Replace 'Usernamehere' with a specific username you want to follow back
        print(f"Found follower: {follower.name}")  # Print the follower's name
        follower.follow()  # Follow the user

# Like or retweet tweets containing a specific keyword (be a narcissist or engage with content!)
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):  # Search for tweets containing the keyword
    try:
        tweet.favorite()  # Like (favorite) the tweet
        print('Liked the tweet')  # Confirm action in console
    except tweepy.TweepError as e:  # Handle Tweepy-specific errors
        print(f"Error: {e.reason}")  # Print error message if something goes wrong
    except StopIteration:  # Break loop if no more tweets are available
        break