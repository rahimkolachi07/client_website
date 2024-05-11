import tweepy

consumer_key = 'xk8MG1mKx9avwBeOokKiZJoVM'
consumer_secret = '6wagl0scIIExjG1tT1r2HFPEXCmzKQNvFCR37aRKLFJiTBTOdI'
access_token = '1495398532588744707-cCaj2L1GPgEAE9kx17Gar6eH0QaF3w'
access_token_secret = 'ahpxvyDoPUaYCGaIFmwXuw6uLPe5kP4AngGCxeqMlvqxi'

Bearer_Token="AAAAAAAAAAAAAAAAAAAAAPHvtgEAAAAA%2FiQhqwR1S7bkjXBXxrBOEzmkafQ%3D5rgiC1IGgiTvd87MwRfmyF4gfbHKSAPlj7F17IIQ4yJzTmoaCF"

Client_ID="OFlXU24zRnZUVk5FWENyZFJKMmc6MTpjaQ"
Client_Secret="M6Dys_PK2a6oQj2gZkwlyACwlySSKkJuMExxbOnUxONkIYymPY"

import requests
import json
import ssl

def post_tweet(bearer_token, tweet_content):
    # Headers
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    # API endpoint
    url = "https://api.twitter.com/2/tweets"

    # Tweet data
    tweet_data = {
        "text": tweet_content
    }

    # Suppress SSL warning
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

    try:
        # Post tweet
        response = requests.post(url, headers=headers, json=tweet_data, verify=True, timeout=30)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 201:
            print("Tweet posted successfully!")
        else:
            print("Failed to post tweet. Error:", response.text)
    except requests.exceptions.HTTPError as e:
        print("HTTP error occurred:", e)
    except requests.exceptions.ConnectionError as e:
        print("Error connecting to the server:", e)
    except requests.exceptions.Timeout as e:
        print("Timeout error:", e)
    except requests.exceptions.RequestException as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    # Replace with your actual Bearer Token and tweet content
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAPHvtgEAAAAA%2FiQhqwR1S7bkjXBXxrBOEzmkafQ%3D5rgiC1IGgiTvd87MwRfmyF4gfbHKSAPlj7F17IIQ4yJzTmoaCF"
    tweet_content = "Hello, this is a test tweet from my Python script!"

    post_tweet(bearer_token, tweet_content)
