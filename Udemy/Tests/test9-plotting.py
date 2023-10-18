# import the required modules
import matplotlib.pyplot as plt
import numpy as np
# generate x over the range from 0 to 2 pi with 50 intervals
x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)  # compute the sin of x
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['sin(x)'])
plt.show()
