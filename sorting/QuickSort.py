# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 13:48:17 2019

@author: Zymieth
"""

import numpy as np
import pandas as pd

comp_count = 0

def quicksort(num_list, l, r):
    if r-l <= 1:
        return None
    global comp_count
    comp_count += r-l-1
    j = partition(num_list, l, r)           
    quicksort(num_list, l, j)
    quicksort(num_list, j + 1, r)
                

def partition(num_list, l, r):
    p = r-1
    num_list[p], num_list[l] = num_list[l], num_list[p]
    j = l+1
    for i in range(l+1,r):
        if num_list[i] < num_list[l]:
            num_list[j], num_list[i] = num_list[i], num_list[j]
            j += 1
    num_list[l], num_list[j-1] = num_list[j-1], num_list[l]
    return j-1

                
#TEST :1:       
a = [1,3,2,6,4,7,9,-52,100,57,23,2,6,7] 

quicksort(a,0,len(a))   
print(a) 

# TEST :2:
PATH = ''
data = pd.read_csv(f'{PATH}/test-sort.txt') 
data = np.array(data)

quicksort(data,0,len(data))