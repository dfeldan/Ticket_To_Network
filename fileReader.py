import networkx as nx
import matplotlib.pyplot as plt
import csv
import operator

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
def maximum_cities_connected(network, currNode, numTrains, connectedCities):
    maxNumConnectedCities = connectedCities #Saving so we can return later
    for adjNode in network[currNode]:   #Traverse over each node that is adjacent to currNode
        if maxNumConnectedCities.count(adjNode) == 0:   #If we added the adjacent node to the subgraph, ignore it
            cost = network.get_edge_data(currNode, adjNode)['weight']   #get the cost of traveling to this node
            if cost < numTrains:    #If we have enough trains to travel to this node...
                newList = connectedCities 
                newList.append(adjNode) #add that node the the subgraph
                reachableCities = maximum_cities_connected(network, adjNode, numTrains - cost, newList) #Then find the maximum number of nodes reachable from it
                if len(reachableCities) > len(maxNumConnectedCities): #If this new subgraph is bigger than the previous biggest, save it
                    maxNumConnectedCities = reachableCities
    return maxNumConnectedCities    #Return the biggest subgraph

#Print the maximum cities connected to Boston as a test
print(maximum_cities_connected(network = G, currNode = "Boston", numTrains = 10, connectedCities = ["Boston"]))    



