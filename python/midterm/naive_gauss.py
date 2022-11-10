# Declaration and Init
e = [0, 3, 5, 5, 1, 1]
f = [5, -4, -4, -1, -4, 2]
g = [7, 6, 2, 7, 1]
r = [9, 7, -10, -2, 9, -1]
x = [0] * len(r)
n = len(r)

# Decomposition
k = 1
while (k < n):
    e[k] /= f[k-1]
    f[k] -= e[k]*g[k-1]
    k += 1

print(e)
print(f)
print(g)


# Forward Substitution
k = 1
while (k < n):
    r[k] -= e[k]*r[k-1]
    k += 1

print(r)


# Back Substitution
x[n-1] = r[n-1]/f[n-1]
k = n - 2
while (k >= 0):
    x[k] = (r[k] - g[k] * x[k+1]) / f[k]
    k -= 1

print(x)