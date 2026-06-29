from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        
        # Localizadores de la pantalla del carrito (POM)
        self.fila_productos = (By.CLASS_NAME, "cart_item")
        self.lbl_nombre_articulo = (By.CLASS_NAME, "inventory_item_name")
        self.lbl_precio_articulo = (By.CLASS_NAME, "inventory_item_price")

    def listar_elementos_del_carrito(self):
        """
        Recorre el carrito y devuelve una lista de diccionarios 
        con el nombre y precio de cada producto encontrado.
        """
        elementos = self.driver.find_elements(*self.fila_productos)
        lista_productos_carrito = []

        for elemento in elementos:
            texto_nombre = elemento.find_element(*self.lbl_nombre_articulo).text
            texto_precio = elemento.find_element(*self.lbl_precio_articulo).text

            lista_productos_carrito.append(
                {
                    "nombre": texto_nombre,
                    "precio": texto_precio
                }
            )

        return lista_productos_carrito