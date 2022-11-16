import math

# parameters
def f(x):
    return -1.5*x**6 - 2*x**4 + 12*x

xl = 0          # lower bound
xu = 2          # upper bound

iter = 10


# algorithm
print("{0:<6}{1:<10}{2:<10}{3:<10}{4:<10}{5:<10}{6:<10}{7:<10}".format("iter", "xl", "xu", "d", "x1", "x2", "f(x1)", "f(x2)"))

for i in range(1, iter+1):
    d = ((math.sqrt(5) - 1)/2) * (xu - xl)  # Golden Formula
    x1 = xl + d
    x2 = xu - d

    print("{0:<6}{1:<10.4f}{2:<10.4f}{3:<10.4f}{4:<10.4f}{5:<10.4f}{6:<10.4f}{7:<10.4f}".format(i, xl, xu, d, x1, x2, f(x1), f(x2)))
    
    if (f(x1) > f(x2)): # might cause error
        xl = x2
    else:
        xu = x1