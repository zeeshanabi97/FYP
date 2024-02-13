import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('0003',sep='\s+') # Read file of the original Model
#Centering the data at black hole
data['x']=data['x']-data['x'][0]
data['y']=data['y']-data['y'][0]
data['z']=data['z']-data['z'][0]
data['vx']=data['vx']-data['vx'][0]
data['vy']=data['vy']-data['vy'][0]
data['vz']=data['vz']-data['vz'][0]

#Deleting Black Hole
data.drop([0],inplace=True) 
#Calculating Radius
data['r']=(data['x']**2+data['y']**2+data['z']**2)**0.5

#An array for mean raddi on which we will plot our Momentum Count
newdata=pd.DataFrame()
rr=[]  #rr is repersentative value of radius 
for i in range (1,101):
    rr.append(float(i)/10)  #100 bins - increments
newdata['rr']=rr
# Taking masses with in rings   
cm=[] 
for i in range (1,101):
    cm.append((data['m'].loc [(data['r']>=float(i)/10-0.1)&(data['r']<=float(i)/10)]).sum())
newdata['cm']=cm

#Calculating Volumes of those rings
newdata['V']=(4/3*np.pi*newdata['rr']**3).diff()
newdata['V'][0]=4/3*np.pi*newdata['rr'][0]**3
density= newdata['cm']/newdata['V']


#%%
# Theoratical work
a=1
gamma = 1
M = 1
p = ((3-gamma)*a*M)/((4*np.pi*newdata['rr']**gamma)*(newdata['rr']+a)**(4-gamma)) #gamma is 1

#Making DataFrames
df = pd.DataFrame()
df['r'] = rr
df['p_a_3'] = p
df['p_e_3'] = density

df.to_csv('0003_density.dat', sep='\t')
#%%
# Create the plot
plt.xscale('log')
plt.yscale('log')
plt.plot(rr,p,label='Analytical')
plt.plot(rr,density,label='Experimental Model')
plt.title ("Density Profile - 0005")
plt.legend()

plt.xlabel("Radius")
plt.ylabel("ϼ(r)")