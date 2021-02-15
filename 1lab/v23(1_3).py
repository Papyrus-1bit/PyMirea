from math import *


def func_a(x:int, y:int):
    sum_1 = 0
    sum_2 = 0
    for i in range(1,x+1):
        for j in  range(1,y+1):
            sum_1+=(sin(j)+88*pow(i,4)+89)
    for i in  range(1,x+1):
        for j in range(1,y+1):
            sum_2+=(pow(i,6)/10-pow(j,5)/10-13)
    return sum_1-58*sum_2


print('{:.2e}'.format(func_a(69,54)))
print('{:.2e}'.format(func_a(39,38)))
print('{:.2e}'.format(func_a(99,20)))
