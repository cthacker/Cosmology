#!/usr/bin/env python
import math


def Simpsonint(a, b, n,func):
    #Uses composite Simpson's rule to numerically integrate from a to b
    #There are 2*n steps
    n *= 2
    h = (float(b)-a)/n
    fx = 0.0
    fy = 0.0
        
    for i in range(1,n,2):
        xi = a + i*h
        fx += func(xi)

    for i in range(2,n,2):
        xi = a + i*h
        fy += func(xi)

    sum = 2*fy + 4*fx + func(a) + func(b)

    return (h/3)*sum

   


    
    
    
