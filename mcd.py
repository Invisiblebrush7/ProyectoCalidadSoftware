''' Tarea de calidad de software '''

def mcd(x, y):
    ''' Calcula el máximo común divisor de dos números '''

    if x <= 0 or y <= 0:
        print("No deben ser negativos")
        return -1
    if(x == 1 or y == 1):
        return 1
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x

    print(x)
    return x
