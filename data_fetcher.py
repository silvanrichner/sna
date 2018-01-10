import json
import sortedcontainers
import csv

from MultiUserAPI import MultiUserAPI

#MultiUserAPI test
mua = MultiUserAPI()

json_object = json.load(open("politicians.json"))

followers_retweets = dict();
all_nodes = sortedcontainers.SortedList()

with open('edges.csv', 'w', newline='') as edgecsv, open('nodes.csv', 'w', newline='') as nodecsv:
    edgewriter = csv.writer(edgecsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    nodewriter = csv.writer(nodecsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

    #initially iterate once over the politicians to write them into the nodes.csv
    for politician in json_object["politicians"]:
        user = mua.getUser(politician["twittername"])

        #write politician node
        nodewriter.writerow([user.id, politician["twittername"], politician["name"], politician["partei"], "P"])
        all_nodes.add(user.id)

    #Iterate over the politicians
    for politician in json_object["politicians"]:

        print(politician["twittername"])

        user = mua.getUser(politician["twittername"])

        print("Get Followers from Politician")
        followers = mua.getFollowerIDs(user.id)
        #add direct follower to reachlist
        for follower in followers:
            #write follower nodes
            if follower not in all_nodes:
                nodewriter.writerow([follower, "", "", "N/A", "F"])
                all_nodes.add(follower)

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
                        #write followerfollower node
                        if retweetfollowerid not in all_nodes:
                            nodewriter.writerow([retweetfollowerid, "", "", "N/A", "FF"])
                            all_nodes.add(retweetfollowerid)

                        #write followerfollower edge
                        edgewriter.writerow([retweet.user.id, retweetfollowerid, 0])

        for followerid in followers_retweets:
            #write follower edge
            edgewriter.writerow([user.id, followerid, followers_retweets[followerid]])

        followers_retweets.clear()

