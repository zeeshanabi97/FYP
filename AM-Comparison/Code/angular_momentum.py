import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


data = pd.read_csv('Model',delimiter='\t') # Read file of the Model

#Centering the data at black hole
data['x']=data['x']-data['x'][0]
data['y']=data['y']-data['y'][0]
data['z']=data['z']-data['z'][0]
data['vx']=data['vx']-data['vx'][0]
data['vy']=data['vy']-data['vy'][0]
data['vz']=data['vz']-data['vz'][0]

#Calculate Angular Momentum Along x,y and z.
data['Lx']=data['m']*(data['y']*data['vz']-data['z']*data['vy'])
data['Ly']=data['m']*(data['z']*data['vx']-data['x']*data['vz'])
data['Lz']=data['m']*(data['x']*data['vy']-data['y']*data['vx'])

#Calculating Radius
data['r']=(data['x']**2+data['y']**2+data['z']**2)**0.5

#An array for mean raddi on which we will plot our Momentum Count
meanr=[]

for i in range (0,100):
    meanr.append((i/10)+0.05)
    
#Taking ratio of positives to total
ratiopx=[] #1. Ratio of L along x axis 
for i in range (0,100):       
    ratiopx.append(data['r'].loc [(data['r']>float(i)/10)&(data['r']\
    <float(i)/10+0.1)&(data['Lx']>0)].count()/data['r'].loc [(data['r']\
    >float(i)/10)&(data['r']<float(i)/10+0.1)].count())

ratiopy=[] #2. Ratio of L along y axis 
for i in range (0,100):       
    ratiopy.append(data['r'].loc [(data['r']>float(i)/10)&(data['r']\
    <float(i)/10+0.1)&(data['Ly']>0)].count()/data['r'].loc [(data['r']\
    >float(i)/10)&(data['r']<float(i)/10+0.1)].count())   
                                                                
ratiopz=[] #3. Ratio of L along z axis 
for i in range (0,100):       
    ratiopz.append(data['r'].loc [(data['r']>float(i)/10)&(data['r']\
    <float(i)/10+0.1)&(data['Lz']>0)].count()/data['r'].loc [(data['r']\
    >float(i)/10)&(data['r']<float(i)/10+0.1)].count())                                                                


#%%
#Zoom in plot 
fig = plt.figure()
plt.rcParams['figure.dpi'] = 1000
ax = fig.add_subplot(111)
ax.plot(meanr,ratiopx,label='Lx')
ax.plot(meanr,ratiopy, c = 'green',label='Ly')
ax.plot(meanr,ratiopz, c = 'purple', label='Lz')
ax.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
plt.title("Radial Distribution of Positive and Negative Angular Momenta")


ax2 = ax.twinx()
ax2.set_ylim(0.6, 0.4)
ax.set_ylim(0.4, 0.6)
ax.set_xlim(0,1)
ax.axhline(0.5,c='red',ls='--',alpha=.7, label='Isotropic Distribution')

#defining plot axis 
ax.set_xlabel("R")
ax.set_ylabel("N(L+)/N")
ax2.set_ylabel("N(L-)/N")                                                                

ax.legend()


#%%                                                              
#Plot
fig = plt.figure()
plt.rcParams['figure.dpi'] = 1000
ax = fig.add_subplot(111)
ax.plot(meanr,ratiopx,label='Lx')
ax.plot(meanr,ratiopy, c = 'green',label='Ly')
ax.plot(meanr,ratiopz, c = 'purple', label='Lz')
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
plt.title("Radial Distribution of Positive and Negative Angular Momenta")

ax2 = ax.twinx()
ax2.set_ylim(1, 0)
ax.set_ylim(0, 1)
ax.axhline(0.5,c='red',ls='--',alpha=.7, label='Isotropic Distribution')

#defining plot axis 
ax.set_xlabel("R")
ax.set_ylabel("N(L+)/N")
ax2.set_ylabel("N(L-)/N")                                                                

ax.legend()
plt.show()