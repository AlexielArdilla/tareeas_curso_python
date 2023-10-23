jugando = True

while jugando:
    bando_user =input("Seleccione su bando:\n1.USA\n2.RUSIA\n>>>")
    if bando_user == "1":
        print("Su bando es: USA")
    elif bando_user == "2":
        print("Su bando es: RUSIA")
    else:
        print("Seleccione un bando correcto")
        
    jugando = False