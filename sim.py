import numpy as np
import matplotlib.pyplot as plt

# Units: Astronomical units for distance and years for time
G = 1
M = 4 * np.pi**2
dt = 0.001        
steps = 200000    

names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
a = np.array([0.387, 0.723, 1.000, 1.524, 5.203, 9.537, 19.19, 30.07])         
e = np.array([0.2056, 0.0068, 0.0167, 0.0934, 0.0484, 0.0539, 0.0473, 0.0086])

r_peri = a * (1 - e)
v_peri = np.sqrt(G * M * (1 + e) / r_peri)
pos = np.column_stack((r_peri, np.zeros(len(a))))
vel = np.column_stack((np.zeros(len(a)), v_peri))

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

plt.plot(0, 0, "yo")
for i in range(len(pos)):
    plt.plot(history[:, i, 0], history[:, i, 1], label=names[i])
plt.axis("equal")
plt.legend()
plt.show()