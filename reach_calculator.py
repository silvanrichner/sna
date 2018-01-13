import csv
from collections import defaultdict

#load csv
with open('edges.csv', 'r', newline='') as edgecsv, open('nodes.csv', 'r', newline='') as nodecsv:
    edgereader = csv.reader(edgecsv, delimiter=',')
    nodereader = csv.reader(nodecsv, delimiter=',')

    indegreemap = dict()

    retweetedges = []

    #skip header
    next(edgereader)

    for row in edgereader:
        if((float(row[2]) < 1)):
            target_id = row[0]

            indegreemap[target_id] = indegreemap.get(target_id, 0) + 1
        else:
            retweetedges.append(row)

    # load politicians
    politicians = dict()
    next(nodereader)
    for row in nodereader:
        if (row[4] == 'P'):
            politicians[row[0]] = {'reach':indegreemap.get(row[0], 0), 'name':row[2], 'party':row[3]}
        else:
            break

    for row in retweetedges:
        politicians[row[0]]['reach'] = politicians[row[0]]['reach'] + int(row[2]) * indegreemap.get(row[1], 0)


    reach_writer = csv.writer(open('politician_reach.csv', 'w', newline=''), delimiter=",")
    reach_writer.writerow(["Name", "Reach", "Partei"])
    for pol in politicians.values():
        reach_writer.writerow([pol['name'], pol['reach'], pol['party']])




