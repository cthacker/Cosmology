#!/usr/bin/env python
import math

#computes the linear power spectrumi, \delta^2

As=(4.657e-5)**2  
knorm=.05
c = 300000       #speed of light in km/s
H0 = 70.0        #hubble const in km/s/Mpc
h=.7
omega_l = 0.7   
omega_m = 0.27
omega_r = 0.0
omega_k = 1-(omega_l+omega_m+omega_r) 
Ga=.76
n=.966
a=1.0

def x(k):
    return k/(omega_m * h**2)

def C(x):
    return 14.4 + 325.0/(1+60.5*x**1.11)

def L(x):
    return math.log(math.e + 1.84*x)

def T(x):
    return L(x)/(L(x) + C(x)*x**2)

def deltasq(k,a): 
    return 4*As/25*(Ga*a/omega_m)**2 *(c*k/H0)**4 * (k/knorm)**(n-1) * \
            T(x(k))**2


def transf(k,a):
    stuff = math.sqrt(4*As/25*(Ga*a/omega_m)**2 *(c/H0)**4)*T(x(k))
    return stuff
