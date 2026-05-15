from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest 
import time

 
def test_logout_exitoso(login_in_driver):
    driver = webdriver.Chrome()
    try:
        # Usamos el driver que ya viene logueado
        driver = login_in_driver
        
        # 1. Abrir menú hamburguesa
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2) # Espera simple para que el menú se deslice
        
        # 2. Clic en Logout
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)
        
        # 3. Validación: Esperamos a que el botón de login aparezca de nuevo
        assert "saucedemo.com/" in driver.current_url
        assert driver.find_element(By.ID, "login-button").is_displayed()
        
        print("Test Logout: Sesión cerrada correctamente.")

    except Exception as e:
        print(f"Error en test_logout: {e}")
        raise


        