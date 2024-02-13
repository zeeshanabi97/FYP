# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
r = np.arange(0.00001,10,0.00001)
a = 1
G = 1
M = 1
v1 = (G*M*r**2)/((r+a)**3)
v2 = (G*M*r**1)/((r+a)**2)
v3 = (G*M*r**0)/((r+a)**1)
# Create the plot
# Define axis 
plt.xscale("log") #Makes x-axis logarithmic
plt.yscale("log")

#Graph the plots
plt.plot(r,v1,label='gamma=0')
plt.plot(r,v2,label='gamma=1')
plt.plot(r,v3,label='gamma=2')


# Add a title
plt.title('Velocity')

# Add X and y Label
plt.xlabel('Radius')
plt.ylabel('Speed square')

# Add a grid
plt.grid(alpha=.4,linestyle='--')

# Add a Legend
plt.legend()

# Show the plot
plt.show()