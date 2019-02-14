# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 04:53:06 2019

@author: Zymieth
"""

with open('L:\Algorithms\prim-mst-test.txt') as file:
    graph = [n[:-1] for n in file]
    a = graph.pop(0)
    graph = [n.split(' ') for n in graph]
    graph = [[int(n) for n in l] for l in graph]
    
    def PrimMST(edge_list, nnodes=500,start=1):
        '''
        Input: list of edges of the type [node1, node2, cost]
        Returns overall cost of edges in MST
        '''
        tot = 0
        X = {}
        X[start]=1
        flag=0
        
        while(len(X.keys()))<nnodes:  
            min_cost = [float("inf"),None,None,None]
            for r in edge_list: 
                if (r[0]in X.keys()) ^ (r[1] in X.keys()):
                    # check if r[0] is in X or r[1] is
                    if r[0] in X.keys():flag=0
                    if r[1] in X.keys():flag=1
                                       
                    if r[2] < min_cost[0]:
                        #[cost, target_node, start_node]
                        min_cost = [r[2],r[1],r[0],flag]

            tot += min_cost[0]
            if min_cost[3]==0: X[min_cost[1]]=1
            elif min_cost[3]==1: X[min_cost[2]]=1
            
        return tot

x=[[1,2,1],[2,3,2],[3,4,3],[4,1,4]]
c = PrimMST(x,4)   
d = PrimMST(graph)
    