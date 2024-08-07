import time

x = 1
inicia = True

while inicia:

    print(x)
    x += 3
    time.sleep(0.2)

    if x>50:
        inicia=False

print("Terminou")
