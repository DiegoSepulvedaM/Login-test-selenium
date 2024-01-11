from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

def realizar_prueba(usuario, contraseña):

    driver = webdriver.Chrome()

    try: 
        
        driver.get("http://the-internet.herokuapp.com/login")
    
        input_usuario = driver.find_element("id", "username")
        input_contraseña = driver.find_element("id", "password")
        boton_iniciar_sesion = driver.find_element("css selector", "button[type='submit']")
    
        input_usuario.send_keys(usuario)
        input_contraseña.send_keys(contraseña)
        boton_iniciar_sesion.click()
    
        time.sleep(2)
    
        if "You logged into a secure area!" in driver.page_source:
             print(f"Prueba para usuario: {usuario} PASADA. Inicio de sesion exitoso.")
    
        else:
             print(f"Prueba para usuario: {usuario} FALLADA. Inicio de sesion erroneo")
        
    finally:
    
     driver.quit()
     
     
realizar_prueba("tomsmith", "SuperSecretPassword!")