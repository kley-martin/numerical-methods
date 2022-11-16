# parameters
def f(x):
    return 2*x - 1.75*x**2 + 1.1*x**3 - 0.25*x**4

def fp(x):      # first derivative
    return 2 - 3.5*x + 3.3*x**2 - x**3

def fpp(x):     # second derivative
    return -3.50 + 6.6*x - 3*x**2

x = 2.5         # initial value

iter = 5


# algorithm
for i in range(1, iter+1):
    print(i, x)
    x = x - fp(x)/fpp(x)