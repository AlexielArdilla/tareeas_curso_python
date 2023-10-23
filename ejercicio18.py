texto = "Yo tengo, un ratón"
palabras = texto.split(",")

#print(palabras)

print(palabras)

frase = "Python es bueno"
frase_mod = frase.replace("bueno", "genial")
print(frase_mod)


frase2 = "Mi tia es Peluda"
mayusculas = frase2.upper()
print(mayusculas)

minusculas = frase2.lower()
print(minusculas)


cadena_con_espacios = "soy Alexx\n"
cadena_normal = cadena_con_espacios.strip()
print(cadena_normal)

frase3 = "la poesía salvará al mundo"
#print(frase3.startswith("la"))
print(frase3.endswith("mundozzz"))