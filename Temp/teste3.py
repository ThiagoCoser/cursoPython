import keyboard

space_pressed = False

while True:
    if keyboard.is_pressed('space'):
        if not space_pressed:  # Verifica se a tecla foi pressionada uma vez
            print("Oops! That was no valid number. Try again...")
            space_pressed = True  # Marca que a tecla foi pressionada
    else:
        space_pressed = False  # Reseta o estado quando a tecla for solta
