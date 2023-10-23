class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola soy {self.nombre} y tengo {self.edad} años")
        

una_persona = Persona("Alexx", 40)

print(una_persona.nombre)
print(una_persona.edad)

una_persona.saludar()
