import pytest
from Page.LoginPage import LoginPage
from Utils.Data_Reader import read_users_csv

@pytest.mark.parametrize("usuario_datos", read_users_csv())
def test_autenticacion_usuarios_csv(driver, usuario_datos):
    """
    Test parametrizado que valida múltiples perfiles de usuario (válidos e inválidos)
    recorriendo de forma dinámica las filas del archivo users.csv.
    """
   
    pantalla_login = LoginPage(driver)

    driver.get("https://www.saucedemo.com/")

    pantalla_login.escribir_usuario(usuario_datos["username"])
    pantalla_login.escribir_password(usuario_datos["password"])
    pantalla_login.hacer_click_en_login()
    
    # Verificación dinámica según el tipo de usuario configurado en el CSV
    if usuario_datos["valid"].lower() == "true":
        # Si el usuario es válido, confirmamos que ingresó a la tienda mirando la URL
        assert "/inventory.html" in driver.current_url, "Un usuario válido no pudo ingresar al inventario."
    else:
        # Si es inválido, capturamos el cartel de error el método y validamos el mensaje
        mensaje_error_pantalla = pantalla_login.obtener_texto_de_error()
        assert "Epic sadface" in mensaje_error_pantalla, f"No se mostró el error esperado para el usuario: {usuario_datos['username']}"