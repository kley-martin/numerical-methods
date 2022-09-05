# configs
max_iter = 10       # maximum iterations


# parameters
x1 = 4              # initial X value
x2 = 3
ea_lim = .01        # approx error limit

def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5


# validate and fix parameters


# algorithm
x1_old = 0
ea = 1

print("{0:<6}{1:<14}{2:<14}".format("iter", "Xr", "Ea"))

for i in range(1, max_iter+1):
    x1_old = x1
    x1 = x1 - (f(x1)*(x2-x1))/(f(x2)-f(x1))
    x2 = x1_old

    if i > 1:
        ea = abs((x1 - x1_old) / x1)

    print("{0:<6}{1:<14.6f}{2:<14.6%}".format(i, x1, ea))

    if ea < ea_lim:
        break