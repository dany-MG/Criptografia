import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import DES
import os
from PIL import Image, ImageTk

TAM_BLOQUE = 8  # tamaño de bloque de 8 bytes

def procesar_imagen(ruta_entrada, ruta_salida, clave, modo):
    try:
        if len(clave) != 8:
            messagebox.showerror("Error", "La clave debe tener exactamente 8 caracteres (bytes).")
            return False

        k = clave.encode('utf-8')

        with open(ruta_entrada, 'rb') as archivo:
            tipo_archivo = archivo.read(2)
            if tipo_archivo != b'BM':
                messagebox.showerror("Error", "El archivo no es un BMP válido.")
                return False

            archivo.seek(10)
            offset = int.from_bytes(archivo.read(4), byteorder='little')

            archivo.seek(0)
            data = archivo.read()

        header = data[:offset]
        pixels = data[offset:]

        limite = len(pixels) - (len(pixels) % TAM_BLOQUE)
        a_procesar = pixels[:limite]
        sobrante = pixels[limite:]

        cipher = DES.new(k, DES.MODE_ECB)

        if modo == 'cifrar':
            resultado = cipher.encrypt(a_procesar)
        else:
            resultado = cipher.decrypt(a_procesar)

        with open(ruta_salida, 'wb') as archivo_salida:
            archivo_salida.write(header + resultado + sobrante)

        messagebox.showinfo("Éxito", f"Imagen guardada como:\n{ruta_salida}")
        return True

    except Exception as e:
        messagebox.showerror("Error al procesar", f"Ocurrió un error: {e}")
        return False

def mostrar_imagen(ruta, label_widget):
    """Carga y redimensiona la imagen para que quepa en la GUI"""
    try:
        img = Image.open(ruta)
        img.thumbnail((300, 300))  # Ajusta el tamaño máximo de previsualización
        img_tk = ImageTk.PhotoImage(img)
        label_widget.config(image=img_tk)
        label_widget.image = img_tk  # Se guarda la referencia para que no se borre de memoria
    except Exception as e:
        print(f"Error al cargar la imagen en la GUI: {e}")

def seleccionar_y_cifrar():
    ruta_entrada = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
    if not ruta_entrada: return
    
    mostrar_imagen(ruta_entrada, lbl_img_orig)
    lbl_titulo_orig.config(text="Imagen Original")
    
    ruta_salida = os.path.splitext(ruta_entrada)[0] + "_c.bmp"
    if procesar_imagen(ruta_entrada, ruta_salida, entry_clave.get(), 'cifrar'):
        mostrar_imagen(ruta_salida, lbl_img_res)
        lbl_titulo_res.config(text="Imagen Cifrada")

def seleccionar_y_descifrar():
    ruta_entrada = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])
    if not ruta_entrada: return
    
    mostrar_imagen(ruta_entrada, lbl_img_orig)
    lbl_titulo_orig.config(text="Imagen Cifrada (Original)")
    
    ruta_salida = os.path.splitext(ruta_entrada)[0] + "_d.bmp"
    if procesar_imagen(ruta_entrada, ruta_salida, entry_clave.get(), 'descifrar'):
        mostrar_imagen(ruta_salida, lbl_img_res)
        lbl_titulo_res.config(text="Imagen Descifrada")

# --- Configuración de la Ventana Principal ---
root = tk.Tk()
root.title("Cifrado/Descifrado DES ECB con Vista Previa")
root.geometry("750x550") # Aumenté ligeramente el tamaño de la ventana inicial

# Controles superiores
frame_controles = tk.Frame(root)
frame_controles.pack(pady=15)

tk.Label(frame_controles, text="Clave DES (8 caracteres):", font=("Arial", 10)).grid(row=0, column=0, padx=5)
entry_clave = tk.Entry(frame_controles, font=("Arial", 12), justify='center')
entry_clave.insert(0, "12345678")
entry_clave.grid(row=0, column=1, padx=5)

btn_cifrar = tk.Button(frame_controles, text="Cifrar BMP", bg="#4CAF50", fg="white", command=seleccionar_y_cifrar)
btn_cifrar.grid(row=0, column=2, padx=10)

btn_descifrar = tk.Button(frame_controles, text="Descifrar BMP", bg="#2196F3", fg="white", command=seleccionar_y_descifrar)
btn_descifrar.grid(row=0, column=3, padx=10)

# Contenedor para las imágenes
frame_imagenes = tk.Frame(root)
frame_imagenes.pack(fill=tk.BOTH, expand=True, pady=10)

# Panel izquierdo (Imagen de entrada)
frame_izq = tk.Frame(frame_imagenes)
frame_izq.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
lbl_titulo_orig = tk.Label(frame_izq, text="Imagen Original", font=("Arial", 10, "bold"))
lbl_titulo_orig.pack()
# Se quitaron los atributos width=40 y height=20 para que la imagen se autoajuste
lbl_img_orig = tk.Label(frame_izq, bg="gray")
lbl_img_orig.pack(padx=10, pady=5)

# Panel derecho (Imagen de salida)
frame_der = tk.Frame(frame_imagenes)
frame_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
lbl_titulo_res = tk.Label(frame_der, text="Resultado", font=("Arial", 10, "bold"))
lbl_titulo_res.pack()
# Se quitaron los atributos width=40 y height=20
lbl_img_res = tk.Label(frame_der, bg="gray")
lbl_img_res.pack(padx=10, pady=5)

root.mainloop()