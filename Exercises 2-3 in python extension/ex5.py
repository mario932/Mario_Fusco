import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 100, 50) 

y = -(x-50)**2 + 2500
for delta, color in zip([2250, 2000, 1750, 1500, 1250, 1000, 750], ["r", "orange", "g", "b", "indigo", "violet", "white"] ):
    y_new = -(x-50)**2 + delta
    plt.plot(x, y, "-k")
    plt.fill_between(x, y, y_new, color=color)
    
    y = y_new
    
plt.ylim(0, 2500)
plt.savefig('rainbow.png')
plt.show()