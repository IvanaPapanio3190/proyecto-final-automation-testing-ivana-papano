from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_logout_exitoso():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://www.saucedemo.com/")
        # 1. Login previo
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # 2. Abrir menú hamburguesa
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        
        # 3. Clic en Logout (usamos espera explícita porque el menú tarda en desplegarse)
        logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout_link.click()
        

        # 4. Validación: Esperamos a que el botón de login aparezca de nuevo
        login_button = wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
        assert login_button.is_displayed()
        assert "saucedemo.com/" in driver.current_url
        print("Test Logout: Sesión cerrada correctamente.")
    finally:
        driver.quit()

        