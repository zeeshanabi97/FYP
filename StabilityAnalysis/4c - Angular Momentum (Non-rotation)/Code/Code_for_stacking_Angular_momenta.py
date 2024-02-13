import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

for i in range(0,6,1):
    globals()['data'+str(i)] = pd.read_csv('000'+str(i)+'_AM.dat' ,delimiter='\t') # Read file of the Model



r = data0['r']
z_0 = data0['pz_0']
z_2 = data2['pz_2']
z_3 = data3['pz_3']
z_4 = data4['pz_4']
z_5 = data5['pz_5']

#%%
fig = plt.figure()
plt.rcParams['figure.dpi'] = 1000
plt.rcParams["figure.figsize"] = (8,6)
ax = fig.add_subplot(111)

ax.plot(r,z_0,label='0.00000000E+00')
ax.plot(r,z_3,label='3.00000000E+01')
ax.plot(r,z_5,label='5.00000000E+01')
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
plt.title("Radial Distribution of Angular Momenta in Time")

#plt.xlim([-0.1,10])

ax2 = ax.twinx()
ax2.set_ylim(1, 0)
ax.set_ylim(0,1)
ax.axhline(0.5,c='red',ls='--',alpha=.7, label='Isotropic Distribution')

#defining plot axis 
ax.set_xlabel("R",fontsize=12)
ax.set_ylabel("N(Lz+)/N",fontsize=11)
ax2.set_ylabel("N(Lz-)/N",fontsize=11)                                                                
ax.legend()
plt.plot()
plt.show()


