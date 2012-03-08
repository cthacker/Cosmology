#!/usr/bin/env python
import integrate
import math
import numpy as np
import matplotlib.pyplot as plt

#This program calls the integration module and plots the results

#define constants of the problem
c = 299792       #speed of light in km/s
H0 = 70.0        #hubble const in km/s/Mpc
omega_l = 0.7   
omega_m = 0.3
omega_r = 0.0
omega_k = 1-(omega_l+omega_m+omega_r)  

#Initializes two arrays for plotting
z=60
x = np.arange(0,z,0.1)
r=[]
dl=[]
da=[]

def func(z):
       return c/H0/math.sqrt(omega_l + omega_k*(1+z)**2 + omega_m*(1+z)**3 +\
               omega_r*(1+z)**4)  

for i in range(0,z*10):
    s=.1*i                                 
     #calls integration using the Simpson method with 2*500 steps 
    r.append(integrate.Simpsonint(0,s,500,func)) 
    dl.append(r[i]*(1+s))
    da.append(r[i]/(1+s))

plt.figure(1)
plt.subplot(311)
plt.plot(x,r)
plt.subplot(312)
plt.plot(x,dl)
plt.subplot(313)
plt.plot(x,da)

plt.show()
