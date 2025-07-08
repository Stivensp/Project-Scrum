import json, os

ruta = "database.json"
actualUser = None

loginMenu = """
    Bienvenido al menú de usuario 👤

    1. 🔒 Iniciar Sesión
    2. 🔑 Registrarse
    3. ❌ Salir
"""

userMenu = """
    █▀▀ █▀█ █▀▄ █▀▀ █▀▀
    █▄▄ █▄█ █▄▀ ██▄ █▄▄

    1. 📃 Listado de Usuarios
    2. ❌ Cerrar Sesión
    3. 📝 Crear Publicación
    4. 📖 Ver Publicaciones
    5. ❤️  Dar Like a Publicación
    6. 💬 Comentar Publicación
"""

# UTILS
def printe(msg):
    print(f"----------------------------------------------------------------\n {msg} \n----------------------------------------------------------------")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# JSON FUNCTIONS
def setJson(data):
    with open(ruta, "w") as file:
        json.dump(data, file, indent=2)

def getJson():
    try:
        with open(ruta, "r") as file:
            return json.load(file)
    except:
        setJson([])
        return []

# USER FUNCTIONS
def setId():
    data = getJson()
    ids = [u["id"] for u in data]
    i = 0
    while i in ids:
        i += 1
    return i

def register():
    clearConsole()
    data = getJson()
    print("🔑 Registrarse")

    user = input("Ingresa tu nombre de Usuario: ").strip()
    if not user:
        printe("❌ El usuario no puede estar vacío.")
        input("Continuar...")
        return
    if " " in user:
        printe("❌ El usuario no puede contener espacios.")
        input("Continuar...")
        return
    if any(u["user"] == user for u in data):
        printe("❌ El usuario ya existe.")
        input("Continuar...")
        return

    password = input("Ingresa tu contraseña: ").strip()
    if not password:
        printe("❌ La contraseña no puede estar vacía.")
        input("Continuar...")
        return
    if " " in password:
        printe("❌ La contraseña no puede contener espacios.")
        input("Continuar...")
        return
    if len(password) < 4:
        printe("❌ La contraseña debe tener al menos 4 caracteres.")
        input("Continuar...")
        return

    new_user = {"id": setId(), "user": user, "password": password, "post": []}
    data.append(new_user)
    setJson(data)
    printe("✅ Usuario registrado correctamente.")
    input("Continuar...")

def login():
    global actualUser
    clearConsole()
    data = getJson()

    if not data:
        printe("❔ No hay usuarios registrados.")
        input("Continuar...")
        return

    user = input("Usuario: ").strip()
    found = next((u for u in data if u["user"] == user), None)
    if not found:
        printe("❌ Usuario no encontrado.")
        input("Continuar...")
        return

    password = input("Contraseña: ").strip()
    if found["password"] != password:
        printe("❌ Contraseña incorrecta.")
        input("Continuar...")
        return

    actualUser = found["id"]
    printe("✅ Sesión iniciada correctamente.")
    input("Continuar...")
    viewUserMenu()

def viewLogMenu():
    while True:
        clearConsole()
        print(loginMenu)
        op = input("Ingrese una opción: ")
        if op == "1":
            login()
        elif op == "2":
            register()
        elif op == "3":
            clearConsole()
            printe("👋 ¡Hasta luego!")
            break
        else:
            printe("❌ Opción inválida.")

# USUARIO
def listarUsers():
    clearConsole()
    data = getJson()
    print("📃 Usuarios registrados:")
    print("------------------------")
    for u in data:
        print(f"🗿 {u['user']}")
    print("------------------------")
    input("Volver...")

# PUBLICACIONES
def crear_publicacion():
    global actualUser
    if actualUser is None:
        printe("❌ No hay usuario logueado.")
        input("Continuar...")
        return

    data = getJson()
    usuario = next((u for u in data if u["id"] == actualUser), None)

    clearConsole()
    print("📝 Crear Publicación")
    titulo = input("Título: ").strip()
    contenido = input("Contenido: ").strip()

    if not titulo or not contenido:
        printe("❌ Título y contenido no pueden estar vacíos.")
        input("Continuar...")
        return

    publicacion = {
        "titulo": titulo,
        "contenido": contenido,
        "likes": 0,
        "liked_by": []
    }

    usuario["post"].append(publicacion)
    setJson(data)
    printe("✅ Publicación creada con éxito.")
    input("Continuar...")

def ver_publicaciones():
    clearConsole()
    data = getJson()
    print("📖 Ver Publicaciones")
    for u in data:
        print(f"🗿 {u['user']}")
    print("------------------------")
    nombre = input("¿De quién deseas ver publicaciones?: ").strip()

    usuario = next((u for u in data if u["user"] == nombre), None)
    if not usuario:
        printe("❌ Usuario no encontrado.")
        input("Continuar...")
        return

    if not usuario["post"]:
        printe("❔ No tiene publicaciones.")
        input("Continuar...")
        return

    clearConsole()
    print(f"📄 Publicaciones de {usuario['user']}")
    for idx, post in enumerate(usuario["post"], 1):
        print(f"{idx}. 📝 {post['titulo']} (❤️ {post.get('likes', 0)} likes)")
    print("------------------------")
    titulo = input("Título exacto para ver contenido: ").strip()

    publicacion = next((p for p in usuario["post"] if p["titulo"] == titulo), None)
    if publicacion:
        clearConsole()
        print("📝 Publicación seleccionada:")
        print(f"📌 Título: {publicacion['titulo']}")
        print(f"📖 Contenido: {publicacion['contenido']}")
        print(f"❤️ Likes: {publicacion['likes']}")
        
        # Mostrar comentarios si existen
        if "comentarios" in publicacion and publicacion["comentarios"]:
            print(f"\n💬 Comentarios ({len(publicacion['comentarios'])}):")
            print("------------------------")
            for comentario in publicacion["comentarios"]:
                print(f"🗿 {comentario['usuario']}: {comentario['comentario']}")
        else:
            print("\n💬 No hay comentarios aún.")
    else:
        printe("❌ Publicación no encontrada.")
    input("Continuar...")

def dar_like():
    global actualUser
    if actualUser is None:
        printe("❌ No hay usuario logueado.")
        input("Continuar...")
        return

    data = getJson()
    print("❤️  Dar Like a Publicación")
    for u in data:
        print(f"🗿 {u['user']}")
    print("------------------------")
    nombre = input("¿A qué usuario deseas darle like?: ").strip()

    usuario = next((u for u in data if u["user"] == nombre), None)
    if not usuario:
        printe("❌ Usuario no encontrado.")
        input("Continuar...")
        return

    if not usuario["post"]:
        printe("❔ Este usuario no tiene publicaciones.")
        input("Continuar...")
        return

    for idx, post in enumerate(usuario["post"], 1):
        print(f"{idx}. 📝 {post['titulo']} (❤️ {post.get('likes', 0)} likes)")
    print("------------------------")
    titulo = input("Título exacto de la publicación: ").strip()

    publicacion = next((p for p in usuario["post"] if p["titulo"] == titulo), None)
    if not publicacion:
        printe("❌ Publicación no encontrada.")
        input("Continuar...")
        return

    if actualUser in publicacion.get("liked_by", []):
        printe("❌ Ya diste like a esta publicación.")
        input("Continuar...")
        return

    publicacion["likes"] += 1
    publicacion.setdefault("liked_by", []).append(actualUser)

    setJson(data)
    printe("✅ Diste like a la publicación.")
    input("Continuar...")

def comentar_publicacion():
    global actualUser
    if actualUser is None:
        printe("❌ No hay usuario logueado.")
        input("Continuar...")
        return

    data = getJson()
    usuario_actual = next((u for u in data if u["id"] == actualUser), None)
    
    clearConsole()
    print("💬 Comentar Publicación")
    for u in data:
        print(f"🗿 {u['user']}")
    print("------------------------")
    nombre = input("¿A qué usuario deseas comentar?: ").strip()

    usuario = next((u for u in data if u["user"] == nombre), None)
    if not usuario:
        printe("❌ Usuario no encontrado.")
        input("Continuar...")
        return

    if not usuario["post"]:
        printe("❔ Este usuario no tiene publicaciones.")
        input("Continuar...")
        return

    for idx, post in enumerate(usuario["post"], 1):
        print(f"{idx}. 📝 {post['titulo']} (❤️ {post.get('likes', 0)} likes)")
    print("------------------------")
    titulo = input("Título exacto de la publicación: ").strip()

    publicacion = next((p for p in usuario["post"] if p["titulo"] == titulo), None)
    if not publicacion:
        printe("❌ Publicación no encontrada.")
        input("Continuar...")
        return

    comentario = input("Escribe tu comentario: ").strip()
    if not comentario:
        printe("❌ El comentario no puede estar vacío.")
        input("Continuar...")
        return

    # Inicializar la lista de comentarios si no existe
    if "comentarios" not in publicacion:
        publicacion["comentarios"] = []

    # Agregar el comentario con información del usuario
    nuevo_comentario = {
        "usuario": usuario_actual["user"],
        "comentario": comentario
    }
    publicacion["comentarios"].append(nuevo_comentario)

    setJson(data)
    printe("✅ Comentario agregado exitosamente.")
    input("Continuar...")

# MENU DE USUARIO
def viewUserMenu():
    while True:
        clearConsole()
        print(userMenu)
        op = input("Seleccione una opción: ")
        if op == "1":
            listarUsers()
        elif op == "2":
            printe("👋 Sesión cerrada bye.")
            break
        elif op == "3":
            crear_publicacion()
        elif op == "4":
            ver_publicaciones()
        elif op == "5":
            dar_like()
        elif op == "6":
            comentar_publicacion()
        else:
            print("❌ Opción inválida.")

# MAIN
viewLogMenu()