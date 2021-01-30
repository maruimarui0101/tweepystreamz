import tweepy
import os 
from dotenv import load_dotenv
import socket 
import json

load_dotenv()

HOST = socket.gethostbyname('d799daa0e411.ngrok.io')
PORT = 14734

class ClientSocket():
    @staticmethod
    def create():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((HOST, PORT))
        return s

class TwitterAuth():

    @staticmethod
    def authenticate():
        auth = tweepy.OAuthHandler(f"{os.getenv('CONSUMER_KEY')}", f"{os.getenv('CONSUMER_SECRET')}")
        auth.set_access_token(f"{os.getenv('ACCESS_TOKEN')}", f"{os.getenv('ACCESS_TOKEN_SECRET')}")
        return auth

class MyStreamListener(tweepy.StreamListener):
    
    def on_data(self, data):
        try: 
            msg = json.loads(data)['text'].encode('utf-8')
            print(msg)
            client.send(msg)
            return True
        except BaseException as e:
            print('ERROR ' + str(e))
            return True

    def on_error(self, status):
        print(status)
        return True


if __name__ == '__main__':
    client = ClientSocket.create()
    MyStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=TwitterAuth.authenticate()
    , listener=MyStreamListener)
    myStream.filter(track=['$GME'])
