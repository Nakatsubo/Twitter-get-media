from dotenv import load_dotenv
import os
from requests_oauthlib import OAuth1Session

load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# 以下の関数をimportして使用する
def CreateOAuthSession():
    return OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)