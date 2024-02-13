import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

for i in range(0,6,1):
    globals()['data'+str(i)] = pd.read_csv('000'+str(i)+'_CM.dat' ,delimiter='\t') # Read file of the Model

fig = plt.figure()
#plt.rcParams['figure.dpi'] = 1000
ax = fig.add_subplot(111)

r = data0['r']
cm_0_a = data0['cm_a_0']
cm_0_e = data0['cm_e_0']
cm_1_a = data1['cm_a_1']
cm_1_e = data1['cm_e_1']
cm_2_a = data2['cm_a_2']
cm_2_e = data2['cm_e_2']
cm_3_a = data3['cm_a_3']
cm_3_e = data3['cm_e_3']
cm_4_a = data4['cm_a_4']
cm_4_e = data4['cm_e_4']
cm_5_a = data5['cm_a_5']
cm_5_e = data5['cm_e_5']

#%%

plt.plot(r,cm_0_e,label='0.00000000E+00',linewidth=5,c='#FF7F50')
#plt.plot(r,p_2_a,label='Analytical')

plt.plot(r,cm_3_e,label='3.00000000E+01',linewidth=3,c='blue')
#plt.plot(r,p_4_a,label='Analytical')

plt.plot(r,cm_5_e,label='5.00000000E+01',linewidth=2,ls='--', c='yellow')

plt.plot(r,cm_0_a,label='Analytical',linewidth=1,c='#8B8878')


plt.rcParams['figure.dpi'] = 1000
plt.rcParams["figure.figsize"] = (8,6)


plt.xscale('log')
plt.yscale('log')


plt.title ("Cumulative Mass Profiles in Time")

plt.legend()

plt.xlabel('log$_{10}$ R',fontsize=10)
plt.ylabel('log$_{10}$ M(r)',fontsize=10)


print(plt.rcParams.get('figure.figsize'))
