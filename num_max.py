def main(x, y, z):
    if x > y and x > z :
        max_value = x
        max_variable = "x"
    elif z > y:
        max_value = z
        max_variable = "z"

    else:
        max_value = y
        max_variable = "y"
    
    print(f"El mÃ¡ximo valor es: {max_value}, contenido en la variable {max_variable}")
    return max_value