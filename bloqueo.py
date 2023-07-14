hostsFile = "C:/Windows/System32/drivers/etc/hosts"
direccion = "127.0.0.1"
dominio = "www.ejemplo.com"

def agregar_direccion():
    with open(hostsFile, 'a') as archivo:
        archivo.write(f"\n{direccion}\t{dominio}")

# Llamada a la función para agregar la dirección al archivo hosts
agregar_direccion()
