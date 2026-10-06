def tamano(numero):
    """Devuelve la cantidad de cifras del número."""
    return len(str(numero))


def mult(u, v):
    n = max(tamano(u), tamano(v))

    if n <= 1:
        return u * v
    else:
        s = n // 2
        potencia = 10**s

        w = u // potencia
        x = u % potencia
        y = v // potencia
        z = v % potencia

        parte1 = mult(w, y) * (10 ** (2 * s))
        parte2 = (mult(w, z) + mult(x, y)) * potencia
        parte3 = mult(x, z)

        return parte1 + parte2 + parte3


print("=== MULTIPLICACIÓN DE ENTEROS GRANDES ===")

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado = mult(numero1, numero2)

print("\nEl resultado de la multiplicación es:")
print(resultado)