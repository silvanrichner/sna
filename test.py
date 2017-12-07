import json
from MultiUserAPI import MultiUserAPI

#MultiUserAPI test
mua = MultiUserAPI()

json_object = json.load(open('politicians.json'))

partei = dict()

politician_followers = set()

data = {}
#Iterate over the politicians
for politician in json_object['politicians']:

    print(politician['twittername'])

    user = mua.getAPI().GetUser(screen_name=politician['twittername'])
    followers = mua.getAPI().GetFollowers(user)
    #add direct follower to reachlist
    for follower in followers:
        politician_followers.add(follower.id)

    user_timeline = mua.getAPI().GetUserTimeline(user.id, include_rts=True)

    for status in user_timeline:
        retweets = mua.getAPI().GetRetweets(status.id)

        for retweet in retweets:
            retweetfollowers = mua.getAPI().GetFollowers(retweet.user.id)
            #add retweet follower to reachlist
            for retweetfollower in retweetfollowers:
                politician_followers.add(retweetfollower.id)



    #data["partei"] = politician['partei']
    #data["politiker"]["name"] = politician['name']
    #data["politiker"]["twittername"] = politician['twittername']
    #data['politiker']['reach'] = politician_followers.length


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


#for x in range(1, 50):
#    print(mua.getAPI().VerifyCredentials())
