import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# check available styles
matplotlib.style.available 
# define one style
matplotlib.style.use('ggplot')

# Generate Data
data1 = np.random.normal(30, 4, 200)
data2 = np.random.normal(20, 4, 200)

# Make a histogram of the Data
plt.hist(data1, alpha=0.4, bins=30, density=True, label='Group A')
plt.hist(data2, alpha=0.4, bins=30, density=True, label='Group B')

ax = plt.gca()
ax.set(
xlabel='Data',
ylabel='Proportion',
title='A test histogram')

#display legend
plt.legend()


plt.savefig('matplotlib.png')
# Display the Figure
plt.show()


