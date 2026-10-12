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
