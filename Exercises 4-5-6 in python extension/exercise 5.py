import matplotlib.pyplot as plt
import numpy as np

def plotting(func):
    def wrapper(*args, **kwargs):
        fig, ax = plt.subplots()
        x_values = np.linspace(0, 100, 1000)
        y_values = func(x_values, *args, **kwargs)
        ax.plot(x_values, y_values, color='k')
        plt.show()
    return wrapper

@plotting
def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

a=1
b=2
c=3

quadratic(a,b,c)
