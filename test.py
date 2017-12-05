import twitter
import json


#Load api tokens and keys from json file
tokens = json.load(open('api_tokens.json'))
#print(tokens['consumer_secret'])

#initialize the API for the application: sna_Richner_Sutter_Terribilini and the user: silvanrichner
#api = twitter.Api(consumer_key=tokens['consumer_key'],
#                  consumer_secret=tokens['consumer_secret'],
#                  access_token_key=tokens['access_token_key'],
#                  access_token_secret=tokens['access_token_secret'])
#print(api.VerifyCredentials())

json_object = json.load(open('politicians.json'))

parteifollowercount = 0;
politikerfollowercount = 0;
retweetfollowercount = 0;
politicians_count = 0;

partei = dict()
for politician in json_object['politicians']:
    politicians_count += 1;

    if politician['partei'] in d:
        partei[politician['partei']] += 1
    else:
        partei[politician['partei']] = 1



for key, value in partei.items():
    print(key + " : " + str(value))

    #politikerfollowercount += wrapper.getFollowercount()


    #retweets = api.GetRetweets()
    #print(politician['name'])
    #twittername = politician['twittername']
    #print(api.GetFollowers(screen_name=twittername))



#Get follower count of user
#follower_count = api.GetUser(screen_name='_BR_JSA').followers_count
#print(follower_count)
#Get followers (ID) of user
#followers = api.GetFollowerIDs(screen_name='_BR_JSA')
#print(followers)

#print(followers)

