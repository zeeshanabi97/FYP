import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


data = pd.read_csv('Model.dat',delimiter='\t') # Read file of the Model
data['s']=0.0001 #adding softing column

#Centering the data at black hole
data['x']=data['x']-data['x'][0]
data['y']=data['y']-data['y'][0]
data['z']=data['z']-data['z'][0]
data['vx']=data['vx']-data['vx'][0]
data['vy']=data['vy']-data['vy'][0]
data['vz']=data['vz']-data['vz'][0]

#Rearranging Data
cols=list(data.columns.values)
data1=data[[cols[6]]+cols[0:6]+[cols[7]]]

#Saving data1 to a file
data1.to_csv('0000',sep='\t',index_label='n')
