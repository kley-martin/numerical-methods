# from math import sqrt

# configs
max_iter = 10       # maximum iterations


# parameters
xr = 1              # initial X value
ea_lim = .01        # approx error limit

def f(x):
    return x**2 - 13*x

def fp(x):           # first derivative of function
    return 2*x - 13


# validate and fix parameters


# algorithm
xr_old = 0
ea = 1

print("{0:<6}{1:<14}{2:<14}".format("iter", "Xr", "Ea"))

for i in range(1, max_iter+1):
    xr_old = xr
    print(xr)
    print(f(xr))
    print(fp(xr))
    print(f(xr)/fp(xr))
    xr = xr - f(xr)/fp(xr)

    if i > 1:
        ea = abs((xr - xr_old) / xr)

    print("{0:<6}{1:<14.6f}{2:<14.6%}".format(i, xr, ea))

    if ea < ea_lim:
        break