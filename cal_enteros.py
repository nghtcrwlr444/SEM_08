def mult(u, v):
    n = max(len(str(u)), len(str(v)))
    if n <= 1:
        return u * v

    s = n // 2
    pot = 10**s

    w = u // pot
    x = u % pot
    y = v // pot
    z = v % pot

    return mult(w, y) * 10**(2 * s) + (mult(w, z) + mult(x, y)) * pot + mult(x, z)


def main():
    u = int(input("Ingrese el primer número: "))
    v = int(input("Ingrese el segundo número: "))
    resultado = mult(u, v)
    print("El resultado es:", resultado)


main()