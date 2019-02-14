# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 03:29:34 2019

@author: Zymieth
"""
import math
import itertools

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

with open('tsp.txt') as file:
    x = [row[:-1].split(' ') for row in file]
    npoints = int(x[0][0])
    x = x[1:]
    
class Point(object):
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.id = num
        self.visited = False
    
    def distance(self, point):
        return math.sqrt((self.x-point.x)**2 + (self.y-point.y)**2)
    
    def set_visited(self):
        self.visited = True
    
    def is_visited(self):
        return self.visited
    
list_points = [Point(float(x[i][0]), float(x[i][1]), i) for i in range(npoints)]

def getDist(lop,i,j):
    return lop[i].distance(lop[j])

def toBinary(n):
    return '{:032b}'.format(n)

def lenBinarySet(n):
    count = 0
    for el in n:
        if el == 1: count += 1
    return count

def getCities(n):
    r = []
    if n/2 > 0:
        r.append(n)
    return r

n = 6
all_distances = [[getDist(list_points,i,j) for i in range(n)] for j in range(n)]

def dynamicTSP(list_o_points, n):
    # initialize dynamic programming storing list of lists   
    # +1 is for one indexing and making everything clearer
    A = {}
    
    # distances from source vertex to all others
    dist_from_source = [getDist(list_o_points,0,j) for j in range(n)]  
    
    # distance from source to itself
    A[0,0] = 0
    
    # distance from source to vertex j
    for j in range(1, n): 
        A[2**j,0] = dist_from_source[j]

    # for all sets/combination of cities
    subsets = range(1, 2**n)
    
    # ordering by cardinality of the subset
    for subset in sorted(subsets, key=lambda m: '{:032b}'.format(m).count('1')):       
        print('{:032b}'.format(subset).count('1'))
        if not subset & 1:
            # vertex 1 not present
            continue
        for j in range(2, n+1):
            if not (1<<(j)) & subset:
                #vertex j not in subset
                continue
            for k in range(1, yn+1):
                if k == j or not (1<<(k)) & subset:
                    continue
                try:
                    A[subset-1,j-1] = min(A[subset-1,j-1], A[(subset^(1<<(j)))-1,k-1] + getDist(list_o_points,j-1,k-1))
                except:
                    A[subset-1,j-1] = math.inf
    return A

            
        
#dynamicTSP(list_points, npoints)
a = dynamicTSP(list_points[:6],6)
    


    
    