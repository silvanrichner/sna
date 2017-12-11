import twitter
import json
import time
import sys


class MultiUserAPI(object):
    def getAPI(self):
        return self.api

    def switchUser(self):
        self.current_token = self.current_token + 1
        if( self.current_token >= len(self.tokens)):
            self.current_token = 0
            time.sleep(15*60)
        self.api = twitter.Api(consumer_key=self.tokens[self.current_token]['consumer_key'],
                               consumer_secret=self.tokens[self.current_token]['consumer_secret'],
                               access_token_key=self.tokens[self.current_token]['access_token_key'],
                               access_token_secret=self.tokens[self.current_token]['access_token_secret'])

    def getUser(self, name):
        try:
            return self.getAPI().GetUser(screen_name = name)
        except:
            #print("Exception: sleeping...")
            #time.sleep(60)
            self.switchUser()
            return self.getUser(name)

    def getFollowers(self, user):
        try:
            return self.getAPI().GetFollowers(user)
        except:
            print(sys.exc_info())
            # print("Exception: sleeping...")
            # time.sleep(60)
            self.switchUser()
            return self.getFollowers(user)

    def getUserTimeline(self, user_id):
        try:
            return self.getAPI().GetUserTimeline(user_id, include_rts=True)
        except:
            print(sys.exc_info()[0])
            # print("Exception: sleeping...")
            # time.sleep(60)
            self.switchUser()
            return self.getTimeline(user_id)

    def getRetweets(self, status_id):
        try:
            return self.getAPI().GetRetweets(status_id)
        except:
            print(sys.exc_info()[0])
            # print("Exception: sleeping...")
            # time.sleep(60)
            self.switchUser()
            return self.getRetweets(status_id)

    def getFollowerIDs(self, retweet_user_id):
        try:
            return self.getAPI().GetFollowerIDs(retweet_user_id)
        except:
            print(sys.exc_info()[0])
            # print("Exception: sleeping...")
            # time.sleep(60)
            self.switchUser()
            return self.getFollowerIDs(retweet_user_id)

    def __init__(self):
        self.tokens = json.load(open('api_tokens.json'))
        self.current_token = 0
        self.switchUser()





