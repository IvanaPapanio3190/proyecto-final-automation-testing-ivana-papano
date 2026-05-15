from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Utils.LoginPage import login
import pytest
import time


driver = webdriver.Chrome()

def test_login(login_in_driver):
    try:
        # PRIMERO definimos la variable
        driver = login_in_driver
        
        # El login YA SE HIZO en el conftest, así que solo validamos la URL
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
        
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    