import numpy as np
from modulo import algoritmo_euclides, aee

"""
Funcion para calcular la matriz de cofactores
"""
def matriz_adjunta(A):
    n = A.shape[0]
    cofactores = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matriz_reducida = np.delete(np.delete(A, i, axis=0), j, axis=1) #devuelve una matriz sin la fila i y columna j
            cofactores[i, j] = round((-1) ** (i + j) * np.linalg.det(matriz_reducida))
    return cofactores.T

"""
Funcion para calcular la inversa de una matriz mediante su adjunta y determinante
"""

def inversa_matrix_mod(A, modN):
    det = round(np.linalg.det(A))
    if det == 0:
        return None

    adjunta = matriz_adjunta(A).astype(int)

    inversa_fracciones = []

    #Mostramos la inversa en forma de fracciones
    for i in range(A.shape[0]):
        fila = []
        for j in range(A.shape[1]):
            fila.append(f"{adjunta[i][j]}/{int(det)}")
        inversa_fracciones.append(fila)

    print("La matriz inversa es:")
    for fila in inversa_fracciones:
        print(fila)

    #Calculamos el inverso multiplicativo de det mod n
    gcd, x, y = aee(det % modN, modN)
    print(f"El inverso multiplicativo de {det} mod {modN} es: {x}")
    if gcd != 1:
        print(f"No existe inversa multiplicativa de {det} mod {modN}")
        return None
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            adjunta[i][j] = (adjunta[i][j] * x) % modN

    return adjunta   

A = np.array([list(map(int, input(f"Ingrese la fila {i} de la matriz A:").split())) for i in range(1,4)])
n = int(input("Ingrese el valor de mod n: "))
print(inversa_matrix_mod(A, n))
