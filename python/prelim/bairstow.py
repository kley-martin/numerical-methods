import math

# configs
max_iter = 20       # maximum iterations


# parameters
r = 1             # first init  guess
s = -1.5             # Second init guess
ea_lim = .01        # approx error limit

def f(x):
    return 2*x**4 + 3*x**3 + 17*x**2 - 2*x + 24


# algorithm
a = [5, -2, 6, -2, 1]
b, c = [0] * (len(a)+2), [0] * (len(a)+2)
ds, dr, ear, eas = 0, 0, 0, 0
ea = 1

print("{0:<6}{1:<14}{2:<14}{3:<14}{4:<14}".format("iter", "r", "s", "Ea.r", "Ea.s"))
print("{0:<6}{1:<14.6f}{2:<14.6f}{3:<14}{4:<14}".format(0, r, s, "~", "~"))

for iter in range(1, max_iter+1):
    # calculate 'b' and 'c'
    i = len(a)-1
    while (i >= 0):
        b[i] = a[i] + r*b[i+1] + s*b[i+2]
        c[i] = b[i] + r*c[i+1] + s*c[i+2]
        i -= 1

    # calculate Δr and Δs
    dr = (c[3]*b[0] - b[1]*c[2])/(c[2]**2 - c[1]*c[3]) # Behold, an equation that I derived myself
    ds = (-b[0] - c[1]*dr)/c[2]

    # calculate Estimated Error 
    ear = abs(dr/r)
    eas = abs(ds/s)

    print("{0:<6}{1:<14.6f}{2:<14.6f}{3:<14.6%}{4:<14.6%}".format(iter, r+dr, s+ds, ear, eas))

    # check stopping criterion
    if ((ear < ea_lim and eas < ea_lim)):
        break

    # prepare for next iteration
    r += dr
    s += ds