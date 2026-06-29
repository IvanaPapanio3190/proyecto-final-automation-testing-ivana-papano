import pytest
from selenium import webdriver
from Page.LoginPage import LoginPage
from Utils.Data_Reader import read_users_csv
import pathlib
import pytest_html

@pytest.fixture

def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window() 
    
    yield driver
    
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login_page = LoginPage(driver)
    
    # Navegamos a la web antes de loguearnos
    driver.get("https://www.saucedemo.com/")
    
    # Leemos el primer usuario del CSV de forma dinámica
    user = read_users_csv()[0]
    
    # Ejecutamos el login
    login_page.escribir_usuario(user["username"])
    login_page.escribir_password(user["password"])
    login_page.hacer_click_en_login()
    
    return driver

   


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Intentamos obtener el driver desde los argumentos del test
        driver = item.funcargs.get("driver") or item.funcargs.get("login_in_driver") or item.funcargs.get("driver_logged")

        if driver:
            target = pathlib.Path("reports/screenshots")
            target.mkdir(parents=True, exist_ok=True)
            file_name = target / f"{item.name}.png"
            
            driver.save_screenshot(str(file_name))

            if hasattr(report, "extra"):
                report.extra.append({
                    "name": "screenshot",
                    "format": "image",
                    "content": str(file_name)
                })

            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(str(file_name)))
            report.extras = extras