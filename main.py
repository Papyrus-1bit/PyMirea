from math import *


def func_a(x):
    return sin(88*pow(x,4))

def func_b(z):
    return 47*pow(z,3)

def func_d(x,z):
    return sqrt((pow(x,7)/10-pow(z,4)/10-13)/(tan(x)-sin(z)))

def func_c(x,y,z):
    return (tan(z)-52*pow(z,6)+42)/(pow(y,2)+32*pow(x,7))

def func(x,y,z):
    a = func_a(x)+func_b(z)+func_d(x,z)-func_c(x,y,z)+66
    print('{:.2e}'.format(a))
    return 

func(-91,4,76)
func(-72,95,-87)
func(45,-6,-12)

