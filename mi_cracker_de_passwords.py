password = "sandro"

with open("posibles_passwords.txt", "r") as pass_list:
    for pass_case in pass_list.readlines():
        # Elimina el carácter de nueva línea
        pass_case = pass_case.strip()  
        print(pass_case)
        if password == pass_case: 
            print(f"Password encontrado: {pass_case}")
            break
    else:
        print("No encontramos el password!!!")