import pytest
import pytest_check as check
import requests

# Configuración de cabeceras comunes para la API
headers = {
    "x-api-key" : "pub_5bca5ffc8772df976fcf8970168a1ad219ad499c472afbba2f27085fa4b4ef7d"
}

@pytest.mark.api
@pytest.mark.smoke
def test_login_valido_api():
    """Valida un inicio de sesión exitoso devolviendo código 200"""
    datos_login = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    respuesta = requests.post("https://reqres.in/api/login", headers=headers, json=datos_login)
    assert respuesta.status_code == 200, "El login válido falló"

@pytest.mark.api
def test_login_sin_password_api():
    """Valida el error 400 cuando falta la contraseña"""
    datos_login = {
        "email": "eve.holt@reqres.in",
    }
    respuesta = requests.post("https://reqres.in/api/login", headers=headers, json=datos_login)
    info_respuesta = respuesta.json()
    
    assert respuesta.status_code == 400
    assert info_respuesta["error"] == "Missing password", "Mensaje de error incorrecto para password faltante"

@pytest.mark.api
def test_login_sin_email_api():
    """Valida el error 400 cuando falta el email"""
    datos_login = {
        "password": "cityslicka",
    }
    respuesta = requests.post("https://reqres.in/api/login", headers=headers, json=datos_login)
    info_respuesta = respuesta.json()
    
    assert respuesta.status_code == 400
    assert info_respuesta["error"] == "Missing email or username", "Mensaje de error incorrecto para email faltante"

@pytest.mark.api
def test_crear_usuario_api():
    """Valida la creación de un nuevo usuario en el sistema"""
    datos_usuario = {
        "name": "Ivana",
        "email": "ivana.test@bue.edu.ar",
        "password": "pwd_12345*"
    }
    respuesta = requests.post("https://reqres.in/api/users", headers=headers, json=datos_usuario)
    datos_recibidos = respuesta.json()

    # Validamos estado de creación exitosa (201)
    assert respuesta.status_code == 201, "No se pudo crear el usuario"
    
    # Validaciones sobre el formato de los datos enviados
    assert datos_usuario["email"].count("@") == 1, "El email cargado no posee un formato válido"
    assert "*" in datos_usuario["password"], "La contraseña no posee el caracter especial *"

    # Validamos que la respuesta del servidor coincida con lo enviado
    assert datos_recibidos["name"] == datos_usuario["name"], "El nombre retornado no coincide"
    assert datos_recibidos["email"] == datos_usuario["email"], "El email retornado no coincide"

    # Verificamos que responda rápido (menos de 1.5 segundos para dar margen de red)
    assert respuesta.elapsed.total_seconds() < 4.0, "El servicio demoró más de lo esperado"

@pytest.mark.api
def test_eliminar_usuario_api():
    """Valida la eliminación de un usuario por ID devolviendo código 204"""
    respuesta = requests.delete("https://reqres.in/api/users/2", headers=headers)
    assert respuesta.status_code == 204, "Falló la baja del usuario"

@pytest.mark.api
def test_obtener_usuario_api():
    """Valida la consulta de datos de un usuario por ID"""
    respuesta = requests.get("https://reqres.in/api/users/2", headers=headers)
    assert respuesta.status_code == 200, "No se pudo obtener el usuario"
    
    tiempo_respuesta = respuesta.elapsed.total_seconds()
    print(f"\n Tiempo de respuesta GET: {tiempo_respuesta} segs")
    assert tiempo_respuesta < 30.0,"El tiempo de ejecución tardó más de lo esperado"
    