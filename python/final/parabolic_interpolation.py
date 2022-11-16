import math

# parameters
def f(x):
    return 2*x - 1.75*x**2 + 1.1*x**3 - 0.25*x**4

x0 = 1.75
x1 = 2
x2 = 2.25          # initail values

iter = 10


# algorithm
print("{0:<6}{1:<10}{2:<10}{3:<10}{4:<10}{5:<10}{6:<10}{7:<10}{8:<10}".format("iter", "x0", "f0", "x1", "f1", "x2", "f2", "x3", "f3"))

for i in range(1, iter+1):
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    x3 = (f0*(x1**2-x2**2) + f1*(x2**2-x0**2) + f2*(x0**2-x1**2))/(2*f0*(x1-x2) + 2*f1*(x2-x0) + 2*f2*(x0-x1))
    f3 = f(x3)

    print("{0:<6}{1:<10.4f}{2:<10.4f}{3:<10.4f}{4:<10.4f}{5:<10.4f}{6:<10.4f}{7:<10.4f}{8:<10.4f}".format(i, x0, f0, x1, f1, x2, f2, x3, f3))

    if (f3 > f1):
        x0 = x3
    else:
        x2 = x3

    xs = [x0, x1, x2]
    xs.sort()
    x0, x1, x2 = xs[0], xs[1], xs[2]