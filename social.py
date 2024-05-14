import tweepy

#current version 2 method
def twitConnection():
    consumer_key = 'koMdF12v0tA4Iz5LnYrBZDgc4'
    consumer_secret = 'g1BRmn3xb4ACVsjYnFz3mMPMReAeQstU51p9WXShCkPX76O40a'
    access_token = '1495398532588744707-G9LmmSefsJZVxQWAq9K2kaPs4UU1UK'
    access_token_secret = 'nhjlqkYhOP2DXSoD4HRODooy649atVRIXmhowsEvwrTOS'

    Bearer_Token="AAAAAAAAAAAAAAAAAAAAAPHvtgEAAAAAHlmVC%2F1Nd4UswbKOmqhbHIo%2BFLA%3DQNqxmi05BwPwiP8zGOKb7MWpBOgyTOx9seYM8eEUUKFwqpkdRe"

    Client_ID="OFlXU24zRnZUVk5FWENyZFJKMmc6MTpjaQ"
    Client_Secret="1g-oqouCjZfV6FP_VvkxzVn_7FGH6T5vUVyxeYprW2I2ABX61B"


    
    client = tweepy.Client(
        consumer_key = consumer_key, consumer_secret=consumer_secret,
        access_token=access_token, access_token_secret=access_token_secret)
     
    return client


def twitter_posting(text,id): 
    text=text+f"""

    https://www.spreadit.es/?p={str(id)}

    """
    client = twitConnection()
    response = client.create_tweet(text = text)
    print(response)

"""
import requests

# Define your authentication keys
client_id = "78bxweotlfjro5"
client_secret = "zp1zF9a6E7xTnbXM"
access_token = "AQV2kvmzqRXFKViwoNNYTESsQvnVQDzlkXldF49Id0rrNW0bclNW-zJBtKJAODv301mnTvn6bKntv4faRNhdt0AKn10LitM2LheBQ0NNlBNhESKp_jsblZRh9TWbvDR2tAiKwkGeyvjH007pxGZyf3YSybOBJTtwx3XdFMwincdCrw_a__STCYQznaEOM7KDmISuWwnwHZJBPEs6OTaoYCwq9w-fcTkKt52FbaBxp9pA6gz66jxslTEp_tdSnoo_OL2LK7O4Isc2n29HjUBXRjZP9yfuvp6d3MPw3tE0HKKZt3nUEG1cigqtt29N9vWsIuyUSmpP5qkvdgVSCaVbnDuVqFd8-w"

# Define the API endpoint
url = "https://api.linkedin.com/rest/posts"

# Define the headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "X-Restli-Protocol-Version": "2.0.0",
    "LinkedIn-Version": "202305",  # Updated LinkedIn version format
    "X-Restli-Protocol-Organization": "urn:li:organization:90700161"  # Organization URN
}

# Define the data for the post
data = {
    "author": "urn:li:organization:90700161",  # Replace with your organization URN
    "commentary": "This is a test post on LinkedIn page.",
    "visibility": "PUBLIC",
    "distribution": {
        "feedDistribution": "MAIN_FEED",
        "targetEntities": [],
        "thirdPartyDistributionChannels": []
    },
    "lifecycleState": "PUBLISHED",
    "isReshareDisabledByAuthor": False
}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Check the response
if response.status_code == 201:
    print("Post created successfully!")
    print("Post ID:", response.headers.get("x-restli-id"))
else:
    print("Failed to create post:", response.status_code, response.text)

"""
