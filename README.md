# Bloqueador de Páginas - Aplicación de tkinter

Este script de Python es una aplicación simple de bloqueo de páginas web utilizando el archivo de hosts en sistemas Windows. La interfaz gráfica de usuario está construida con tkinter.

## Características

- Permite agregar una URL al archivo de hosts para bloquear el acceso a un sitio web.
- Permite eliminar una URL del archivo de hosts para desbloquear un sitio web previamente bloqueado.
- Proporciona una opción para listar las páginas bloqueadas actualmente.

## Requisitos

- Python 3.x
- tkinter (ya viene incluido en la instalación estándar de Python)
- Las siguientes librerías Python deben estar instaladas:
    - zstandard
    - Nuitka
    - ordered-set

## Instalación de las librerías

Ejecuta los siguientes comandos para instalar las librerías necesarias:

```bash
pip install zstandard Nuitka ordered-set
```

## Compilación del script

Se puede utilizar Nuitka para compilar el script en un archivo ejecutable independiente. Ejecuta el siguiente comando para compilar el script `bloqueador.py`:

```bash
py -m nuitka --mingw64 --onefile --enable-plugin=tk-inter bloqueador.py
```

## Instrucciones de uso

1. Ejecutar el script `bloqueador.py` utilizando Python 3.x.
2. En la interfaz gráfica, ingresar una URL en el campo de entrada y hacer clic en el botón "Añadir" para bloquear la página.
3. Para desbloquear una página, ingresar la misma URL en el campo de entrada y hacer clic en el botón "Eliminar".
4. Para listar las páginas bloqueadas, hacer clic en el botón "Listar".

## Importante

- Este script requiere permisos de administrador para modificar el archivo de hosts en `C:/Windows/System32/drivers/etc/hosts`. 

## Notas

- El script solo ha sido probado en sistemas Windows.


