from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Chrome(options=options)
    context.driver.maximize_window()

def after_scenario(context, scenario):

    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()