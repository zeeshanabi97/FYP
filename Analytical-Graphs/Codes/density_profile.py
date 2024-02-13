# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np

# Create the vectors X and Y
r = np.arange(0.00001,10,0.00001)
a = 1 #scaling radius 
M = 1
x = np.pi
d1 = ((3)*M*a)/(4*x*(r**0)*(r+a)**4) # gamma is 0
d2 = ((2)*M*a)/(4*x*(r**1)*(r+a)**3) # gamma is 1 
d3 = ((1)*M*a)/(4*x*(r**2)*(r+a)**2) # gamma is 2 



# Create the plot
plt.xscale("log")#Makes x-axis logarithmic
plt.yscale("log")#Makes y-axis logarithmic

# Add a title
plt.title('Analytical Distribution of Density')

# Add X and y Label

plt.xlabel(" R")
plt.ylabel('\u03C1(r)')

plt.ylim([10e-6,10e+3])
plt.xlim([0.01,10])

# Add a Legend
plt.rcParams['figure.dpi'] = 1000
plt.plot(r,d1,label='γ=0')
plt.plot(r,d2,label='γ=1')
plt.plot(r,d3,label='γ=2')
plt.legend()



# Show the plot
plt.show()