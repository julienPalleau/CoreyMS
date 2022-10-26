from scipy import arange, cos, exp
from scipy.optimize import fmin
import pylab


def f(x):
    return cos(x) - 3 * exp(-(x - 0.2) ** 2)


# find minima of f(x),
# # starting from 1.0 and 2.0 respectively
minimum1 = fmin(f, 1.0)
print("Start search at x=1., minimum is", minimum1)
minimum2 = fmin(f, 2.0)
print("Start search at x=2., minimum is", minimum2)


# plot function
x = arange(-10, 10, 0.1)
y = f(x)
pylab.plot(x, y, label="$cos(x)-3e ^ {-(x-0.2) ^ 2}$")
pylab.xlabel("x")
pylab.grid()
pylab.axis([-5, 5, -2.2, 0.5])

# add minimum1 to plot
pylab.plot(minimum1, f(minimum1), "vr", label="minimum 1")

# add start1 to plot
pylab.plot(1.0, f(1.0), "or", label="start 1")

# add minimum2 to plot
pylab.plot(minimum2, f(minimum2), "vg", label="minimum 2")

# add start2 to plot
pylab.plot(2.0, f(2.0), "og", label="start 2")

pylab.legend(loc="lower left")
pylab.savefig("fmin1.pdf")
pylab.show()
