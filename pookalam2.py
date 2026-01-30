import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)

for r, c in zip([1, 2, 3, 4], ['red', 'orange', 'yellow', 'green']):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.fill(x, y, c)

plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
