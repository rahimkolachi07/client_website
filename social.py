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