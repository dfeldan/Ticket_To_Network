import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
#G.add_node("Node 1")



file = open("Network.txt", "rb")
G = nx.read_weighted_edgelist(file)
file.close()

#print(list(G.nodes))

print(G.number_of_nodes())
print(G.number_of_edges())
#plt.subplot(121)
#nx.draw(G, with_labels=True, font_weight='bold')
#plt.subplot(122)
#nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
#text = file.readlines()
#file.close()

