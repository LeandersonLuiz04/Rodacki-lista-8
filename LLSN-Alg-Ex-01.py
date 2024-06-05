def fatorial(f):
    total, contador=1 , 1
    while contador<=f:
        total, contador=total*contador, contador+1
    return total
print(fatorial(4))