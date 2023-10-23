tupla = ("Alexx", 22, False)
lista = ["Julieta", 35, False,45]
diccionario = {"Darío": 45, "Javier": 40, "Uriel": 39}

for item in tupla:
    print(item)
  
for item in lista:
    print(item)
    if item == "Julieta":
        print("Hola Julieta!!!") 
    
   
for item in diccionario:
    print(item , diccionario[item])