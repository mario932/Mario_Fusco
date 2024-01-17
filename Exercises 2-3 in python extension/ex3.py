import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 20)
y1 = np.sin(x)  #sine function
y2 = np.cos(x + 0.2) #cosine function
y3 = (x + 0.4)  #linear function
y4 = x**2 + 2 * x + 1 #quadratic function
y5 = 5*x**3 + 4 * x**2  + x + 2 #cubic function
y6 = np.tan(x+2) #tangential function


fig = plt.figure(figsize=(14, 7))
plt.suptitle('Multiple Wave Plots', fontweight='bold', fontsize='x-large')

# Subplot 1
plt.subplot(231)
plt.title('sine function')
plt.ylabel('Sine values', fontsize='medium', fontweight='medium')
plt.xlabel('x', fontsize='large', fontweight='medium')
plt.plot(x, y1, color='r', label='y1')
plt.legend()

# Subplot 2
plt.subplot(232)
plt.title('cosine function')
plt.xlabel('x', fontsize='large', fontweight='medium')
plt.ylabel('Cosine values', fontsize='medium', fontweight='medium')
plt.plot(x, y2, color='g', label='y2')
plt.legend()

# Subplot 3
plt.subplot(233)
plt.title('linear function')
plt.xlabel('x', fontsize='large', fontweight='medium')
plt.ylabel('y', fontsize='large', fontweight='medium')
plt.plot(x, y3, color='b', label='y3')
plt.legend()

# Subplot 4
plt.subplot(234)
plt.title('quadratic function')
plt.xlabel('x', fontsize='large', fontweight='medium')
plt.ylabel('y', fontsize='large', fontweight='medium')
plt.plot(x, y4, color='y', label='y4')
plt.legend()

# Subplot 5
plt.subplot(235)
plt.title('cubic function')
plt.xlabel('x', fontsize='large', fontweight='medium')
plt.ylabel('y', fontsize='large', fontweight='medium')
plt.plot(x, y5, color='c', label='y5')
plt.legend()

# Subplot 6
plt.subplot(236)
plt.title('tangential function')
plt.xlabel('x', fontsize='large', fontweight='medium')
plt.ylabel('y', fontsize='large', fontweight='medium')
plt.plot(x, y6, color='m', label='y6')
plt.legend()

# Adjust layout for better spacing
plt.tight_layout()
plt.savefig('Multiple Wave Plots.png')
plt.show()
