import requests
import subprocess

# URL del archivo en GitHub (repositorio público)
url = 'https://raw.githubusercontent.com/gioboto/rexdata/refs/heads/main/data.dat'

def leer_archivo_github(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        contenido = response.text
        return contenido.strip()  # Elimina espacios y saltos de línea
    except requests.RequestException as e:
        print(f"Error al leer el archivo: {e}")
        return None

def ejecutar_aplicacion():
    # Aquí se coloca el comando para ejecutar la aplicación
    # Por ejemplo, ejecutar un script o un binario
    comando = ["python3.11", "hola.py"]  # Cambia esto por tu aplicación
    try:
        subprocess.run(comando, check=True)
        print("Aplicación ejecutada correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar la aplicación: {e}")

def main():
    contenido = leer_archivo_github(url)

    if contenido is None:
        print("No se pudo leer el archivo.")
        return

    # Condicionar la ejecución según el contenido leído
    if contenido == "run_app":
        print("Ejecutando la aplicación...")
        ejecutar_aplicacion()
    elif contenido == "do_nothing":
        print("No se ejecutará ninguna acción.")
    else:
        print(f"Contenido no reconocido: {contenido}")

if __name__ == "__main__":
    main()

