# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:33:19 2019

@author: Zymieth
"""

from operator import itemgetter

with open('APSP1.txt') as file:
    x1 = [row[:-1] for row in file]
    x1 = [[int(r) for r in row.split(" ")] for row in x1]
    
with open('APSP2.txt') as file:
    x2 = [row[:-1] for row in file]
    x2 = [[int(r) for r in row.split(" ")] for row in x2]
    
with open('APSP3.txt') as file:
    x3 = [row[:-1] for row in file]
    x3 = [[int(r) for r in row.split(" ")] for row in x3]
    

def adj_listify(g):
    '''
    Returns the adjacency list representation of a directed graph G from a naive
    list of the form [tail, head, edge_cost]
    '''
    graph = []
    sol = []
    g = sorted(g, key=itemgetter(0))
    curr = g[0][0]
    sol.append([curr])
    

    for idx, row in enumerate(g):
        if curr == row[0]: 
            sol.append([row[1], row[2]])           
        else:
            graph.append(sol)
            sol = []
            curr = row[0]
            sol.append([curr])
            sol.append([row[1], row[2]])
            
    # final remaining sublist
    graph.append(sol)   
    return graph

def adj_listify_target(g):
        '''
        Returns the adjacency list representation of a directed graph G from a naive
        list of the form [tail, head, edge_cost]
        where the first element of each sublist is the head of an edge 
        '''
        graph = []
        sol = []
        g = sorted(g, key=itemgetter(1))
        curr = g[0][1]
        sol.append([curr])
        
        for idx, row in enumerate(g):
            if curr == row[1]: 
                sol.append([row[0], row[2]])           
            else:
                graph.append(sol)
                sol = []
                curr = row[1]
                sol.append([curr])
                sol.append([row[0], row[2]])
                
        # final remaining sublist
        graph.append(sol)   
        return graph
    
class Graph(object):
    def __init__(self, adj_list, adj_list_targets):
        self.nodes = [n[0][0] for n in adj_list]
        self.edges = [n for n in adj_list]
        self.heads = [n for n in adj_list_targets]
        self.visited = []
    
    def augment(self):
        '''
        augments graph with artificial node with 0 edge connections 
        to all other vertices
        '''
        new = len(self.nodes)+1
        self.nodes.append(new)
        for row in self.heads:
            row.append([new, 0])
    
    def restoreOriginal(self)   :
        '''
        restores the original G from the augmented version
        '''
        
    def dijkstra(self, start):
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
                    
            A[mnxt] = A[origin] + mcost
            node = mnxt
        
        # reset visited
        self.visited = []
        return A
    
    def bellmanFord(self, start):
        A_prev, A = {}, {}
        
        for n in range(1,len(self.nodes)+1):
            A_prev[n] = float('inf')
            
        A_prev[1] = 0
        
        # edge budget
        for i in range(1, len(self.nodes)+1):
            
            # destination vertex
            for j in range(1, len(self.nodes)+1):
                             
                # bruteforce search to find min edge going into vertex j
                candidate = min(self.heads[j-1][1:],\
                                key = lambda x: x[1] + A_prev[x[0]])
                source, cost = candidate[0], candidate[1]
                A[j] = min(A_prev[j], A_prev[source] + cost)
            
            A_prev, A = A, {}
        return A_prev
                 
# test on small undirected graph   
sg = [[1, 2, 20], [1, 4, 30],
      [2, 1, 20], [2, 3, 20],
      [3, 2, 30], [3, 4, 20],
      [4, 1, 30], [4, 3, 20]]

sg1 = adj_listify(sg)
sg2 = adj_listify_target(sg)

sG = Graph(sg1, sg2)
a1 = sG.dijkstra(1)  
a2 = sG.bellmanFord(1)

 
# x1 = adj_listify(x1)
# x2 = adj_listify(x2)
# x3 = adj_listify(x3) 
# 
# g1 = Graph(x1)
# =============================================================================
