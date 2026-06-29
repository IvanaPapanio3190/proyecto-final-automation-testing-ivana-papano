from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_usuario_bloqueado(driver):
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://www.saucedemo.com/")
        # Usamos el usuario bloqueado que da la página
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Validamos el mensaje específico de bloqueo
        error_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']")))
        assert "Sorry, this user has been locked out" in error_msg.text
        print("Test Bloqueado: Validado con éxito.")
    except Exception as e:
        print(f"Error en test_usuario_bloqueado: {e}")
        raise

        