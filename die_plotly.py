#
import matplotlib.pyplot as plt
from die import Die

die = Die()
values = list(die.roll() for i in range(1000))
x_values = list(range(1, 1001))

plt.title('one D6 dice for 1000 times', fontsize=20)
plt.xlabel('Values')
plt.ylabel('Frequency of rolling one D6 1000 times.')
plt.plot(x_values, values, c='red', linewidth=3)
plt.show()