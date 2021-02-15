from math import *


def f(n):
    return rec_func(n,0)

def rec_func(n,x):
    if n == 0: 
        return x+8
    else:
        return x + (1/59)*(pow(rec_func(n-1,x),2))-tan(rec_func(n-1,x))

    
     
print('{:.2e}'.format(f(4)))
print('{:.2e}'.format(f(1)))
print('{:.2e}'.format(f(0)))
print('{:.2e}'.format(f(11)))