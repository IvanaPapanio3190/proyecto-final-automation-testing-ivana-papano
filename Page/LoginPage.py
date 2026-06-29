from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores de elementos 
        self.txt_usuario = (By.ID, "user-name")
        self.txt_password = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")
        self.lbl_error = (By.CSS_SELECTOR, "[data-test='error']")
    
    def abrir_pagina(self):
        """Navega a la URL de la app"""
        self.driver.get("https://www.saucedemo.com/")

    def escribir_usuario(self, usuario):
        """Ingresa el nombre de usuario en el campo correspondiente"""
        self.driver.find_element(*self.txt_usuario).send_keys(usuario)

    def escribir_password(self, password):
        """Ingresa la contraseña en el campo correspondiente"""
        self.driver.find_element(*self.txt_password).send_keys(password)

    def hacer_click_en_login(self):
        """Hace clic en el botón de ingresar"""
        self.driver.find_element(*self.btn_login).click()

    def ejecutar_login_completo(self, usuario, password):
        """Realiza el flujo completo de inicio de sesión"""
        self.abrir_pagina()
        self.escribir_usuario(usuario)
        self.escribir_password(password)
        self.hacer_click_en_login()

    def obtener_texto_de_error(self):
        """Captura el mensaje de error para los escenarios negativos"""
        return self.driver.find_element(*self.lbl_error).text

