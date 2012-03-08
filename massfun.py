#!/usr/bin/env python
import linpwer
import integrate
import math
import scipy.special
import numpy as np
import matplotlib.pyplot as plt
import massvar


rhoc=2.76e11
omega_m=.3
alpha=0.75
dc=1.686
p=0.3

def numdens(m):
    r=(3*m/(4*np.pi*omega_m*rhoc))**(1./3) 
    sigma=massvar.sigma(massvar.r(m))
    nu = dc/sigma
    bias=1+(alpha*nu**2 - 1)/(dc)+2*p/(dc*(1+(alpha*nu**2)**p))
    
    def integrand(k):
        first = 6*(np.sin(k*r)-k*r*np.cos(k*r))*(((k*r)**2 -3)*np.sin(k*r)\
                +3*k*r*np.cos(k*r))/(k*r)**7 *linpwer.deltasq(k,1.)
        
        second = 6*(np.sin(r/k)-r/k*np.cos(r/k))*(((r/k)**2 -3)*np.sin(r/k)\
                +3*r/k*np.cos(r/k))/(r/k)**7 *linpwer.deltasq(1/k,1.)        
        
        return first + second
    return integrate.Simpsonint(.001,1.,200,integrand)*(-1./(2.*sigma**2)*\
        (1/(4*np.pi*rhoc*omega_m))*m**(1/3)   \
        *.315*rhoc*omega_m/m**2*np.exp(-abs(-np.log(sigma))+.61)**3.8)*bias



#print numdens(3*10**14)
stuff = integrate.Simpsonint(3.*10**14,3.*10**19,1,numdens)
File = open(density,'w')
File.write(stuff)
File.close()

r = 100
x=np.linspace(14,19,1000)
x=3*10**x
dist=[]
density =0.0
for m in x:
    dist.append(numdens(m))
    density += numdens(m) 
                  


#plt.plot(x,dist)
#plt.xscale('log')
#plt.yscale('log')
#plt.title('Number Density')
#plt.xlabel('$h^{-1}M_{\odot}$')
#plt.ylabel('Number Density')
#plt.show()
