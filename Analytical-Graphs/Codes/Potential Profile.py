# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
r = np.arange(0.00001,10,0.00001)
a = 1
G = 1
M = 1

pot1 = -1*(1/(r+1))


# Create the plot
# Define axis 
#%%
plt.xscale("log")#Makes x-axis logarithmic
#plt.yscale("symlog")


# Plot the graph
plt.plot(r,pot1,label='gamma=0')
#plt.plot(r,pot2,label='gamma=1')
#plt.plot(r,pot3,label='gamma=2')


# Add a title
plt.title('Commulative Potential')

# Add X and y Label
plt.xlabel('Radius')
plt.ylabel('Potential')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()