import numpy as np
import matplotlib.pyplot as plt

def inspiration(c):
	m = 1-c
	T = np.matrix([[m, 0, 0, 0, 0, 0, c], [m, 0, 0, 0, 0, 0, c], [0, m, 0, 0, 0, 0, c], [0, 0 , m , 0, 0, 0, c], [0, 0, 0, m, 0, 0, c], [0, 0, 0, 0, m, 0, c], [0, 0, 0, 0, 0, m, c]])
	Z = T**100
	uptime = Z[0,1] + Z[0,2] + Z[0,3] + Z[0,4] + Z[0,5] + Z[0,6]
	return uptime

uptime = []
for c in np.arange(0,0.35,0.01):
	uptime.append(inspiration(c))

plt.plot(uptime)
plt.grid()
plt.xlabel('crit %')
plt.ylabel('Inspiration uptime %')
plt.show()