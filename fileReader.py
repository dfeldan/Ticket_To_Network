import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

file = open("Network.txt", "rb")
G = nx.read_weighted_edgelist(file)
file.close()

#List the nodes
#print(list(G.nodes))

#Get Number of nodes and edges
print(G.number_of_nodes()) #Should be 37
print(G.number_of_edges())	#SHould be 78

#Attempt to graph the network
#plt.subplot(121)
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.subplot(122)
#nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')


