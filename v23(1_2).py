from math import *


def func(x:float):
    if x<54:
        return sin(88*pow(x,4))+47*pow(x,3)+66
    elif 54 <= x < 95:
        return (pow(x,6)/10)-(pow(x,5)/10)-13 
    elif 95 <= x <194:
        return tan(12*pow(x,3)-pow(x,7))-tan(pow(x,8))
    elif 194<= x <268:
        return pow(x,2)-15*pow(x,4)
    elif x>=268:
        return 86*pow(x,3)-pow(x,4)/60
        
print('{:.2e}'.format(func(253)))
print('{:.2e}'.format(func(302)))
print('{:.2e}'.format(func(23)))
