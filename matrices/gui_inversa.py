import tkinter as tk
from tkinter import messagebox
import numpy as np
from modulo import aee # Importa el algoritmo euclides extendido[cite: 4, 5]

def matriz_adjunta(A):
    n = A.shape[0] #[cite: 4]
    cofactores = np.zeros((n, n)) #[cite: 4]
    for i in range(n): #[cite: 4]
        for j in range(n): #[cite: 4]
            matriz_reducida = np.delete(np.delete(A, i, axis=0), j, axis=1) #[cite: 4]
            cofactores[i, j] = round((-1) ** (i + j) * np.linalg.det(matriz_reducida)) #[cite: 4]
    return cofactores.T #[cite: 4]

def calcular_inversa():
    try:
        # Leer valores de la matriz A
        A = []
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append(int(entradas_A[i][j].get()))
            A.append(fila)
        A = np.array(A)

        n = int(entry_n.get())

        # Calculo de determinante y adjunta
        det = round(np.linalg.det(A)) #[cite: 4]
        texto_resultado.delete(1.0, tk.END)
        
        if det == 0: #[cite: 4]
            texto_resultado.insert(tk.END, "El determinante es 0. La matriz no tiene inversa.\n")
            return

        adjunta = matriz_adjunta(A).astype(int) #[cite: 4]

        # Mostrar inversa en fracciones[cite: 4]
        texto_resultado.insert(tk.END, f"Determinante de A: {det}\n\n")
        texto_resultado.insert(tk.END, "Inversa (en fracciones):\n")
        for i in range(A.shape[0]):
            fila_str = "   ".join([f"{adjunta[i][j]}/{int(det)}" for j in range(A.shape[1])])
            texto_resultado.insert(tk.END, fila_str + "\n")

        # Inverso multiplicativo de det mod N
        gcd, x, y = aee(det % n, n) #[cite: 4]
        texto_resultado.insert(tk.END, f"\nInverso multiplicativo de {det} mod {n} es: {x}\n") #[cite: 4]
        
        if gcd != 1: #[cite: 4]
            texto_resultado.insert(tk.END, f"No existe inversa multiplicativa de {det} mod {n}.\n") #[cite: 4]
            return
        
        # Calcular inversa modular[cite: 4]
        for i in range(A.shape[0]): #[cite: 4]
            for j in range(A.shape[1]): #[cite: 4]
                adjunta[i][j] = (adjunta[i][j] * x) % n #[cite: 4]

        texto_resultado.insert(tk.END, f"\nMatriz Inversa Definitiva mod {n}:\n")
        texto_resultado.insert(tk.END, str(adjunta)) #[cite: 4]

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa solo números enteros.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# --- Configuración de la GUI ---
root = tk.Tk()
root.title("Inversa de Matriz 3x3 (mod N)")
root.geometry("550x550")

frame_A = tk.LabelFrame(root, text="Introduce la Matriz A (3x3)", padx=10, pady=10)
frame_A.pack(pady=15)

entradas_A = []
for i in range(3):
    fila = []
    for j in range(3):
        e = tk.Entry(frame_A, width=6, justify='center', font=("Arial", 12))
        e.grid(row=i, column=j, padx=10, pady=10)
        e.insert(0, "0")
        fila.append(e)
    entradas_A.append(fila)

frame_medio = tk.Frame(root)
frame_medio.pack(pady=10)
tk.Label(frame_medio, text="Valor de mod n:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
entry_n = tk.Entry(frame_medio, width=10, font=("Arial", 12), justify='center')
entry_n.pack(side=tk.LEFT, padx=5)

btn_calcular = tk.Button(root, text="Calcular Inversa mod N", bg="#2196F3", fg="white", font=("Arial", 12, "bold"), command=calcular_inversa)
btn_calcular.pack(pady=10)

texto_resultado = tk.Text(root, height=14, width=50, font=("Courier", 11))
texto_resultado.pack(pady=10)

root.mainloop()