try:
    resultado = 10/0
#except ZeroDivisionError:
 #   print("No se puede dividir por cero!!!")
except Exception as e:
    print(f"Ocurrió una excepción {e}")
else:
    print("Se realizó la operación con éxito")
finally:
    print(f"Esto sale así")
