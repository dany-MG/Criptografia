import tkinter as tk
from tkinter import messagebox
import numpy as np

def calcular_producto():
    try:
        # Leer valores de la matriz A
        A = []
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append(int(entradas_A[i][j].get()))
            A.append(fila)
        A = np.array(A)

        # Leer valores de la matriz B
        B = []
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append(int(entradas_B[i][j].get()))
            B.append(fila)
        B = np.array(B)

        # Leer mod n
        n = int(entry_n.get())

        # Producto de matrices y aplicacion del modulo
        C = np.linalg.matmul(A, B) #[cite: 6]
        C_mod = C % n #[cite: 6]

        # Mostrar resultado
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, f"Matriz Resultante (A x B) mod {n}:\n\n")
        texto_resultado.insert(tk.END, str(C_mod))

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa solo números enteros.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")

# --- Configuración de la GUI ---
root = tk.Tk()
root.title("Producto de Matrices 3x3 (mod n)")
root.geometry("600x450")

frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

# Matriz A
frame_A = tk.LabelFrame(frame_superior, text="Matriz A", padx=10, pady=10)
frame_A.pack(side=tk.LEFT, padx=20)
entradas_A = []
for i in range(3):
    fila = []
    for j in range(3):
        e = tk.Entry(frame_A, width=5, justify='center', font=("Arial", 12))
        e.grid(row=i, column=j, padx=5, pady=5)
        e.insert(0, "0")
        fila.append(e)
    entradas_A.append(fila)

# Matriz B
frame_B = tk.LabelFrame(frame_superior, text="Matriz B", padx=10, pady=10)
frame_B.pack(side=tk.LEFT, padx=20)
entradas_B = []
for i in range(3):
    fila = []
    for j in range(3):
        e = tk.Entry(frame_B, width=5, justify='center', font=("Arial", 12))
        e.grid(row=i, column=j, padx=5, pady=5)
        e.insert(0, "0")
        fila.append(e)
    entradas_B.append(fila)

# Módulo y Botón
frame_medio = tk.Frame(root)
frame_medio.pack(pady=10)
tk.Label(frame_medio, text="Valor de mod n:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
entry_n = tk.Entry(frame_medio, width=10, font=("Arial", 12), justify='center')
entry_n.pack(side=tk.LEFT, padx=5)

btn_calcular = tk.Button(root, text="Calcular Producto", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), command=calcular_producto)
btn_calcular.pack(pady=10)

# Resultado
texto_resultado = tk.Text(root, height=8, width=40, font=("Courier", 12))
texto_resultado.pack(pady=10)

root.mainloop()