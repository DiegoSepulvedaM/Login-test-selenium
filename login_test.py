"""
Module login_test: This module contains functions related to authentication in a system.
"""
import time
from selenium import webdriver
from decouple import config  # Import the config function


def perform_test(username, password):
    # Set up the Selenium driver
    driver = webdriver.Chrome()

    try:
        # Open the login page on The Internet
        driver.get("http://the-internet.herokuapp.com/login")

        # Automate the login process
        input_username = driver.find_element("id", "username")
        input_password = driver.find_element("id", "password")
        login_button = driver.find_element("css selector", "button[type='submit']")
        input_username.send_keys(username)
        input_password.send_keys(password)
        login_button.click()

        # Add a pause to allow the page to load and authentication to occur
        time.sleep(2)

        # Verify if the login was successful
        if "You logged into a secure area!" in driver.page_source:
            print(f"Test for user: {username} PASSED. Successful login.")
        else:
            print(f"Test for user: {username} FAILED. Incorrect login.")

    finally:
        # Close the browser at the end of the test
        driver.quit()


# Load .env
user_id = config('USER_ID')
password_id = config('PASSWORD')

# Perform tests on The Internet
perform_test(user_id, password_id)

