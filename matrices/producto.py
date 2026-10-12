import numpy as np
from modulo import algoritmo_euclides, aee

def producto_matrices(A, B):
    return np.linalg.matmul(A,B)

A = np.array([list(map(int, input(f"Ingrese la fila {i} de la matriz A:").split())) for i in range(1, 4)])
print(A)

B = np.array([list(map(int, input(f"Ingrese la fila {i} de la matriz B:").split())) for i in range(1, 4)])
print(B)

try:
    C = producto_matrices(A, B)
    print(C)
except Exception as e:
    print(f"Error al multiplicar las matrices: {e}")

n = int(input("Ingrese el valor de mod n: "))

for i in range(3):
    for j in range(3):
        C[i][j] = C[i][j] % n

print(C)

# TO DO: Implementar la aceptacion de elementos racionales en las matrices y la conversion a enteros mod n
