def change(pennies):
    out = []
    out.append((pennies-(pennies%100))/100)
    pennies -= (pennies-(pennies%100))
    out.append((pennies-(pennies%25))/25)
    pennies -= (pennies-(pennies%25))
    out.append((pennies-(pennies%10))/10)
    pennies -= (pennies-(pennies%10))
    out.append((pennies-(pennies%5))/5)
    pennies -= (pennies-(pennies%5))
    out.append(pennies)
    for i in range(len(out)):
        out[i] = round(out[i])
    return tuple(out)

print( change(162) )
print( change(3) )