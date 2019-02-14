# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 05:56:59 2019

@author: Zymieth
"""
import numpy as np
import heapq

with open('Median.txt') as file:
    x = [int(row[:-1]) for row in file]

def heapMedian(nums):
    h_min = [max(nums[0],nums[1])]
    h_max = [-min(nums[0],nums[1])]
    median_ith = [nums[0],(nums[0]+nums[1])/2]
    
    for num in nums[2:]:
        # insert num in correct location
        if num > h_min[0]: heapq.heappush(h_min,num)
        elif num < -h_max[0]: heapq.heappush(h_max,-num)
        else: heapq.heappush(h_min,num)
        
        # balance lenghts of two heaps
        if len(h_max) > len(h_min) + 1:
            tmp = heapq.heappop(h_max)
            heapq.heappush(h_min,-tmp)
        elif len(h_min) > len(h_max) + 1:
            tmp = heapq.heappop(h_min)
            heapq.heappush(h_max,-tmp)
        
        # odd or even median
        if (len(h_min)+len(h_max))%2!=0:
            if len(h_max)>len(h_min): median_ith.append(-h_max[0])
            elif len(h_min)>len(h_max): median_ith.append(h_min[0])
        else: median_ith.append((-h_max[0] + h_min[0])/2)

    return median_ith,h_min,h_max
 
# test
a,mn,mx = heapMedian(x)
assert(a[-1] == np.median(x))

       
