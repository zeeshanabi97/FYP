# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
r = np.arange(0.00001,10,0.00001)
M = 1
a = 1 #scaling radius
m1 = M*((r/(r+a))**3) # gamma is 0
m2 = M*(r/(r+a))**2 # gamma is 1
m3 = M*(r/(r+a)) # gamma is 2

#%%

# Create the plot
plt.xscale("log")#Makes x-axis logarithmic
plt.yscale("log")#Makes x-axis logarithmic

# Add a title
plt.title('Analytical Distribution of Commulative Mass')

# Add X and y Label

plt.xlabel('R')
plt.ylabel('M(r)')

plt.xlim([10e-2,10e+0])
plt.ylim([10e-4,10e-1])


# Add a Legend
plt.rcParams['figure.dpi'] = 1000
plt.plot(r,m1)
#plt.plot(r,m1,label='γ=0')
#plt.plot(r,m2,label='γ=1')
#plt.plot(r,m3,label='γ=2')
plt.legend(loc='lower right')



# Show the plot
plt.show()
