# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:41:44 2019

@author: Zymieth
"""

with open('dijkstraData.txt') as file:
    x = [row.split('\t') for row in file]
    x = [[n.split(',') for n in row[:-1]] for row in x]
    x = [[[int(a) for a in n] for n in row] for row in x]
    graph = x

# currently not needed
need_nodes = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
subgraph = [n for n in x if n[0][0] in need_nodes]


def removeUnwantedNodes(G, need_nodes):
    G_new = []
    for i, row in enumerate(G):
        new = []
        for el in row[1:]:
            if el[0] in need_nodes:
                new.append(el)
        G_new.append(new)
    return G_new
      
subgraph = removeUnwantedNodes(subgraph,need_nodes)
                

class Graph(object):
    def __init__(self, adj_list):
        self.nodes = [n[0][0] for n in adj_list]
        self.edges = [n for n in adj_list]
        self.visited = []
        
    def Dijkstra(self, start):
        A = {}       
        node = start

        # initialization of hash      
        for n in range(1,len(self.nodes)+1):
            A[n] = float('inf')
      
        A[node] = 0  
        while self.visited != self.nodes:
            
            if len(self.visited) == len(self.nodes) - 1:
                self.visited.append(node)
                break
            
            self.visited.append(node)
            
            opt = float('inf')
            mcost = float('inf')
            for n in self.visited:            
                candidates = [e for e in self.edges[n-1][1:] 
                              if e[0] not in self.visited]
                
                if len(candidates) != 0:
                    for c in candidates:
                        nxt, cost = c 
                        # check optimality of edge selection
                        if A[n]+cost < A[n]+mcost and A[n]+cost < opt:
                            opt = A[n]+cost
                            mnxt, mcost, origin = nxt, cost, n
                            print(mnxt,mcost,origin)
                    
            A[mnxt] = A[origin] + mcost
            node = mnxt

        return A

# test on small graph
sg = [[[1], [2, 20], [4, 30]], 
      [[2], [1, 20], [3, 20]], 
      [[3], [2, 30], [4, 20]], 
      [[4], [1, 30], [3, 20]]]

sG = Graph(sg)
a = sG.Dijkstra(1)   
    
# test on proper graph    
G = Graph(graph)
sol = G.Dijkstra(1)
            
    


    
    
                   