from selenium import webdriver
import time

def realizar_prueba(usuario, contrasena):
    # Configurar el driver de Selenium (asegúrate de tener el driver correspondiente instalado)
    driver = webdriver.Chrome()

    try:
        # Abrir la página de inicio de sesión en The Internet
        driver.get("http://the-internet.herokuapp.com/login")

        # Automatizar el inicio de sesión
        input_usuario = driver.find_element("id", "username")
        input_contrasena = driver.find_element("id", "password")
        boton_iniciar_sesion = driver.find_element("css selector", "button[type='submit']")

        input_usuario.send_keys(usuario)
        input_contrasena.send_keys(contrasena)
        boton_iniciar_sesion.click()

        # Agregar una pausa para permitir que la página se cargue y se realice la autenticación
        time.sleep(2)

        # Verificar si el inicio de sesión fue exitoso
        if "You logged into a secure area!" in driver.page_source:
            print(f"Prueba para usuario: {usuario} PASADA. Inicio de sesión exitoso.")
        else:
            print(f"Prueba para usuario: {usuario} FALLADA. Inicio de sesión incorrecto.")

    finally:
        # Cerrar el navegador al finalizar la prueba
        driver.quit()

# Realizar pruebas en The Internet
realizar_prueba("tomsmith", "SuperSecretPassword!")

