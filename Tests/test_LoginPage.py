from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time


driver = webdriver.Chrome()

def test_login():

  try:
      
      # Ingresar a la página de login
      driver.get("https://www.saucedemo.com/")

      # Ingresar nombre de usuario 
      usuario = driver.find_element(By.ID, "user-name")
      usuario.send_keys("standard_user")

      # Ingresar contraseña
      password=driver.find_element(By.ID, "password")
      password.send_keys("secret_sauce")

      # Hacer click en el botón de login
      login_button=driver.find_element(By.ID, "login-button") 
      login_button.click()

      # Verificación de la URL después del login
      # Comprobamos que la URL cambió a la de adentro de la página
      assert "inventory.html" in driver.current_url
  
  finally:
    
    driver.quit()
    