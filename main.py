import json, os
ruta = "database.json"
actualUser = None

loginMenu = """

    Biembenido al menu de usuario. 👤

    1. 🔒 Iniciar Sesion
    2. 🔑 Registrarse
    3. ❌ Salir

"""

def printe(msg):
    print(f"----------------------------------------------------------------\n {msg} \n----------------------------------------------------------------")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

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


while True:
    clearConsole()
    print(loginMenu)
    op = input("Ingrese una opcion: ")
    if op == "1":
        pass
    elif op == "2":
        register()
    elif op == "3":
        clearConsole()
        printe("\n\n     👋 Goodbye! \n\n")
        break
    else:
        printe("Invalid option, please try again.")