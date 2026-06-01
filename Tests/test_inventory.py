from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def driver_logged(login_in_driver):
    driver = login_in_driver
    return driver



def test_inventory_title(driver_logged):
    titulo = driver_logged.title
    assert titulo == "Swag Labs", "El titulo de la pagina a la que se accede no es correcto"

def test_productos_visibles(driver_logged):
    productos = driver_logged.find_elements(By.CLASS_NAME,"inventory_item")
    assert len(productos) > 0

def test_ui_elements(driver_logged):
    menu = driver_logged.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver_logged.find_element(By.CLASS_NAME, "product_sort_container")

    assert menu.is_displayed(), "El icono del menu no está presente en la pagina"
    assert filtro.is_displayed(), "El filtro del catalogo no está presente en la pagina"



def test_listar_primer_producto(driver_logged):
    # Buscamos la lista de productos
    productos = driver_logged.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos disponibles en el catálogo"
    
    # Nos paramos en el primero (índice 0)
    primer_producto = productos[0]
    
    # Extraemos el nombre y el precio
    nombre = primer_producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = primer_producto.find_element(By.CLASS_NAME, "inventory_item_price").text
    
    # Lo imprimimos en consola (esto va a salir impecable en el reporte HTML)
    print(f"\n[INFO TP] Primer producto del catálogo: {nombre} | Precio: {precio}")
    
    # Validaciones de seguridad
    assert len(nombre) > 0, "El nombre del primer producto está vacío"
    assert "$" in precio, "El precio no tiene el formato de moneda correcto"

