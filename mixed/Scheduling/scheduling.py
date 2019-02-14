# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 12:43:16 2019

@author: Zymieth
"""
import operator

with open('L:\Algorithms\jobs.txt') as file:
    jobs = [row[0:-1].split(' ') for row in file]
    jobs.pop(0)
    [job.append(i) for i,job in enumerate(jobs)]


def schedulingDiff(jobs, criterion='diff'):
    '''
    Schedules jobs based on weight - length value  
    :criterion: can be 'diff' for w-l or 'ratio' for w/l
    '''
    [job.append(i) for i,job in enumerate(jobs)]
    if criterion=='diff': a_jobs = [[int(job[0]) - int(job[1]),int(job[0]),int(job[1]),int(job[2])] for job in jobs]
    else: a_jobs = [[int(job[0])/int(job[1]),int(job[0]),int(job[1]),int(job[2])] for job in jobs]
    a_jobs.sort(key=operator.itemgetter(1),reverse=True)
    a_jobs.sort(key=operator.itemgetter(0),reverse=True)
    time_elapsed = 0
    C = 0
    for job in a_jobs:
        time_elapsed += int(job[2])
        C += int(job[1])*time_elapsed
        print(C)
    return C,a_jobs
        

x = [[5,1],[10,3],[1,2]]
C1 = schedulingDiff(x)
C2,E = schedulingDiff(jobs,'ratio')
    
    
    