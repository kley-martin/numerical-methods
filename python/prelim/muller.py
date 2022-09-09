import math

# configs
max_iter = 10       # maximum iterations


# parameters
x0 = 4.5              # first 3 given points
x1 = 5.5
x2 = 5
ea_lim = .01        # approx error limit

def f(x):
    return x**3 - 13*x - 12


# algorithm
def far(target, *nums): # function for finding the farthest value from target
    farthest = 0
    for num in nums:
        if (farthest < abs(num-target)):
            farthest = num
    return farthest

h0, h1, d0, d1, a, b, c, x3, x3_old = (0,)*9
ea = 1

print("{0:<6}{1:<14}{2:<14}".format("iter", "X", "Ea"))

for i in range(1, max_iter+1):

    h0 = x1 - x0
    h1 = x2 - x1
    d0 = (f(x1) - f(x0))/(x1 - x0)
    d1 = (f(x2) - f(x1))/(x2 - x1)
    a = (d1 - d0)/(h1 + h0)
    b = a*h1 + d1
    c = f(x2)

    if (b > 0):
        x3 = x2 + (-2*c)/(b + math.sqrt(b**2 - 4*a*c))
    else:
        x3 = x2 + (-2*c) / (b - math.sqrt(b**2 - 4*a*c))

    if i > 1:
        ea = abs((x3 - x3_old)/x3)

    print("{0:<6}{1:<14.6f}{2:<14.6%}".format(i, x3, ea))

    if ea < ea_lim:
        break

    # prepare for next iteration
    temp = far(x3, x0, x1, x2)
    if (temp == x0):
        x0 = x3
    elif (temp == x1):
        x1 = x3
    else:
        x2 = x3
    x3_old = x3