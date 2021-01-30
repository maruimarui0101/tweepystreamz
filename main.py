import tweepy
import os 
from dotenv import load_dotenv
import socket 

load_dotenv()

host = socket.gethostname() 
port = 12345                   

class ClientSocket():
    @staticmethod
    def create():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        s.connect((host, port))
        return s

client = ClientSocket.create()

class TwitterAuth():

    @staticmethod
    def authenticate():
        auth = tweepy.OAuthHandler(f"{os.getenv('CONSUMER_KEY')}", f"{os.getenv('CONSUMER_SECRET')}")
        auth.set_access_token(f"{os.getenv('ACCESS_TOKEN')}", f"{os.getenv('ACCESS_TOKEN_SECRET')}")
        return auth

class MyStreamListener(tweepy.StreamListener):
    
    def on_status(self, status):
        client.sendall(status.text.encode())

MyStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=TwitterAuth.authenticate()
, listener=MyStreamListener)

myStream.filter(track=['$GME'])
