
import tweepy
import csv

def run_etl():
    # Twitter API credentials
    consumer_key = ' '
    consumer_secret = ' '
    access_token = ' '
    access_token_secret = ' '

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Create API object
    api = tweepy.API(auth)

    # Retrieve the last 10 tweets from the user's timeline
    tweets = api.user_timeline(screen_name='gate_io', count=10, tweet_mode='extended')

    # Prepare CSV file
    csv_file_path = "s3://airflow/tweets.csv"  # Replace with your desired file path
    csv_file = open(csv_file_path, "w", encoding="utf-8", newline="")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Tweet"])

    # Save non-repetitive tweets with keywords to CSV
    saved_tweets = set()
    for tweet in tweets:
        tweet_text = tweet.full_text.lower()
        if ("margin" in tweet_text or "borrowable" in tweet_text) and tweet_text not in saved_tweets:
            csv_writer.writerow([tweet.full_text])
            saved_tweets.add(tweet_text)

    # Close the CSV file
    csv_file.close()

 
