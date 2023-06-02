import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    print(rw.x_values)
    print(rw.y_values)
    print(rw.z_values)
    # plt.scatter(0, 0, 0, c='green', edgecolors='none', s=10)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], rw.z_values[-1], c='red', edgecolors='none', s=10)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    fig = plt.figure(dpi=96, figsize=(15, 9))
    ax = Axes3D(fig)

    ax.plot(rw.x_values, rw.y_values, rw.z_values, linewidth=3)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_run = input("keep run the walk?(y/n)")
    if keep_run == 'n':
        break
    # plt.style.use('classic')
    # fig, ax = plt.subplots()
    # ax.scatter(rw.x_values, rw.y_values, s=15)
    # plt.show()
