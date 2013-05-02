import networkx as nx
from random import random

def instance7():
    """
    Returns a 3-element tuple (G,T,leaves) where G is the graph
    T is the optimal solution and leaves is the number of leaves
    in the optimal solution.
    
    The graph is constructed by creating 4 stars with 90 nodes and
    adding 10 random nodes.
    """
    
    #create a star of 4 stars
    starList = []
    
    starList.append(nx.star_graph(22))
    starList.append(nx.star_graph(21))
    starList.append(nx.star_graph(21))
    starList.append(nx.star_graph(21))
    
    T = nx.Graph()
    for star in starList:
        T = nx.disjoint_union(T,star)
        
    T.add_node(89)
    T.add_edges_from([(89,0),(89,23),(89,67),(89,45)])
    
    #add 10 more nodes with random edges
    T.add_nodes_from(range(90,101))
    for i in range(90,101):
        x = int(random()*5371)%90
        T.add_edge(i,x)
    
    #randomize the label of nodes
    for n in T.nodes():
        new = n + int(random()*2000)
        while(new in T.nodes()):
            new = n + int(random()*2000)
        T = nx.relabel_nodes(T,{n:new})
        
    G = nx.Graph()
    G.add_nodes_from(T.nodes())
    G.add_edges_from(T.edges())

    # add random edges
    for i in range(1000):
        x = int(random()*15897)%100
        y = int(random()*17691)%100
        G.add_edge(G.nodes()[x],G.nodes()[y])
        
    return (G,T)