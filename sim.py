import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1
M = 1000
dt = 1
steps = 2000

pos = np.array([[100.0, 0.0], [-70,70]])   # one row per body
vel = np.array([[0.0, 4], [0,4]])

def accel(pos):
    x = pos[:, 0]
    y = pos[:, 1]
    r = np.sqrt(x**2 + y**2)
    ax = -G * M * x / r**3
    ay = -G * M * y / r**3
    return np.column_stack((ax, ay))

acc = accel(pos)
history = []

for _ in range(steps):
    pos = pos + vel * dt + 0.5 * acc * dt**2
    new_acc = accel(pos)
    vel = vel + 0.5 * (acc + new_acc) * dt
    acc = new_acc
    history.append(pos)

history = np.array(history)

plt.plot(0, 0, "yo", markersize=12)
for i in range(len(pos)):
    plt.plot(history[:, i, 0], history[:, i, 1])
plt.axis("equal")
plt.show()