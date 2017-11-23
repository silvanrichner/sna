import twitter
import json


#Load api tokens and keys from json file
tokens = json.load(open('api_tokens.json'))
print(tokens['consumer_secret'])

#initialize the API for the application: sna_Richner_Sutter_Terribilini and the user: silvanrichner
api = twitter.Api(consumer_key=tokens['consumer_key'],
                  consumer_secret=tokens['consumer_secret'],
                  access_token_key=tokens['access_token_key'],
                  access_token_secret=tokens['access_token_secret'])
print(api.VerifyCredentials())


#Get follower count of user
#follower_count = api.GetUser(screen_name='_BR_JSA').followers_count

#Get followers (ID) of user
#followers = api.GetFollowerIDs(screen_name='_BR_JSA')

#print(followers)

