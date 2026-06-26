from random_walk import RandomWalk

import matplotlib.pyplot as plt

while True:
    rw = RandomWalk()
    rw.fill_work()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    ax.set_aspect('equal')

    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
                edgecolors='none', s=100)
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break