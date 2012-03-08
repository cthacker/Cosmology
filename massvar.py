#!/usr/bin/env python
import linpwer
import integrate
import math
import numpy as np
import matplotlib.pyplot as plt   


def r(m):
    return (3.*m/(4*np.pi*.3*2.76e11))**(1./3)

def sigma(r):
    def integrand(k):
        first = 9.*(np.sin(k*r)/(k*r)**3 -np.cos(k*r)/(k*r)**2)**2\
            *linpwer.deltasq(k,1)/k
        second =9*(np.sin(r/k)/(r/k)**3 -np.cos(r/k)/(r/k)**2)**2\
            *linpwer.deltasq(1/k,1)/k


        return math.sqrt(first + second)
    #return quad(integrand,.001,1.,limit=1000)
    return integrate.Simpsonint(.001,1.,200,integrand)

rr=1.0e19
x=np.linspace(1.0e8,rr,20000)
sig=[]



for m in x:
    sig.append(sigma(r(m)))


plt.plot(x,sig)
plt.xscale('log')
plt.yscale('log')
plt.title('Mass Variance')
plt.xlabel('$h^{-1}M_{\odot}$')
plt.ylabel('$\sigma$')
plt.show()
