from numpy import *
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import mlab


def f(x):
    5 * sin(10 * x) * cos(3 * x)

    if x == 0:
        return 1.0
    return math.sin(10 * x) * cos(3 * x)


x_list = np.arange(0, 8)
y_list = [f(x) for x in x_list]

plt.plot(x_list, y_list, 'g^', label='5*sin(10*x)*cos(3*x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('My first plot')

plt.plot(y_list)
plt.show()