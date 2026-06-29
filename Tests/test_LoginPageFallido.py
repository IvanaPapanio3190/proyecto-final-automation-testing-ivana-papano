from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login_credenciales_invalidas(driver):
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        # Ingresamos datos incorrectos
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("usuario_falso")
        driver.find_element(By.ID, "password").send_keys("clave_erronea")
        driver.find_element(By.ID, "login-button").click()
        
        # VALIDACIÓN: Buscamos el mensaje de error que aparece en rojo
        error_container = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        
        # Verificamos que el texto del error sea el esperado
        assert "Username and password do not match" in error_container.text
        print("Test Negativo: Error de login validado correctamente.")
        
    except Exception as e:
        print(f"Error en test_login_credenciales_invalidas: {e}")
        raise
        

