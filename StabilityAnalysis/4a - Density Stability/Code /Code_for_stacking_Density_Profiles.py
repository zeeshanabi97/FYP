import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

for i in range(0,6,1):
    globals()['data'+str(i)] = pd.read_csv('000'+str(i)+'_density.dat' ,delimiter='\t') # Read file of the Model



r = data0['r']
p_0_a = data0['p_a_0']
p_0_e = data0['p_e_0']
p_1_a = data1['p_a_1']
p_1_e = data1['p_e_1']
p_2_a = data2['p_a_2']
p_2_e = data2['p_e_2']
p_3_a = data3['p_a_3']
p_3_e = data3['p_e_3']
p_4_a = data4['p_a_4']
p_4_e = data4['p_e_4']
p_5_a = data5['p_a_5']
p_5_e = data5['p_e_5']

#%%
fig = plt.figure()
plt.rcParams['figure.dpi'] = 1000
plt.rcParams["figure.figsize"] = (8,6)

plt.plot(r,p_0_e,label='0.00000000E+00',linewidth=5,c='#FF7F50')
#plt.plot(r,p_2_a,label='Analytical')

plt.plot(r,p_3_e,label='3.00000000E+01',linewidth=3,c='blue')
#plt.plot(r,p_4_a,label='Analytical')

plt.plot(r,p_5_e,label='5.00000000E+01',linewidth=2,ls='--', c='yellow')

plt.plot(r,p_0_a,label='Analytical',linewidth=1.5,c='#8B8878')

plt.title ("Density Profiles in Time")

plt.xscale('log')
plt.yscale('log')


plt.legend()

plt.xlabel('R',fontsize=10)
plt.ylabel('\u03C1 (r)',fontsize=10)

