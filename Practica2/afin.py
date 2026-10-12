"""
Usando algoritmo de euclides para encontrar gcd(alpha, n)
"""
def algoritmo_euclides(a,b):
    while b != 0:
        a, b = b, a % b
    return a

"""
Usando algoritmo de euclides extendido para encontrar el inverso multiplicativo de alpha mod n
    Args:
        a: el valor de alpha
        b: el valor de n
    Returns:
        gcd: el máximo común divisor de a y b
        x: el coeficiente de a en la combinación lineal
        y: el coeficiente de b en la combinación lineal
"""

def aee(a,b):
    if b == 0:
        return 0, 1, 0
    
    x0 = 1
    y0 = 0
    x1 = 0
    y1 = 1
    
    while b != 0:
        c = a // b # cociente
        r = a - b * c # residuo
        x = x0 - c * x1
        y = y0 - c * y1
        
        #Actualizamos los valores
        a = b
        b = r
        x0 = x1
        y0 = y1
        x1 = x
        y1 = y
    return a, x0, y0

print("Ingresa los valores de n, alpha y beta separados por comas:")
values = input().split(',')
n = int(values[0])
alpha = int(values[1])
beta = int(values[2])

if beta >= n or beta < 1:
    print("Error: beta debe de estar entre 1 y n")

"""alpha y n deben de ser coprimos, gcd(alpha, n) = 1"""
if algoritmo_euclides(alpha, n) != 1:
    print("Error: alpha y n no son coprimos, gcd(alpha, n) != 1")

"""Encontrar el inverso multiplicativo de alpha mod n"""
gcd, x, y = aee(alpha, n)
if x < 0:
    x = x + n
if gcd != 1:
    print("Error: No existe el inverso multiplicativo de alpha mod n")
    exit()
else:
    print(f"MCD = {gcd}, x = {x}, y = {y}")

print(f"Funcion de cifrado: C = {alpha}p + {beta} mod {n}")
print(f"Funcion de descifrado:")
print(f"\tDK1: p = {x}[ C + {n-(beta%n)} ] mod {n}")
print(f"\tDK2: p = {x}C + {n - (x*beta)%n} mod {n}\n")








