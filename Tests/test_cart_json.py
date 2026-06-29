import pytest
from Page.InventoryPage import InventoryPage
from Page.CartPage import CartPage
from Utils.Data_Reader import read_products_json

def test_carrito_con_datos_json(login_in_driver):
    """
    Test que lee productos desde un archivo JSON, los agrega al carrito
    y verifica que se listen correctamente con sus nombres y precios.
    """
    driver = login_in_driver
    
    # Inicializamos tus objetos de página
    pantalla_inventario = InventoryPage(driver)
    pantalla_carrito = CartPage(driver)
    
    # Cargamos la lista de productos desde tu JSON
    lista_productos_json = read_products_json()

    # Bucle para añadir cada producto del JSON usando tu método personalizado
    for articulo in lista_productos_json:
        pantalla_inventario.seleccionar_producto_por_nombre(articulo["nombre"])

    # Vamos al carrito usando tus métodos
    pantalla_inventario.navegar_al_carrito()
    elementos_en_carrito = pantalla_carrito.listar_elementos_del_carrito()

    # Verificación cruzada: Validamos que cada producto del JSON exista en el carrito
    for prod_json in lista_productos_json:
        item_encontrado = False
        
        for prod_carrito in elementos_en_carrito:
            # Comparamos que coincidan tanto el nombre como el precio
            if (prod_carrito["nombre"] == prod_json["nombre"]) and (prod_carrito["precio"] == prod_json["precio"]):
                item_encontrado = True
                break

        # Mensaje de error personalizado en caso de falla
        assert item_encontrado, f" No se encontró en el carrito el producto: {prod_json['nombre']}"