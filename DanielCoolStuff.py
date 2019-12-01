import networkx as nx
import matplotlib.pyplot as plt
import csv
import operator

roadPoints = [0,1,2,4,7,10,15]

G = nx.Graph()

file = open("Network.txt", "rb")
G = nx.read_weighted_edgelist(file)
file.close()



# prim algorithm
def stats(G):
    cityCount = 0
    print(len(G.nodes))
    print(len(G.edges))
    edgeLengths = [0,0,0,0,0,0,0]
    for edge in G.edges:
        length = G.get_edge_data(edge[0], edge[1])['weight']
        edgeLengths[int(length)] += 1
    print(edgeLengths)


def prim(G, startCity):
    # initialize the MST and the set X
    MST = list()
    cnctCities = list()
    count = 45;
    numCities = 1
    # select an arbitrary vertex to begin with
    cnctCities.append(startCity) #start with Boston
    #while len(X) != G.vertices:
    first = True
    while count > 0:
        #crossing = set()
        crossing = list()
        # for each element x in X, add the edge (x, k) to crossing if
        # k is not in X
        #for city in cnctCities:
        length = 0;
        for e in G.edges:#each adj city
            #if adjn not in cnctCities and G.get_edge_data(city, adjn)['weight'] != 0:
            if (bool(e[0] not in cnctCities) ^ bool(e[1] not in cnctCities)) and G.get_edge_data(e[0], e[1])['weight'] != 0:
                #cost = network.get_edge_data(currNode, adjNode)['weight']  # get the cost of traveling to this node
                #crossing.append(G[city][adjn]) #add the Edge
                crossing.append(e)
                #print("just added " + e[0]+ ", " + e[1])
        # find the edge with the smallest weight in crossing
        first = False
        #shortEdge = sorted(crossing, key=lambda edge: G.get_edge_data(edge[0], edge[1])['weight'])[0]
        sortedEdges = sorted(crossing, key=lambda edge: G.get_edge_data(edge[0], edge[1])['weight'])
        pos = 0
        shortEdge = sortedEdges[pos]
        #print(shortEdge)
        length = int(G.get_edge_data(shortEdge[0], shortEdge[1])['weight'])
        while length > count:
            pos += 1
            if pos >= len(sortedEdges):
                print(startCity + ", " + str(numCities))
                return MST
            shortEdge = sortedEdges[pos]
            length = int(G.get_edge_data(shortEdge[0], shortEdge[1])['weight'])
        # add this edge to MST
        MST.append(shortEdge)
        # add the new vertex to X
        cnctCities.append(shortEdge[1])# the name
        cnctCities.append(shortEdge[0])  # the name
        count -= length
        numCities += 1
        #print("The length is " + str(length) + " and the current count is " + str(count))
    print(startCity + ", " + str(numCities))
    return MST


def longestRoadA(G, startCity, roadsLeft):
    alreadyUsed = list()
    #cityTrail = list()
    #ans = longestRoad(G, startCity, roadsLeft, alreadyUsed, cityTrail)
    ans = longestRoad(G, startCity, roadsLeft, alreadyUsed)
    print(ans[0])
    print(ans[1])
    return 0

#def longestRoad(G, startCity, roadsLeft, alreadyUsed, oldCityTrail):
def longestRoad(G, startCity, roadsLeft, alreadyUsed):
    newList = alreadyUsed.copy()
    currentNode = startCity
    roadLength = 0
    maxPoints = 0
    if roadsLeft < 0:
        ans = [0, newList]
        return ans
    newList.append(currentNode)
    maxList = newList
    #print(alreadyUsed)
    for adj in G[currentNode]:
        if adj not in newList:
            lengthToAdj = int(G.get_edge_data(currentNode, adj)['weight'])
            if lengthToAdj > roadsLeft:
                points = 0
            else:
                result = list(longestRoad(G, adj, roadsLeft-lengthToAdj, newList))
                points = result[0] + roadPoints[int(lengthToAdj)]
            if points > maxPoints:
                maxPoints = points
                maxList = result[1]
                #print("The new max points for "+currentNode+" is "+adj)
    #print("City "+startCity+" has "+str(maxPoints)+" points")
    #print(cityTrail)
    ans = [int(maxPoints), maxList]
    #print(ans[1])
    return ans

#Print the maximum cities connected to Boston as a test
#print(maximum_cities_connected(network = G, currNode = "Boston", numTrains = 10, connectedCities = ["Boston"]))
#print("hello")
#print(prim(G, "Boston"))
#stats(G)
empty = list()


for node in G.nodes:
    longestRoadA(G, node, 45)
#for e in list(G.edges):
 #   #print (e.data('weight'))
  #  print(G.get_edge_data(e[0], e[1])['weight'])
