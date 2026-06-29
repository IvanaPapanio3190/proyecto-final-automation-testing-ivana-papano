from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Page.LoginPage import LoginPage
import pytest
import time


def test_login_ok(driver):
    login_page = LoginPage(driver)
    

    login_page.ejecutar_login_completo("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"

def test_login_invalid_password(driver):
    login_page = LoginPage(driver)

    login_page.ejecutar_login_completo("standard_user", "123456")

    error = login_page.obtener_texto_de_error() 
    assert "Epic sadface: Username and password do not match any user in this service" in error