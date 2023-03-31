import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.5, 1.5, 300)  

y1 = np.sin(np.exp(2*x))
y2 = np.cos(np.exp(-2*x))

plt.plot(x, y1, color = 'k', linestyle = '--', label = 'Sin(e^2x)')
plt.plot(x, y2, color = 'b', linestyle = ':', label = 'Cos(e^-2x)')

plt.grid()

plt.xlabel('X Values')
plt.ylabel('Y Values')

plt.title('Trig Graphs')

plt.legend()

plt.text(0, .25, 'Sin(e^2x)')
plt.text(0, .10, 'Cos(e^-2x)')


fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1,)


ax1.plot(x, y1, color = 'r', linestyle = '-.', label = 'Sin(e^2x)')
ax2.plot(x, y2, color = 'g', label = 'Cos(e^-2x)')

ax1.set_title('Trig Graphs')
ax2.set_title('Trig Graphs')

ax1.set_xlabel('X')
ax1.set_ylabel('Y')

ax2.set_xlabel('X')
ax2.set_ylabel('Y')

ax1.legend()
ax2.legend()

ax1.grid()
ax2.grid()

ax1.text(0, .25, 'Sin(e^2x)')
ax2.text(0, .10, 'Cos(e^-2x)')

plt.tight_layout()
plt.show()