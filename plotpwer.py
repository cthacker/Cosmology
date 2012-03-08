#!/usr/bin/env python
import linpwer
import numpy as np
import math
import matplotlib.pyplot as plt

#This program calls the deltasq module to calculate the linear power spectrum

k=1000
x=np.linspace(.0001,k,10000)
delta=[]

for i in x[:]:
    delta.append(linpwer.deltasq(i,1)*10)

fig=plt.figure()
ax=fig.add_subplot(2,1,1)
ax.plot(x,delta)
ax.set_xscale('log')


#plt.plot(x,delta)
#plt.axes.set_xscale('log')
plt.show()
