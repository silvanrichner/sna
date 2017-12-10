import json
from MultiUserAPI import MultiUserAPI

#MultiUserAPI test
mua = MultiUserAPI()

json_object = json.load(open('politicians.json'))

#partei : countPolitician
partei = dict()

#reachlist every followerId only once
politician_followers = set()

#json object
data = {'parteien' : []}

#Iterate over the politicians
for politician in json_object['politicians']:

    #HEEEEELP
    if politician['partei'] not in data['parteien']:
        data['parteien'].append({politician['partei']:{}});

    print(data)

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
            retweetfollowers = mua.getAPI().GetFollowerIDs(retweet.user.id)
            #add retweet follower to reachlist
            for retweetfollowerid in retweetfollowers:
                politician_followers.add(retweetfollowerid)

    json_politician = {'name' : politician['name'], 'twittername' : politician['twittername'], 'reach' : len(politician_followers)}
    print(json_politician)


    #HeEEEElp
    data['parteien'][politician['partei']].append(json_politician)
    politician_followers.clear()

print(data)



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
