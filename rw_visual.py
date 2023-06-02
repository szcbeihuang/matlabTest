import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    print(rw.x_values)
    print(rw.y_values)
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.figure(dpi=96, figsize=(10, 6))
    plt.plot(rw.x_values, rw.y_values, linewidth=3)
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
