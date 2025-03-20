import numpy as np
import matplotlib.pyplot as plt


def csderiv(func, x, h=1e-8):
    return np.imag(func(x + 1j*h))/h


def f(x):
    return np.exp(x)/((np.cos(x))**3 + (np.sin(x))**3)


def fprime(x):
    """ Analytic derivative of e^x/(cos(x))^3 + (sin(x))^3)"""
    den = (np.cos(x))**3 + (np.sin(x))**3
    num = np.exp(x)*(den + 3*np.cos(x)*np.sin(x)*(np.cos(x) - np.sin(x)))
    return num/(den*den)


x = np.linspace(-3.9*np.pi/16, np.pi/2, 100)
dfdx = csderiv(f, x)
y, dy, exact = f(x), dfdx, fprime(x)
#y, dy, exact = [np.array([y(xval) for xval in x]) for y in (f, dfdx, fprime)]
error = dy - exact
print(error)

fig, ax = plt.subplots()
ax.plot(x, y, lw=1.5, label="$f(x)$")
ax.plot(x, dy, lw=2.5, alpha=0.8, label="$f'(x)$: complex step")
ax.plot(x, exact, "k--", lw=1, label="$f'(x)$: exact")
ax.legend()
ax.set_ylim([-5, 5])
ax.set_xticks([-np.pi/4, 0, np.pi/4, np.pi/2])
ax.set_xticklabels(("-$\pi$/4", "0", "$\pi$/4", "$\pi$/2"))
ax.grid(True)
plt.show()
