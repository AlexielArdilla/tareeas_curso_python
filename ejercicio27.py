import requests

url='https://ejemplo.com/formulario'

data ={
    'user': 'Alexx',
    'password': 'qwerty'
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Logging exitoso")
else:
    print("No se pudo logear")
    