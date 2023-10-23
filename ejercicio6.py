list_usuarios=[]

respuesta= input("¿Quiere ingresar un usuario? y/N\n>>>")

while(respuesta == "y"):
    nuevo_usuario = input("Ingrese el nombre del usuario\n>>>")
    list_usuarios.append(nuevo_usuario)
    
    respuesta =input("¿Quiere ingresar más usuarios? y/N\n>>>")

print("Los usuarios son\n")
for users in list_usuarios:
    print(users)






