# configs
max_iter = 20       # maximum iterations


# parameters
xl = 1              # lower bound
xu = 2              # upper bound
ea_lim = .01        # approx error limit

def f(x):
    return x**2 - x - 1


# validate and fix parameters
if f(xu)*f(xl) >= 0:
    print("Upper Xu and Lower Xl invalid. F(Xu) and F(Xl) should result in a positive and negative respectively.")
    print("F(Xl) = " + str(f(xl)))
    print("F(Xu) = " + str(f(xu)))

if f(xl) > f(xu):
    xl, xu = xu, xl
    print("Swapped Xu and Xl because <insert reason>")

# algorithm
xr = 0
xr_old = 0
ea = 1

print("{0:<6}{1:<14}{2:<14}{3:<14}{4:<14}{5:<14}{6:<14}{7:<14}".format("iter", "Xl", "F(Xl)", "Xu", "F(Xu)", "Xr", "F(Xr)", "Ea"))

for i in range(1, max_iter+1):
    xr_old = xr
    xr = xu -(f(xu)*(xu-xl))/(f(xu)-f(xl))
    
    if i > 1:
        ea = abs((xr - xr_old) / xr)

    print("{0:<6}{1:<14.6f}{2:<14.6f}{3:<14.6f}{4:<14.6f}{5:<14.6f}{6:<14.6f}{7:<14.6%}".format(i, xl, f(xl), xu, f(xu), xr, f(xr), ea))

    if f(xr) > 0:
        xu = xr
    elif f(xr) < 0:
        xl = xr
    else:
        break

    if ea < ea_lim:
        break