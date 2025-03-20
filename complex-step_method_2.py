import numpy as np
import matplotlib.pyplot as plt


def complex_step_derivative(f, x, h=1e-200):
    """
    Compute the derivative of a real-valued function f at x using the complex-step method.

    Args:
        f: The function to differentiate.
        x: The point at which to evaluate the dericative.
        h: The small complex step size (default: 1e-200).

    Returns:
        The dericative of f at x.
    """
    return np.imag(f(x + h*1j))/h


# example usage
def my_function(x):
    return np.exp(x)/(np.cos(x)**3 + np.sin(x)**3)


def my_fun_deriv(x):
    return 2*x + np.cos(x)


x = 2.0
derivative = complex_step_derivative(my_function, x)
#print(derivative)

x = np.linspace(-np.pi/4, np.pi/2, 30)
#print(x)

plt.figure(1)
plt.plot(x, my_function(x))
plt.show()

#plt.figure(2)
#plt.plot(x, complex_step_derivative(my_function, x), 'o')
#plt.plot(x, my_fun_deriv(x), '--')
#plt.show()
