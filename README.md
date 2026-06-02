# Pre-entrega Automation Testing - Ivana Papaño

Proyecto de automatización para el sitio SauceDemo - Talento Tech 2026


## Temario
* [1. Propósito del Proyecto](#1-propósito-del-proyecto)
* [2. Tecnologías Utilizadas](#2-tecnologías-utilizadas)
* [3. Estructura de Carpetas](#3-estructura-de-carpetas)
* [4. Casos de Prueba Automatizados](#4-casos-de-prueba-automatizados)
* [5. Instrucciones de Ejecución](#5-instrucciones-de-ejecución)
* [6. Evidencias](#6-evidencias)

---


## 1. Propósito del Proyecto
Este proyecto desarrolla la automatización de pruebas para el sitio **SauceDemo**. Se enfoca en validar flujos críticos de la plataforma: el proceso de autenticación (Login), la salida del sistema (Logout), la correcta visualización del catálogo de productos y la persistencia de datos (nombre y precio) al añadir artículos al carrito de compras, asegurando la estabilidad mediante el uso de esperas explícitas e interacciones con el DOM.

## 2. Tecnologías Utilizadas
* **Lenguaje:** Python 3.11+
* **Framework de Pruebas:** Pytest
* **Herramienta de Automatización:** Selenium WebDriver
* **Reportes:** Pytest-html

## 3. Estructura de Carpetas
El proyecto se organiza de la siguiente manera:
* `Tests/`: Scripts de prueba automatizados (Login, Catálogo, Carrito y Logout).
* `Utils/`: Lógica de soporte y configuraciones compartidas.
* `conftest.py`: Configuración de fixtures globales para el manejo automatizado del ciclo de vida del WebDriver.
* **Raíz del proyecto**: Almacena el reporte final HTML generado y el archivo de configuración `pytest.ini`.

## 4. Casos de Prueba Automatizados
La suite cuenta con un total de **9 ítems de prueba** completamente automatizados:

* **Gestión de Autenticación (`test_LoginPage.py`, `test_LoginBloqueado.py`, `test_LoginPageFallido.py`)**:
  * **Login Exitoso**: Validación de redirección correcta a `/inventory.html`.
  * **Login Fallido**: Control de mensajes de error frente a credenciales inválidas.
  * **Login Bloqueado**: Validación del mensaje de alerta específico para el usuario bloqueado (`locked_out_user`).
* **Cierre de Sesión (`test_Logout.py`)**:
  * **Logout Exitoso**: Verificación del retorno seguro al formulario de login tras cerrar sesión.
* **Catálogo de Productos (`test_inventory.py`)**:
  * Verificación del título de la interfaz y presencia de los artículos en pantalla.
  * Control de componentes visuales esenciales (menú lateral y filtros).
  * Extracción dinámica y logueo en consola del nombre y precio del primer producto del catálogo.
* **Carrito de Compras (`test_cart.py`)**:
  * Adición de un producto al carrito y validación del contador dinámico (`shopping_cart_badge`).
  * **Validación de persistencia**: Verificación rigurosa de que el nombre y el precio del artículo dentro del carrito coincidan exactamente con los capturados en el catálogo.

## 5. Instrucciones de Ejecución

Para ejecutar la suite completa de 9 pruebas de manera local y actualizar el reporte dinámico en la raíz del proyecto, ejecute el comando correspondiente según su terminal de Windows:

### Desde Command Prompt (CMD):
```cmd
python -m pytest --html="report_final.html" --self-contained-html -s

## 6. Evidencias

Los resultados de la última ejecución muestran un **100% de éxito (9/9 tests passed)**. 

Puede encontrar el desglose técnico y los resultados detallados directamente en el archivo interactivo **`report_final.html`** generado en la raíz de este proyecto.

