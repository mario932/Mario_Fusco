import numpy as np
#import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt

n = 25

theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
c, a = 2, 1
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

# Plot 1 one color
fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax1.set_zlim(-3,3)
ax1.view_init(36, 26)
ax1.plot_wireframe(x, y, z, color="orange")
ax1.set_title('One color')

# Plot 2 Gradient Color
ax2 = fig.add_subplot(132, projection='3d')
ax2.set_zlim(-3,3)
ax2.view_init(36, 26)
ax2.plot_surface(x, y, z, cmap='viridis')
ax2.set_title('Gradient Color')

# Style 3: Transparency
ax3 = fig.add_subplot(133, projection='3d')
ax3.set_zlim(-3,3)
ax3.view_init(36, 26)
ax3.plot_surface(x, y, z, color='violet', alpha=0.5)
ax3.set_title('Transparency')

plt.tight_layout()
plt.savefig('Torus.png')
plt.show()