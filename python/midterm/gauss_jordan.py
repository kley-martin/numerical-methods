

# configs


# parameters
x = [[2, 1, -1, 1], 
     [5, 2, 2, -4], 
     [3, 1, 1, 5]]      # Coefficient w/ RHS Matrix


# algorithm
p = 0 # Pivot Index
r = 0 # Row Index
c = 0 # Column Index

while (p < len(x)):
    # Normalize Row
    c = 0
    d = x[p][p]
    while (c < len(x[0])):
        x[p][c] /= d
        c += 1

    # Eliminate Column
    r = 0
    while (r < len(x)):
        if (r == p):
            r += 1
            continue
        c = 0
        d = x[r][p]
        while (c < len(x[0])):
            x[r][c] -= d * x[p][c]
            c += 1
        r += 1
    p += 1

    print(x)
print(x)