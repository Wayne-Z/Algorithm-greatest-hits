# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 10:41:07 2019

@author: Zymieth
"""
import numpy as np

with open('L:\Algorithms\kargerMinCut.txt') as file:
    graph = [n for n in [line.split('\t')[:-1] for line in file]]

class Graph(object):
    def __init__(self,adjacency_list):
        self.adj = {}
        for i,d in enumerate(adjacency_list):
            self.adj[i+1] = [int(num) for num in d]
        self.og = self.adj
        self.deleteSelfLoops()
        
    def selectNode(self):
        return np.random.choice(list(self.adj.keys()),replace=False)
    
    def selectEdge(self,node):
        return np.random.choice(self.adj[node],replace=False)
    
    def contract(self,node,edge):
            self.adj[edge] = list(filter(lambda x: x != node,self.adj[edge]))
            self.adj[edge].extend(list(filter(lambda x: x != edge,self.adj[node])))
            del self.adj[node]
            self.replace(node,edge)
    
    def deleteSelfLoops(self):
        for key in self.adj.keys():
            self.adj[key] = list(filter(lambda x: x != key, self.adj[key]))
            
    def replace(self,inst1,inst2):
        for key in self.adj.keys():
            self.adj[key] = [i if i!=inst1 else inst2 for i in self.adj[key]]
         
    def findMinCut(self, iterations = 10):
        min_cut = len(self.adj)
        for i in range(iterations):
            while len(list(self.adj.keys())) > 2:
                node = self.selectNode()           
                edge = self.selectEdge(node)
                self.contract(node,edge)
            if min([len(i) for i in list(self.adj.values())]) < min_cut: 
                min_cut = min([len(i) for i in list(self.adj.values())])
            self.adj = self.og
        return min_cut
            
                

s_graph = [[2],[1,3],[2,4],[3]] 
G = Graph(s_graph)
x = G.findMinCut()
s_graph = graph
G = Graph(s_graph)
x = G.findMinCut(iterations=10000000)
    