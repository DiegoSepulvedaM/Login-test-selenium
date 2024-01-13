import os
from selenium import webdriver
import time
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

print(os.getenv('USER'))
print(os.getenv('PASSWORD'))


def realizar_prueba(user, password):
    # Configurar el driver de Selenium para Firefox (geckodriver)
    driver = webdriver.Firefox()

    try:
        # Abrir la página de inicio de sesión en The Internet
        driver.get("http://the-internet.herokuapp.com/login")

        # Automatizar el inicio de sesión
        input_user = driver.find_element("id", "username")
        input_password = driver.find_element("id", "password")
        boton_iniciar_sesion = driver.find_element("css selector", "button[type='submit']")

        input_user.send_keys(user)
        input_password.send_keys(password)
        boton_iniciar_sesion.click()

        # Agregar una pausa para permitir que la página se cargue y se realice la autenticación
        time.sleep(2)

        # Verificar si el inicio de sesión fue exitoso
        if "You logged into a secure area!" in driver.page_source:
            print(f"Prueba para USER: {user} PASADA. Inicio de sesión exitoso.")
        else:
            print(f"Prueba para user: {user} FALLADA. Inicio de sesión incorrecto.")

    finally:
        # Cerrar el navegador al finalizar la prueba
        driver.quit()

# Cargar el nombre de usuario y la contraseña desde las variables de entorno
user = os.getenv('MY_USER')
password = os.getenv('PASSWORD')

# Realizar pruebas en The Internet
realizar_prueba(user, password)
