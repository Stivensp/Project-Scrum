import json
import os

JSON_FILE = "crear.json"

def cargar_datos():
    """Carga los datos existentes del archivo JSON."""
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    return {}

def guardar_datos(data):
    """Guarda los datos en el archivo JSON."""
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

def crear_publicacion(usuario, titulo, contenido):
    """
    Crea una nueva publicación para el usuario logueado.

    Args:
        usuario (str): Nombre del usuario logueado.
        titulo (str): Título de la publicación.
        contenido (str): Contenido de la publicación.
    """
    datos = cargar_datos()

    if usuario not in datos:
        datos[usuario] = []

    publicacion = {
        "titulo": titulo,
        "contenido": contenido
    }

    datos[usuario].append(publicacion)

    guardar_datos(datos)
    print(f"Publicación creada exitosamente para el usuario '{usuario}'.")

def menu_principal():
    """Muestra el menú principal y permite al usuario seleccionar una opción."""
    while True:
        print("\n--- Menú Principal ---")
        print("1. Crear una nueva publicación")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario_logueado = input("Ingrese el nombre del usuario logueado: ")
            titulo = input("Ingrese el título de la publicación: ")
            contenido = input("Ingrese el contenido de la publicación: ")
            crear_publicacion(usuario_logueado, titulo, contenido)
        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()