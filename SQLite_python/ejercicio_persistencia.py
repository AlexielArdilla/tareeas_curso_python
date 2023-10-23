import sqlite3

# Función para crear la tabla de usuarios si no existe
def crear_tabla_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT,
                      password TEXT)''')
    conn.commit()
    conn.close()

# Función para insertar un nuevo usuario y contraseña en la base de datos
def insertar_usuario(username, password):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

# Función para listar todos los usuarios
def listar_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Main del programa
if __name__ == '__main__':
    crear_tabla_usuarios()
    
    while True:
        print("1. Registrar un usuario")
        print("2. Listar usuarios")
        print("3. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            username = input("Ingresa un nombre de usuario: ")
            password = input("Ingresa una contraseña: ")
            insertar_usuario(username, password)
            print("Usuario registrado con éxito.\n")
        elif opcion == '2':
            usuarios = listar_usuarios()
            if usuarios:
                print("Usuarios registrados:")
                for usuario in usuarios:
                    print(usuario[0])
            else:
                print("No hay usuarios registrados.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.\n")
