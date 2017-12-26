import json
import copy

from MultiUserAPI import MultiUserAPI

#MultiUserAPI test
mua = MultiUserAPI()

json_object = json.load(open("politicians.json"))

followers_retweets = dict();

#json object
data = {"parteien" : {}}


try:
    #Iterate over the politicians
    for politician in json_object["politicians"]:

        if politician["partei"] not in data["parteien"]:
            data["parteien"].update({politician["partei"]:{}})

        print(politician["twittername"])

        user = mua.getUser(politician["twittername"])
        print("Get Followers from Politician")
        followers = mua.getFollowerIDs(user)
        #add direct follower to reachlist
        for follower in followers:
            followers_retweets[follower] = 0

        print("get user timeline from politician")
        user_timeline = mua.getUserTimeline(user.id)

        for status in user_timeline:
            print("get retweets from tweet: " + str(status.id))
            retweets = mua.getRetweets(status.id)

            for retweet in retweets:
                if(retweet.user.id not in followers_retweets):
                    followers_retweets[retweet.user.id] = 0

                followers_retweets[retweet.user.id] += 1

                print("get followerid from follower retweet: " + str(retweet.user.id))
                retweetfollowers = mua.getFollowerIDs(retweet.user.id)
                #add retweet follower to reachlist
                for retweetfollowerid in retweetfollowers:
                    if(retweetfollowerid not in followers_retweets):
                        followers_retweets[retweetfollowerid] = 0

        json_politician = {politician["name"]: { "twittername" : politician["twittername"], "reach" : copy.deepcopy(followers_retweets)}}

        data["parteien"][politician["partei"]].update(json_politician)
        print(data)
        followers_retweets.clear()
finally:
    print(data)

    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)