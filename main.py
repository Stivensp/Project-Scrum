import json, os
ruta = "database.json"
actualUser = None

loginMenu = """

    Biembenido al menu de usuario. 👤

    1. 🔒 Iniciar Sesion
    2. 🔑 Registrarse
    3. ❌ Salir

"""

userMenu = """
    
    
    █▀▀ █▀█ █▀▄ █▀▀ █▀▀
    █▄▄ █▄█ █▄▀ ██▄ █▄▄

    1. 📃 Listado de Usuarios
    2. ❌ Cerrar Sesion
    3. 📝 Crear Publicación
    4. Ver pulicaciones
    

"""

#FUNCIONES DE GUI

def printe(msg):
    print(f"----------------------------------------------------------------\n {msg} \n----------------------------------------------------------------")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNCIONES DE CARGAR Y DESCARGAR JSON

def setJson(data):
    global ruta
    try:
        with open(ruta, "w") as file:
            json.dump(data, file, indent=2)
    except Exception as e:
        print(e)
        return

def getJson():
    global ruta
    try:
        with open(ruta, "r") as file:
            data = json.load(file)
    except Exception as e:
        print(e)
        data = []
        setJson([])
    return data

# FUNCIONES DE REGISTRO E INICIO DE SESION DE USUARIOS

def setId():
    idd = 0
    data = getJson()
    for i in data:
        if i["id"] == idd:
            idd += 1
        else:
            idd = idd
            break
    return idd

def register():
    clearConsole()
    data = getJson()
    print("🔑 Registrarse")
    if data == []:
        user = input("Ingresa tu nombre de Usuario: ")
        if user == "":
            printe("❌ El usuario no puede estar vacio.")
            input("Continuar...")
            return
        elif user.count(" "):
            printe("❌ El Usuario no puede contener espacios.")
            input("Continuar...")
            return
        
        password = input("Ingresa tu contraseña: ")
        if password == "":
            printe("❌ La contraseña no puede estar vacio.")
            input("Continuar...")
            return
        elif password.count(" ") > 0:
            printe("❌ La contraseña no puede contener espacios.")
            input("Continuar...")
            return
        elif len(password) < 4:
            printe("❌ La contraseña debe contener 4 caracteres.")
            input("Continuar...")
            return
        else:
            data.append({"id": 0, "user": user, "password": password, "post": []})
            setJson(data)
            printe("✅ Usuario creado correctamente.")
            input("Continuar...")
    else:
        user = input("Ingresa tu nombre de Usuario: ")
        if user == "":
            printe("❌ El usuario no puede estar vacio.")
            input("Continuar...")
            return
        elif user.count(" ") > 0:
            printe("❌ El usuario no puede contener espacios.")
            input("Continuar...")
            return
        elif any(u["user"] == user for u in data):
            printe("❌ El nombre de Usuario ya existe, elige otro.")
            input("Continuar...")
            return
        
        password = input("Ingresa tu contraseña: ")
        if password == "":
            printe("❌ La contraseña no puede estar vacia.")
            input("Continuar...")
            return
        elif password.count(" ") > 0:
            printe("❌ La contraseña no puede contener espacios.")
            input("Continuar...")
            return
        elif len(password) < 4:
            printe("❌ La contraseña debe contener 4 caracteres.")
            input("Continuar...")
            return
        else:
            data.append({"id": setId(),"user": user, "password": password, "post": []})
            setJson(data)
            printe("✅ Usuario creado correctamente.")
            input("Continuar...")

def login():
    clearConsole()
    print("🔒 Iniciar sesion")
    global actualUser
    data = getJson()
    if data == []:
        printe("❔ No hay cuentas existentes.")
        input("Continuar...")
        return
    user = input("Ingresa tu nombre de usuario: ")
    if user == "":
        printe("❌ El usuario no puede estar vacio.")
        input("Continuar...")
        return
    if any(u["user"] == user for u in data):
        print("Usuario encontrado.")
    else:
        printe("❌ El usuario ingresado no existe.")
        input("Continuar...")
        return
    
    for u in data:
        if u["user"] == user:
            id = u["id"]

    password = input("Ingresa tu contraseña: ")
    if password == "":
        printe("❌ La contraseña no puede estar vacia.")
        input("Continuar...")
        return
    if data[id]["password"] != password:
        printe("❌ La contraseña no coincide.")
        input("Continuar...")
        return

    actualUser = id
    printe("✅ Usuario iniciado correctamente")
    input("Continuar...")
    viewUserMenu()

def viewLogMenu():
    while True:
        clearConsole()
        print(loginMenu)
        op = input("Ingrese una opcion: ")
        if op == "1":
            login()
        elif op == "2":
            register()
        elif op == "3":
            clearConsole()
            printe("\n\n     👋 Goodbye! \n\n")
            break
        else:
            printe("Invalid option, please try again.")

# FUNCIONES DE LISTADO DE USUARIOS

def listarUsers():
    clearConsole()
    data = getJson()
    print("📃 Listado de Usuarios")
    print("------------------------")
    for i in data:
        print(f"    🗿 - {i['user'] }")
        print("------------------------")
    input("Volver...")

# FUNCIONES DE PUBLICACIONES

def cargar_datos():
    """Carga los datos existentes del archivo JSON."""
    if os.path.exists(ruta):
        with open(ruta, "r") as file:
            return json.load(file)
    return []

def guardar_datos(data):
    """Guarda los datos en el archivo JSON."""
    with open(ruta, "w") as file:
        json.dump(data, file, indent=2)

def crear_publicacion():
    """
    Crea una nueva publicación para el usuario logueado.
    """
    global actualUser
    if actualUser is None:
        printe("❌ No hay un usuario logueado.")
        input("Continuar...")
        return

    data = getJson()
    usuario = next((u for u in data if u["id"] == actualUser), None)

    if not usuario:
        printe("❌ Usuario no encontrado.")
        input("Continuar...")
        return
    clearConsole()
    print("📝 Crear Publicación")
    titulo = input("Ingrese el título de la publicación: ")
    if not titulo.strip():
        printe("❌ El título no puede estar vacío.")
        input("Continuar...")
        return

    contenido = input("Ingrese el contenido de la publicación: ")
    if not contenido.strip():
        printe("❌ El contenido no puede estar vacío.")
        input("Continuar...")
        return

    publicacion = {
        "titulo": titulo,
        "contenido": contenido
    }

    usuario["post"].append(publicacion)
    guardar_datos(data)
    printe(f"✅ Publicación creada exitosamente para el usuario '{usuario['user']}'.")

def ver_publicaciones():
    """
    Muestra la lista de usuarios, permite buscar un usuario, y muestra sus publicaciones.
    Permite seleccionar una publicación por título para ver su contenido.
    """
    clearConsole()
    data = getJson()
    print("📃 Ver Publicaciones")
    print("------------------------")
    
    # Mostrar lista de usuarios
    for i in data:
        print(f"    🗿 - {i['user']}")
        print("------------------------")
    
    # Buscar usuario
    usuario_buscado = input("Ingrese el nombre del usuario a buscar: ").strip()
    usuario = next((u for u in data if u["user"] == usuario_buscado), None)

    if usuario:
        clearConsole()
        print(f"👤 Perfil del usuario: {usuario['user']}")
        print("------------------------")
        
        # Mostrar títulos de publicaciones
        if usuario["post"]:
            print("📄 Publicaciones disponibles:")
            for idx, post in enumerate(usuario["post"], start=1):
                print(f"  {idx}. 📝 Título: {post['titulo']}")
            print("------------------------")
            
            # Seleccionar publicación por título
            titulo_buscado = input("Ingrese el título de la publicación que desea ver: ").strip()
            publicacion = next((p for p in usuario["post"] if p["titulo"] == titulo_buscado), None)
            
            if publicacion:
                clearConsole()
                print(f"📝 Publicación seleccionada:")
                print(f"  Título: {publicacion['titulo']}")
                print(f"  Contenido: {publicacion['contenido']}")
            else:
                printe("❌ No se encontró una publicación con ese título.")
        else:
            printe("❔ Este usuario no tiene publicaciones.")
    else:
        printe("❌ Usuario no encontrado.")
    
    input("Presione Enter para continuar...")

def viewUserMenu():
    while True:
        clearConsole()
        print(userMenu)
        op = input("Ingrese una opcion: ")
        if op == "1":
            listarUsers()
        elif op == "2":
            clearConsole()
            printe("\n\n     👋 Goodbye! \n\n")
            break
        elif op == "3":
            crear_publicacion()  # Llamar a la nueva función
        elif op == "4":
            ver_publicaciones()
        else:
            printe("Invalid option, please try again.")


viewLogMenu()