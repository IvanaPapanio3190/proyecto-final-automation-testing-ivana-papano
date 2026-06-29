from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        # Localizadores de la página de inventario (POM)
        self.items_inventario = (By.CLASS_NAME, "inventory_item")
        self.btn_menu = (By.ID, "react-burger-menu-btn")
        self.cmb_filtro = (By.CLASS_NAME, "product_sort_container")
        self.btn_agregar_carrito = (By.CLASS_NAME, "btn_inventory")
        self.badge_carrito = (By.CLASS_NAME, "shopping_cart_badge")
        self.icono_carrito = (By.CLASS_NAME, "shopping_cart_link")
        self.lbl_nombres_productos = (By.CLASS_NAME, "inventory_item_name")
    
    def obtener_titulo_pagina(self):
        """Retorna el título oficial del sitio web"""
        return self.driver.title
    
    def listar_productos(self):
        """Devuelve la lista de todos los elementos web de productos"""
        return self.driver.find_elements(*self.items_inventario)
    
    def verificar_menu_visible(self):
        """Valida si el menú lateral está visible en pantalla"""
        return self.driver.find_element(*self.btn_menu).is_displayed()
    
    def verificar_filtro_visible(self):
        """Valida si el combo de ordenamiento/filtro está desplegado"""
        return self.driver.find_element(*self.cmb_filtro).is_displayed()
    
    def click_agregar_primer_producto(self):
        """Agrega el primer artículo de la lista al carrito"""
        self.driver.find_elements(*self.btn_agregar_carrito)[0].click()

    def obtener_cantidad_carrito(self):
        """Devuelve el número actual que muestra el carrito"""
        return self.driver.find_element(*self.badge_carrito).text
    
    def obtener_nombre_del_primer_producto(self):
        """Retorna el texto del nombre del primer artículo en la tienda"""
        return self.driver.find_elements(*self.lbl_nombres_productos)[0].text
    
    def navegar_al_carrito(self):
        """Hace clic en el icono del carrito para ir al checkout"""
        self.driver.find_element(*self.icono_carrito).click()
    
    def seleccionar_producto_por_nombre(self, nombre_buscado):
        """Busca un producto específico que coincida con el JSON y lo añade"""
        productos = self.listar_productos()

        for producto in productos:
            nombre_actual = producto.find_element(*self.lbl_nombres_productos).text

            if nombre_actual == nombre_buscado:
                producto.find_element(*self.btn_agregar_carrito).click()
                break