import numpy as np
from matplotlib import pyplot as plt


def differential_equation(x: float, y: float) -> float:
    """
    Any differential equation
    Args:
        x (int): argument
        y (int): y argument
    Returns:
        float: equation output
    """
    return x + x * y + y + 1


def modified_euler_method(func: callable, start_x: float, start_y: float, min_x: float, max_x,
                          h: float) -> np.ndarray:
    """
    Modified euler method
    Args:
        func (callable): predefined differential equation function
        start_x (float): predefined x value
        start_y (float): predefined y value for start_x
        min_x (float): minimal x range value
        max_x (float): maximal x range value
        h: step jump
    Returns:
        np.ndarray: modified euler method calculated values
    """
    calculated_values = np.array([[start_x, start_y]])
    for i in np.arange(min_x + h, max_x + h, h):
        last_x = calculated_values[-1][0]
        last_y = calculated_values[-1][1]
        new_x = i;
        k1 = h * func(last_x, last_y)
        k2 = h * func(last_x + h, last_y + k1)
        new_y = last_y + 1 / 2 * (k1 + k2)
        new_values = np.array([[new_x, new_y]])
        calculated_values = np.concatenate((calculated_values, new_values))
    return calculated_values


# calculations
mem = modified_euler_method(differential_equation, -1., 1., -1., 1., 0.25)
print(mem)

# plot
x, y = mem.T
plt.plot(x, y)
plt.grid(color='gray', linestyle='-', linewidth=0.5)
plt.ylabel('x')
plt.xlabel('y')
plt.show()
