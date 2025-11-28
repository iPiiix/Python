#  Ejercicio 1: Leer un archivo CSV
import csv
with open("datos.csv", "r") as archivo:
    lector_csv = csv.reader(archivo)
    for fila in lector_csv:
        nombre, edad = fila
        print(f"Nombre: {nombre}, Edad: {edad}")

# Ejercicio 2: Escribir en un archivo CSV
with open("productos.csv", "w", newline='') as archivo:
    escritor_csv = csv.writer(archivo)
    escritor_csv.writerow(["Producto", "Precio"])
    escritor_csv.writerow(["Manzana", "0.50"])
    escritor_csv.writerow(["Banana", "0.30"])
    escritor_csv.writerow(["Cereza", "0.20"])

# Ejercicio 3: Leer un archivo JSON
import json
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
    for usuario in datos["usuarios"]:
        print(f"usuario: {usuario['usuario']}, activo: {usuario['activo']}, roles: {usuario['roles']}")
    print(datos)

# Ejercicio 4: Guardar datos en un archivo JSON
datos_a_guardar = {
    "empleados": [
        {"nombre": "Ana", "departamento": "Ventas"},
        {"nombre": "Luis", "departamento": "Marketing"},
        {"nombre": "Marta", "departamento": "IT"}
    ]
}
with open("salida.json", "w") as archivo:
    json.dump(datos_a_guardar, archivo, indent=4)

# Ejercicio 5: Listar arcvhivos en un directorio
import os
ruta_directorio = "Escritorio"
archivos = os.listdir(ruta_directorio)
print("Archivos en el directorio actual:")
for archivo in archivos:
    print(archivo)

# Ejercicio 6: Contar palabras en un archivo grande
with open("libro.txt", "r") as archivo:
    contenido = archivo.read()
    contador = contenido.count("Python")
    print(f"La palabra 'Python' aparece {contador} veces en el archivo.")

# Ejercicio 7: Copar un archivo binario
import shutil
shutil.copy("foto.jpg", "copia_foto.jpg")
print("Archivo copiado exitosamente.")

# Ejercicio 8: Comprimir un archivo en ZIP
import zipfile
with zipfile.ZipFile("archivo_comprimido.zip", "w") as archivo_zip:
    archivo_zip.write("saludo.txt") 
    archivo_zip.write("lineas.txt")
print("Archivos comprimidos exitosamente.")

# Ejercicio 9: Leer un archivo linea por linea y crea otro filtrado
with open("datos.txt", "r") as entrada:
    with open("datos_filtrados.txt", "w") as salida:
        for linea in entrada:
            if "ERROR" in linea:
                salida.write(linea)

# Ejercicio 10: Procesar un archivo grande sin cargarlo completo
with open("grande.txt", "r") as archivo:
    total_palabras = 0
    for linea in archivo:
        palabras = linea.split()
        total_palabras += len(palabras)
    print(f"El archivo tiene un total de {total_palabras} palabras.")

