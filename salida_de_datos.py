import requests

# URL del formulario web
url = 'https://ejemplo.com/formulario'

# Datos que deseas enviar al formulario
data = {
    'nombre': 'Tu Nombre',
    'mensaje': 'Hola, este es mi mensaje desde Python.'
}

# Realiza una solicitud POST al formulario
response = requests.post(url, data=data)

# Verifica si la solicitud se realizó con éxito
if response.status_code == 200:
    print("Solicitud exitosa. Datos enviados al formulario.")
else:
    print("Error al enviar datos al formulario.")
