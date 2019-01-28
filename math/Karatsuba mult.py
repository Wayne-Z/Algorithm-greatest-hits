# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 17:55:15 2018

@author: Zymieth
"""
import math

def split_num(number, n):
    '''
    splits a number at position n and returns both halves
    '''
    if len(str(abs(number))) == 1:
        return (0,number)
    lh = number // 10**n 
    rh = number % 10**n
    return(lh,rh)
    
def karatsuba(x,y):
    '''
    Performs Karatsuba's Multiplication Algorithm on integers X and Y,
    assumed to be of same length n
    '''
    if x < 10 and y < 10:
        return x*y
    else:     
        l = len(str(abs(x)))
        a,b = split_num(x,math.ceil(l/2))
        c,d = split_num(y,math.ceil(l/2))
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        return 10**(l)*ac + 10**math.ceil(l/2)*(karatsuba(a+b,c+d)-ac-bd) + bd
    

#testing
        
num = [1234, 875543, 11, 0]
pos = [2, 3, 1, 0]

for i in range(len(num)):
    print(split_num(num[i],pos[i]))
    
print(karatsuba(800, 200))
print(karatsuba(12, 21))
print(karatsuba(13121232, 24857389))