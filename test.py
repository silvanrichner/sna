import json
from MultiUserAPI import MultiUserAPI

#MultiUserAPI test
mua = MultiUserAPI()

json_object = json.load(open("politicians.json"))

#partei : countPolitician
partei = dict()

#reachlist every followerId only once
politician_followers = set()

#json object
data = {"parteien" : {}}

#Iterate over the politicians
for politician in json_object["politicians"]:

    #HEEEEELP
    if politician["partei"] not in data["parteien"]:
        data["parteien"].update({politician["partei"]:{}})

    print(politician["twittername"])
    user = mua.getAPI().GetUser(screen_name=politician["twittername"])
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

    json_politician = {"name" : politician["name"], "twittername" : politician["twittername"], "reach" : len(politician_followers)}

    data["parteien"][politician["partei"]].update(json_politician)
    politician_followers.clear()

print(data)

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)