#!/usr/bin/env python
import linpwer
import integrate
import math
import scipy.special
import numpy as np
import matplotlib.pyplot as plt


def ftnfw(m,k):
    rhoc=2.76e11
    omega_m=.3
    rvir=(3*m*178/(4*np.pi*rhoc*omega_m))**(1./3)
    p=m*5.177/(4*np.pi*rvir**3)
    def integrand(r):
        return p*4*np.pi*r**2*np.sin(k*r)/(m*k*r*10*r/rvir*(1+10*r/rvir)**2)
    return integrate.Simpsonint(0.00001,rvir,100000,integrand)


rr=1000
x=np.linspace(.01,rr,600)
nfw1=[]
nfw2=[]
nfw3=[]
nfw4=[]
nfw5=[]
nfw6=[]




for kk in x:
    nfw1.append(ftnfw(10e11,kk))
    nfw2.append(ftnfw(10e12,kk))
    nfw3.append(ftnfw(10e13,kk))
    nfw4.append(ftnfw(10e14,kk))
    nfw5.append(ftnfw(10e15,kk))
    nfw6.append(ftnfw(10e16,kk))


plt.plot(x,nfw1)
plt.plot(x,nfw2)
plt.plot(x,nfw3)
plt.plot(x,nfw4)
plt.plot(x,nfw5)
plt.plot(x,nfw6)
plt.xscale('log')
plt.yscale('log')
plt.title('Fourrier Transfor of NFW')
plt.xlabel('k [h/Mpc]')
plt.ylabel('y(k|m)')
plt.savefig('nfw.png')
plt.show()
