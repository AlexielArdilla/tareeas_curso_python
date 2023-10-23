import sys

if len(sys.argv) > 1:
    nombre = sys.argv[1]
    print("Hola, "+nombre)
else:
    print("Ejecuta el script con tu nombre como argumento")