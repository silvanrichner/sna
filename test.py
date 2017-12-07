import twitter
import json
from MultiUserAPI import MultiUserAPI


#Load api tokens and keys from json file
tokens = json.load(open('api_tokens.json'))
print(tokens['consumer_secret'])

#initialize the API for the application: sna_Richner_Sutter_Terribilini and the user: silvanrichner
api = twitter.Api(consumer_key=tokens['consumer_key'],
                  consumer_secret=tokens['consumer_secret'],
                  access_token_key=tokens['access_token_key'],
                  access_token_secret=tokens['access_token_secret'])
print(api.VerifyCredentials())


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



#test connection
#print(api.VerifyCredentials())

#Get follower count of user
#follower_count = api.GetUser(screen_name='_BR_JSA').followers_count

#Get followers (ID) of user
#followers = api.GetFollowerIDs(screen_name='_BR_JSA')
#print(followers)

#rate_limit_status = api.CheckRateLimit()
#print(rate_limit_status)

#MultiUserAPI test
mua = MultiUserAPI()
for x in range(1, 50):
    print(mua.getAPI().VerifyCredentials())
