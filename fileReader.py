import networkx as nx
import matplotlib.pyplot as plt
import csv
import operator
import time

G = nx.Graph()

file = open("Network.txt", "rb")
G = nx.read_weighted_edgelist(file)
file.close()

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

def maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n):
    if numTrains == 0 or n == len(edgeQueue):
        return connectedCities, connectedPath
    cost = network.get_edge_data(edgeQueue[n][0], edgeQueue[n][1])['weight']
    
    if cost > numTrains:
        return maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n+1) 

    if connectedCities.count(edgeQueue[n][1]) != 0:
        return maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n+1) 

    #print(connectedCities)
    tempConnnectedCities = connectedCities.copy()
    tempConnectedPath = connectedPath.copy()
    tempConnnectedCities.append(edgeQueue[n][1])
    tempConnectedPath.append(edgeQueue[n])

    tempEdgeQueue = edgeQueue.copy()
    for edge in network.edges(edgeQueue[n][1]):
       if edgeQueue.count([edge[0], edge[1]]) == 0 or edgeQueue.count([edge[1], edge[0]]) ==0:
            if tempConnnectedCities.count(edge[1]) == 0 or tempConnnectedCities.count(edge[0]) == 0:
                tempEdgeQueue.append(edge)
    connectedCitiesWith, ConnectedPathWith = maximum_cities_connected(network, numTrains - cost, tempConnnectedCities, tempConnectedPath, tempEdgeQueue, n+1)
    connectedCitiesWithout, ConnectedPathWithout = maximum_cities_connected(network, numTrains, connectedCities, connectedPath, edgeQueue, n+1)

    if len(connectedCitiesWith) > len(connectedCitiesWithout):
        return connectedCitiesWith, ConnectedPathWith
    else:
        return connectedCitiesWithout, ConnectedPathWithout

currNode = "Boston"
adjEdges = []
for edge in G.edges(currNode):
    adjEdges.append(edge)

numTests = 15
times = []

for i in range(2,24):
    start = time.time()
    for x in range(numTests):
    #Print the maximum cities connected to Boston as a test
        maximum_cities_connected(network = G, numTrains = i, edgeQueue = adjEdges.copy(), connectedCities = ["Boston"], connectedPath = [], n = 0)
    end = time.time()
    times.append((end-start)/numTests)
    print((end-start)/numTests)

file = open("timeTest.csv", "w")
w = csv.writer(file)
for key in sorted(times):
    w.writerow([key])
file.close()
print(times)
# for edge in G.edges("Boston"):
#     print(edge[1])

