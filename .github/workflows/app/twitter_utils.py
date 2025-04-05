import tweepy
import os

# ✅ Load your Twitter Bearer Token securely from environment variable
bearer_token = os.getenv("AAAAAAAAAAAAAAAAAAAAAIg%2FxwEAAAAAAZDQLpPPExkKCHwrR43E1mm44F4%3Db1e77vSwuwHUq6D8mPVJx5HHLfhdtIp4pvGm4odGTwlm6FE84N")

client = tweepy.Client(bearer_token=bearer_token)

def analyze_twitter_profile(handle):
    try:
        user = client.get_user(username=handle)
        user_id = user.data.id
        tweets = client.get_users_tweets(id=user_id, max_results=5)
        return [tweet.text for tweet in tweets.data] if tweets.data else ["No recent tweets"]
    except Exception as e:
        return [str(e)]

