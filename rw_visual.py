from random_walk import RandomWalk

import matplotlib.pyplot as plt

rw = RandomWalk()
rw.fill_work()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
plt.show()