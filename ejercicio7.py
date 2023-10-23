user = "Alexx"
password= "qwerty"

ingreso_user = input("Ingrese su usuario\n>>>")
ingreso_password= ""

if ingreso_user == user:
    ingreso_password = input("Ingrese su password\n>>>")
    if ingreso_password == password:
        print("Logueado con éxito")
        #acá va la aplicación
    else:
        print("Ingresó mal el password")
else:
    print("Ingresó un user que no existe")
            

    