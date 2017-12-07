import json
from MultiUserAPI import MultiUserAPI

#MultiUserAPI test
mua = MultiUserAPI()

json_object = json.load(open('politicians.json'))

parteifollowercount = 0;
politikerfollowercount = 0;
retweetfollowercount = 0;
politicians_count = 0;

partei = dict()
partei_follower = dict()


politician_followers = set()

#Iterate over the politicians
for politician in json_object['politicians']:
    #count the politicians
    politicians_count += 1;

    #count politicians in the different parteien
    #and initiate partei follower dict with politician
    if politician['partei'] in partei:
        partei[politician['partei']] += 1
        partei_follower[politician['partie']] += 1
    else:
        partei[politician['partei']] = 1
        partei_follower[politician['partie']] = 1

    print(politician['twittername'])

    user = mua.getAPI().GetUser(screen_name=politician['twittername'])
    politikerfollowercount += user.followers_count;
    print("politikerfolllowercount: " + str(politikerfollowercount))

    user_timeline = mua.getAPI().GetUserTimeline(user.id, include_rts=True)

    for status in user_timeline:
        retweets = mua.getAPI().GetRetweets(status.id)

        for retweet in retweets:
            retweetfollowercount += mua.getAPI().GetUser(retweet.user.id).followers_count
            print("retweeter followercount: " + str(retweetfollowercount))
            politikerfollowercount += retweetfollowercount

    print("politikerfollowercount und retweeter followercount --> politiker erreicht: " + str(politikerfollowercount) + " Follower")

    #add politician followercount and retweeter followercount to parteifollowers
    partei_follower[politician['partie']] += politikerfollowercount




for key, value in partei.items():
    print(key + " : " + str(value))

for key, value in partei_follower():
    print(key + " erreicht: " + value + " Twitternutzer")

#test connection
#print(api.VerifyCredentials())

#Get follower count of user
#follower_count = api.GetUser(screen_name='_BR_JSA').followers_count

#Get followers (ID) of user
#followers = api.GetFollowerIDs(screen_name='_BR_JSA')
#print(followers)

#rate_limit_status = api.CheckRateLimit()
#print(rate_limit_status)


for x in range(1, 50):
    print(mua.getAPI().VerifyCredentials())
