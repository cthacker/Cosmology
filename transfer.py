#!/usr/bin/env python
import linpwer
import math
import numpy as np
import matplotlib.pyplot as plt  



f=np.loadtxt('test_transfer_out.dat')
k=f[:,0]
T=f[:,1]


mytran=[]
for stuff in k: 
    mytran.append(2.1*10e3*linpwer.transf(stuff,1))


plt.plot(k,T,label='CAMB Tranfer')
plt.plot(k,mytran,'--',label='My Tranfer')
plt.xscale('log')
plt.yscale('log')
plt.title('Transfer Function')
plt.xlabel('k')
plt.ylabel('T(k)')
plt.legend(loc='upper right')
plt.savefig('tranfer.png')
plt.show()
