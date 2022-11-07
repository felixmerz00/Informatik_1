def add(n):
    return (lambda b:n+b)
    

print( add(3)(10) )
print( add(-5)(15) )