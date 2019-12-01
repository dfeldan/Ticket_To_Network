import networkx as nx
import matplotlib.pyplot as plt
import csv
import operator
import time

roadPoints = [0,1,2,4,7,10,15]

G = nx.Graph()

file = open("Network.txt", "rb")
G = nx.read_weighted_edgelist(file)
file.close()
<<<<<<< HEAD
<<<<<<< HEAD


#Print Degree to a file
file = open("degree.csv", "w")
w = csv.writer(file)
for city, degree in sorted(G.degree):
    w.writerow([city, degree])
file.close()

=======
>>>>>>> 5103d66dafaa71f489decb9751e431a029bd4c79
=======
>>>>>>> 5103d66dafaa71f489decb9751e431a029bd4c79
#List the nodes
#print(list(G.nodes))

# #Get Number of nodes and edges
# print(G.number_of_nodes()) #Should be 37
# print(G.number_of_edges())	#SHould be 78

# #Get betweeness
# edgeBetween = nx.edge_betweenness_centrality(G)
# nodeBetween = nx.betweenness_centrality(G)

#Print Betweeness to a file
# file = open("nodeBetween.csv", "w")
# w = csv.writer(file)
# for key, val in sorted(nodeBetween.items(), key = operator.itemgetter(1)):
#     w.writerow([key,val])
# file.close()
# file = open("edgeBetween.csv", "w")
# w = csv.writer(file)
# for key, val in sorted(edgeBetween.items(), key = operator.itemgetter(1)):
#     w.writerow([key,val])
# file.close()

#Draw the network
#nx.draw(G)
#plt.show()

# @Params 
# network = the network you are working with 
# currNode = the node on the current stage of traversal
# numTrains = number of trains left to go to new nodes
#connectedCities = number of trains currently in the subgraph

#There is a problem where it is not return the correct input. I think it has to do with the fact that the alg 
#ignores a subgraph if it is the same size as the current max size subgraph. I need to think on how to fix this issue
# def maximum_cities_connected(network, currNode, numTrains, connectedCities, currentEdges):
#     tempConnnectedCities = connectedCities.copy()
#     tempCurrentEdges = currentEdges.copy()
#     tempNumTrains = numTrains
#     maxNumTrains = numTrains
#     maxNumConnectedCities = connectedCities.copy() #Saving so we can return later
#     maxCurrentEdges = currentEdges.copy()
#     for adjNode in network[currNode]:   #Traverse over each node that is adjacent to currNode
#         if tempConnnectedCities.count(adjNode) == 0:   #If we added the adjacent node to the subgraph, ignore it
#             cost = network.get_edge_data(currNode, adjNode)['weight']   #get the cost of traveling to this node
#             if cost <= tempNumTrains:    #If we have enough trains to travel to this node...
#                 tempConnnectedCities.append(adjNode) #add that node the the subgraph
#                 tempCurrentEdges.append({currNode,adjNode})
#                 tempNumTrains = numTrains - cost
#                 checkNumTrains, checkConnectedCities, checkCurrentEdges = maximum_cities_connected(network, adjNode, tempNumTrains, tempConnnectedCities, tempCurrentEdges) #Then find the maximum number of nodes reachable from it
#                 if len(checkConnectedCities) >= len(maxNumConnectedCities): #If this new subgraph is bigger than the previous biggest, save it
#                     maxNumTrains = checkNumTrains
#                     maxNumConnectedCities = checkConnectedCities
#                     maxCurrentEdges = checkCurrentEdges
#     return maxNumTrains, maxNumConnectedCities, maxCurrentEdges    #Return the biggest subgraph

# def maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n):
#     if numTrains == 0 or n == len(edgeQueue):
#         return connectedCities, connectedPath
#     cost = network.get_edge_data(edgeQueue[n][0], edgeQueue[n][1])['weight']
    
#     if cost > numTrains:
#         return maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n+1) 

#     if connectedCities.count(edgeQueue[n][1]) != 0:
#         return maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n+1) 

#     #print(connectedCities)
#     tempConnnectedCities = connectedCities.copy()
#     tempConnectedPath = connectedPath.copy()
#     tempConnnectedCities.append(edgeQueue[n][1])
#     tempConnectedPath.append(edgeQueue[n])

#     tempEdgeQueue = edgeQueue.copy()
#     for edge in network.edges(edgeQueue[n][1]):
#        if edgeQueue.count([edge[0], edge[1]]) == 0 or edgeQueue.count([edge[1], edge[0]]) ==0:
#             if tempConnnectedCities.count(edge[1]) == 0 or tempConnnectedCities.count(edge[0]) == 0:
#                 tempEdgeQueue.append(edge)
#     connectedCitiesWith, ConnectedPathWith = maximum_cities_connected(network, numTrains - cost, tempConnnectedCities, tempConnectedPath, tempEdgeQueue, n+1)
#     connectedCitiesWithout, ConnectedPathWithout = maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n+1)

#     if len(connectedCitiesWith) > len(connectedCitiesWithout):
#         return connectedCitiesWith, ConnectedPathWith
#     else:
#         return connectedCitiesWithout, ConnectedPathWithout

# currNode = "Boston"
# adjEdges = []
# for edge in G.edges(currNode):
#     adjEdges.append(edge)

# numTests = 15
# times = []

# for i in range(2,24):
#     start = time.time()
#     for x in range(numTests):
#     #Print the maximum cities connected to Boston as a test
#         maximum_cities_connected(network = G, numTrains = i, edgeQueue = adjEdges.copy(), connectedCities = ["Boston"], connectedPath = [], n = 0)
#     end = time.time()
#     times.append((end-start)/numTests)
#     print((end-start)/numTests)

# file = open("timeTest.csv", "w")
# w = csv.writer(file)
# for key in sorted(times):
#     w.writerow([key])
# file.close()
# print(times)

# for edge in G.edges("Boston"):
#     print(edge[1])

##TODO ALL THE NEW STUFF PRIM + LONGEST ROAD
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

