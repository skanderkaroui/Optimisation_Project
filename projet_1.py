#On commence par importer les packets que l'on va utiliser
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pulp
#Partie Commune
#1-On génere les noeuds et l'ensemble des arcs aléatoirement
N= np.random.randint(20, 100)
A= np.random.randint(50, 100)
#Génerer le graphe dirigé aléatoires avec N noeuds
G=nx.gnm_random_graph(N,A,directed=True)
#Identifie les boucles et les supprimer
boucles=list(nx.selfloop_edges(G))
G.remove_edges_from(boucles)
#Afficher le graphe
nx.draw_spring(G,with_labels=True)
plt.show()
#On s'assure que le nombre 
print("Le nombre de noeuds initialisé est", N, "et le nombre de noeuds du graphe est:", G.number_of_nodes())
print("Le nombre d'arcs initialisé est", A, "et le nombre d'arcs du graphe est:", G.number_of_edges())


