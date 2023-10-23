import re

patron = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

email = "ejemplo@ejemplo.com"

if re.match(patron, email):
    print("Es un correo válido")
else:
    print("No es un correo válido")