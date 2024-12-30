#easy heart for pyton

import math
from turtle import *
def heart1(h):
    return 15*math.sin(h)**3
def heart2(h):
    return 12*math.cos(h)-5*\
            math.cos(2*h)-2*\
            math.cos(3*h)-\
            math.cos(4*h)
speed(1000)
bgcolor('#212121')
for i in range(6000):
    goto(heart1(i)*20,heart2(i)*20)
    for i in range(5):
        color("#f56f6f")
    goto(0,0)
done()