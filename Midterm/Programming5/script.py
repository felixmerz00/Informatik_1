def duplicate_every(l, n):
    out = []
    for i in range(len(l)):
        out.append(l[i])
        if((i+1)%n == 0):
            out.append(l[i])
    return out

print( duplicate_every([1, 3, 4, 5], 2) )
print( duplicate_every([1, 4, 5, 4, 3, 2, 1], 3) )