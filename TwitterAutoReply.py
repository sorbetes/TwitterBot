#!/usr/bin/env python
import os
import tweepy
from secrets2 import *
from time import gmtime, strftime
from tweepy import Stream
from tweepy import StreamListener

# ====== Individual bot configuration ==========================
bot_username = 'username'
logfile_name = bot_username + ".log"
# ==============================================================
auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
    
    def on_status(self, status):
        if 'RT' not in status.text:
            # Prints the text of the tweet
            print('Tweet text: ' + status.text)
            s = status.author.screen_name
            print(s)
            try:
                message = 'Message'
                filename = 'image.png'.format(b)
                api.update_with_media(filename, status=message, in_reply_to_status_id=status.id)
            except:
                try:
                    print('error')
                except:
                    print('double error')
        return True
    
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
    
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening

if __name__ == '__main__':
    listener = StdOutListener()
    stream = Stream(auth, listener)
    myStream.filter(follow=['user id'])

#https://dev.twitter.com/streaming/overview/request-parameters
