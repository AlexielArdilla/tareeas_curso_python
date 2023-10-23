password = "GabyILoveyou"

user = input("Ingrese el user a crackear\n>>>")

with open("posibles_passwords.txt", "r") as pass_list:
    
    for pass_case in pass_list.readlines():

        pass_case = pass_case.strip()

        #print(pass_case)

        if password == pass_case:

            print(f"Password encontrado: {pass_case} del user {user}")
            break
        else:
            print(pass_case)
        
