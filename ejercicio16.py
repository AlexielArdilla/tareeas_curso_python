edad_del_user = int(input("Ingrese su edad\n>>>"))

if edad_del_user > 18:
    print("Puede entrar al bar")
elif edad_del_user == 18:
    print("Puede entrar aunque tiene cara de niño")
else:
    print("No puede entrar, vaya a su casita")

