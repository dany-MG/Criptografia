from Crypto.Cipher import DES

k = b'12345678'  # clave de 8 bytes
TAM_BLOQUE = 8   # tamaño de bloque de 8 bytes

try:
    with open('imagen_c.bmp', 'rb') as archivo:
        tipo_archivo = archivo.read(2)

        if tipo_archivo != b'BM':
            print("El archivo no es un BMP")
            exit(1)

        file_size = int.from_bytes(archivo.read(4), byteorder='little')
        reserved = int.from_bytes(archivo.read(4), byteorder='little')
        offset = int.from_bytes(archivo.read(4), byteorder='little')
        header_size = int.from_bytes(archivo.read(4), byteorder='little')
        width = int.from_bytes(archivo.read(4), byteorder='little')
        height = int.from_bytes(archivo.read(4), byteorder='little', signed=True)
        planes = int.from_bytes(archivo.read(2), byteorder='little')
        bits_per_pixel = int.from_bytes(archivo.read(2), byteorder='little')
        compression = int.from_bytes(archivo.read(4), byteorder='little')
        image_size = int.from_bytes(archivo.read(4), byteorder='little')
        x_pixel_por_meter = int.from_bytes(archivo.read(4), byteorder='little')
        y_pixel_por_meter = int.from_bytes(archivo.read(4), byteorder='little')
        colors_used = int.from_bytes(archivo.read(4), byteorder='little')
        colors_important = int.from_bytes(archivo.read(4), byteorder='little')

        # Volver al inicio para leer el archivo completo
        archivo.seek(0)
        data = archivo.read()

    header = data[:offset]   # no se cifra el header
    pixels = data[offset:]   # se cifra la parte de los pixeles

    # Recortar a un múltiplo de 8; el sobrante (0 a 7 bytes) queda sin cifrar
    limite = len(pixels) - (len(pixels) % TAM_BLOQUE)
    a_cifrar = pixels[:limite]
    sobrante = pixels[limite:]

    # Cifrado de todo el buffer de una sola vez
    cipher = DES.new(k, DES.MODE_ECB)
    descrifrado = cipher.decrypt(a_cifrar)

    # Guardar resultado en un nuevo archivo
    with open('imagen_d.bmp', 'wb') as archivo_cifrado:
        archivo_cifrado.write(header + descrifrado + sobrante)

    print("Imagen descrifrada correctamente y guardada como 'imagen_d.bmp'")

except Exception as e:
    print(f"Error al procesar la imagen: {e}")
    exit(1)