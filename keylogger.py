import pynput.keyboard

# Función que se llama cuando se presiona una tecla
def on_key_press(key):
    try:
        # Registra la tecla presionada
        with open("registro_teclado.txt", "a") as file:
            file.write(str(key))
    except AttributeError:
        pass

# Crea un objeto de escucha de teclado
keyboard_listener = pynput.keyboard.Listener(on_press=on_key_press)

# Solicita el consentimiento del usuario
consentimiento = input("¿Deseas iniciar la captura de teclas? (s/n): ").lower()

if consentimiento == "s":
    print("La captura de teclas ha comenzado. Presiona Ctrl+C para detener.")
    with open("registro_teclado.txt", "a") as file:
        file.write("\n--- Inicio de la captura de teclas ---\n")
    keyboard_listener.start()
    keyboard_listener.join()
else:
    print("La captura de teclas no ha comenzado.")

