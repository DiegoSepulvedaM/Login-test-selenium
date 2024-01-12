from selenium import webdriver 
import time
from decouple import config         #import the necessary modules

def realizar_prueba(user, password):
    
    #configure Selenium
    driver = webdriver.Chrome()
    
    #open the link to do the automation
    
    try:
        driver.get("http://the-internet.herokuapp.com/login")
        
        #automatize the login
        
        input_user = driver.find_element("id", "username")
        input_password = driver.find_element("id" , "password")
        input_button = driver.find_element("css selector", "button[type = 'submit']")
        
        input_user.send_keys(user)
        
        input_password.send_keys(password)
        
        input_button.click()
        
        #add a pause for allow the page load and do the authentication
        
        time.sleep(2)
        
        #verify if the login was succesfull
        
        if "You logged into a secure area!" in driver.page_source:
            print(f"prueba para user : {user} Exitosa. Inicio de sesion correcto")
        else:
            print(f"prueba para user: {user} Fallida. Inicio de sesion Incorrecto" )
            
            #close the browser to finish the test
            
    finally:
        driver.quit()
        

#load the user and password with the .env file
        
user = config('USER')

password = config ('PASSWORD')

#do the test

realizar_prueba(user , password)




        

    
    
    