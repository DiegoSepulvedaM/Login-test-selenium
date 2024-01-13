import time
from selenium import webdriver
from decouple import config

def perform_login(username, password):
    driver = webdriver.Chrome()
    try:
        driver.get("http://the-internet.herokuapp.com/login")
        input_username = driver.find_element("id", "username")
        input_password = driver.find_element("id", "password")
        login_button = driver.find_element("css selector", "button[type='submit']")
        input_username.send_keys(username)
        input_password.send_keys(password)
        login_button.click()
        time.sleep(2)
        return "You logged into a secure area!" in driver.page_source
    finally:
        driver.quit()

