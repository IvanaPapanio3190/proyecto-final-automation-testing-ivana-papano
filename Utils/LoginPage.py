from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Definir los selectores (los "objetos" de la página)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    # Métodos para interactuar con la página
    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    
    def login_to_sauce(self, username, password):
        # 1. Espera explícita para asegurarnos de que la página está lista
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.username_field))
        
        # 2. Usamos tus métodos
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
        # 3. Validación de que entramos 
        wait.until(EC.url_contains("/inventory.html"))


def login(driver):
    login_page = LoginPage(driver)
    login_page.login_to_sauce("standard_user", "secret_sauce")