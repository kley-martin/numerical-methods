import math

# parameters
x = [[16, 4, 28, 12],
     [4, 10, 13, 18],
     [28, 13, 54, 33], 
     [12, 18, 33, 42]] 


# algorithm
xl = len(x)
l = [ [0]*xl for i in range(xl)]

# decomposition
k = 0
while (k < xl):
    i = 0
    while (i <= k):
        if (k == i):
            sum = 0
            j = 0
            while (j < k):
                sum += l[k][j]**2
                j += 1
            l[k][k] = math.sqrt(x[k][k] - sum)
        else:
            sum = 0
            j = 0
            while (j < i):
                sum += l[i][j]*l[k][j]
                j += 1
            l[k][i] = (x[k][i] - sum) / l[i][i]
        i += 1
    k += 1

print(l)