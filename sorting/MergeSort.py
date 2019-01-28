# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:36:49 2018

@author: Zymieth
"""
import numpy as np

def merge_sort(num_list):
    '''
    Implementation of vanilla merge sort, O(nlogn) 
    '''    
    if len(num_list) == 1:
        return num_list
   
    l = len(num_list)//2
    l1 = merge_sort(num_list[:l])
    l2 = merge_sort(num_list[l:])
    
    v = []
    i = 0
    j = 0
    
    # merging subroutine, break from loop when one of the pointers falls off
    for k in range(len(l1)+len(l2)):
        if j == len(l2) or i == len(l1): break            
        if l1[i] <= l2[j]:
            v.append(l1[i])
            i += 1
        else:
           v.append(l2[j])
           j += 1
    # handling final remaining elements in either l1 or l2
    while(i < len(l1)):
        v.append(l1[i])
        i += 1
    while(j < len(l2)):
        v.append(l2[j])
        j += 1   
    return v

def count_inversions(num_list, count = 0):
    '''
    Counts number of inversions in array of numbers num_list
    '''   
    if len(num_list) == 1:
        return num_list, count
    
    l = len(num_list)//2
    l1, count = count_inversions(num_list[:l], count)
    l2, count = count_inversions(num_list[l:], count)
    
    v = []
    i = 0
    j = 0
    
    # merging subroutine, break from loop when one of the pointers falls off
    for k in range(len(l1)+len(l2)):
        if j == len(l2) or i == len(l1): break            
        if l1[i] <= l2[j]:
            v.append(l1[i])
            i += 1
        else:
           v.append(l2[j])
           j += 1
           count += len(l1)-i
    # handling final remaining elements in either l1 or l2
    while(i < len(l1)):
        v.append(l1[i])
        i += 1
    while(j < len(l2)):
        v.append(l2[j])
        j += 1         
    return v, count

###################################################### TESTS: merge_sort 
n = np.array([2,5,1,3,4])
n = merge_sort(n)
assert np.all([n[i] <= n[i+1] for i in range(len(n)-1)])

n = np.array([6,3,6,8,3,2,-40,20,4.2,4,0,3,215])
n = merge_sort(n)
assert np.all([n[i] <= n[i+1] for i in range(len(n)-1)])

n = np.random.rand(100)
n = merge_sort(n)
assert np.all([n[i] <= n[i+1] for i in range(len(n)-1)])

n = np.loadtxt("L:\Algorithms\tests-merge.txt")
n = merge_sort(np.array(n))
assert np.all([n[i] <= n[i+1] for i in range(len(n)-1)])

###################################################### TESTS: count_inversions
n = np.array([2,5,1,3,4])
n, c = count_inversions(n)
assert np.all([n[i] <= n[i+1] for i in range(len(n)-1)])
assert c == 4

n = np.loadtxt("L:\Algorithms\tests-merge.txt")
n, c = count_inversions(n)
assert np.all([n[i] <= n[i+1] for i in range(len(n)-1)])
assert c == 2407905288
