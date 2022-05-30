#!/bin/python

import sys
import os
import pylab
import matplotlib.pyplot as plt

os.chdir('c:/dane/btc/crypto-calc-master/log')

x=[]
ysum=[]
for i in os.listdir():
    plik = open(i).read()
    ysum.append(float(plik.split('=')[-1]))
    x.append(i[0:10])
#pylab.plot(x,ysum)
plt.plot(x,ysum)
plt.xticks(range(0,200,30))

"""
y={}
for i in os.listdir():
    plik = open(i).read()
    for j in plik.split('\n')[9:-1]:
        label=j.split(' ')[0]
        if not label in y:
            y[label]={}
        y[label][i[5:10]]=float(j.split('=')[-1])


walory=[]
wartosci=[]
for z in y:
    walory.append(z)
    try:        
        pylab.plot(x,list(y[z].values()))        
    except:
        a=str(sys.exc_info()[1]).split(' ')[-3][1:-2]
        b=str(sys.exc_info()[1]).split(' ')[-1][1:-2]
        roznica=int(a)-int(b)
        wartosci=list(y[z].values())
        wartosci.insert(0,0)
        for u in range(roznica-1):
            wartosci.insert(0,0)
        pylab.plot(x,wartosci)

walory.reverse()
walory.insert(0,'Suma')
pylab.legend(walory)
"""
#pylab.show()
plt.show()

