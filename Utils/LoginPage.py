from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(driver):
    # 1. Navegar a la URL
    driver.get("https://www.saucedemo.com/")
    time.sleep(1) # Un segundito para que cargue

    # 2. Ingresar usuario
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")

    # 3. Ingresar contraseña
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    # 4. Click en botón
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1) # Esperamos a que redireccione
    

