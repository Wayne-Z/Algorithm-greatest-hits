# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 05:42:39 2019

@author: Zymieth
"""

with open('hash2sum.txt') as file:
    x = [int(row[:-1]) for row in file]
    
def twoSum(nums, target):
    '''
    Given a target value returns two distinct numbers x, y in nums s.t x + y = t
    returns x, y, 1 if present, otherwise _, _, 0
    
    :nums: list of int
    :target: int
    '''
    A = {}
    for num in nums:
        A[num] = 1
    
    for num in nums:
        if target-num in A.keys():
            if target-num != num:
                return num, target-num, 1
    return _, _, 0


# test for targets between -10000 and 10000
count = 0
for t in range(-10000,10000+1):
    _, _, r = twoSum(x, t)
    count += r
    print(t)
            


    