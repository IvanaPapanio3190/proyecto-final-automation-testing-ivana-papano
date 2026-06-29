# Proyecto Final Automation Testing - Ivana Papaño

---

Proyecto de automatización para el sitio SauceDemo - Talento Tech 2026


## Temario
* [1. Propósito del Proyecto](#1-propósito-del-proyecto)
* [2. Tecnologías Utilizadas](#2-tecnologías-utilizadas)
* [3. Estructura de Carpetas](#3-estructura-de-carpetas)
* [4. Casos de Prueba Automatizados](#4-casos-de-prueba-automatizados)
* [5. Instrucciones de Ejecución](#5-instrucciones-de-ejecución)
* [6. Reportes y Evidencias](#6-evidencias)
* [7. Integración Continua (CI/CD)](#7-integración-continua-cicd)
* [8. Informacion del Proyecto](#8-información-del-proyecto)

---


## 1. Propósito del Proyecto
Este proyecto desarrolla la automatización de pruebas para el sitio **SauceDemo**. Se enfoca en validar flujos críticos de la plataforma: el proceso de autenticación (Login), la salida del sistema (Logout), la correcta visualización del catálogo de productos y la persistencia de datos (nombre y precio) al añadir artículos al carrito de compras, asegurando la estabilidad mediante el uso de esperas explícitas e interacciones con el DOM.


## 2. Tecnologías Utilizadas

* **Lenguaje principal:** Python 3.13
* **Automatización Web (UI):** Selenium WebDriver & Webdriver-Manager
* **Framework de Pruebas:** Pytest (con soporte de `pytest-check` para soft asserts)
* **Pruebas de API:** Requests
* **Enfoque BDD (Behavior-Driven Development):** Behave (Lenguaje Gherkin)
* **Reportes Visuales:** Pytest-html
* **Control de Versiones y CI/CD:** Git & GitHub Actions


## 3. Estructura de Carpetas
El proyecto está estructurado de manera limpia, escalable y mantenible:
* `Page/`: Clases correspondientes a las páginas web bajo el patrón **Page Object Model (POM)**, separando la interacción del DOM de los scripts de prueba.
* `Tests/`: Suite de pruebas automatizadas con Pytest:
  - Pruebas de UI tradicionales (`test_inventory.py`, `test_cart.py`, etc.).
  - Pruebas parametrizadas basadas en datos externos (`test_login_csv.py` y `test_cart_json.py`).
  - Pruebas de API REST (`test_api.py`).
* `features/`: Escenarios de prueba BDD escritos en Gherkin (`.feature`) y sus archivos de mapeo de pasos (`steps/`).
* `Data/`: Fuentes de datos externas (archivos `.csv` y `.json`) para la parametrización de pruebas.
* `Reports/`: Carpeta destinada a almacenar el reporte interactivo HTML y las capturas de pantalla (`.png`) generadas de forma automática en caso de fallos.
* `.github/workflows/`: Configuración del pipeline automatizado (`tests.yml`) para la ejecución en la nube.
* `requirements.txt`: Archivo con la lista estandarizada de dependencias del proyecto.
* `pytest.ini`: Configuración global de ejecución de Pytest.


## 4. Casos de Prueba Automatizados

### A. Pruebas de UI - Selenium WebDriver (SauceDemo)
* **Gestión de Autenticación (Flujos Positivos y Negativos):** Login Exitoso, Login Fallido (credenciales inválidas) y Login Bloqueado (`locked_out_user`).
* **Manejo de Datos Externos (Parametrización):** Inyección de credenciales mediante lectura dinámica de archivos **CSV** y validación de payloads desde archivos **JSON**.
* **Cierre de Sesión:** Retorno seguro al formulario de Login.
* **Carrito e Inventario:** Verificación de catálogo, adición de productos, actualización del contador dinámico y validación rigurosa de persistencia (coincidencia exacta de nombre y precio entre catálogo y carrito).

### B. Pruebas de API - Requests (ReqRes API)
Automatización de múltiples endpoints utilizando diferentes métodos HTTP con validaciones de códigos de estado, estructuras de respuesta JSON y aserciones detalladas:
* **GET:** Listar usuarios (Status 200).
* **POST:** Creación exitosa de un recurso (Status 201) y flujo negativo de registro fallido por falta de contraseña (Status 400).
* **DELETE:** Borrado exitoso de un recurso (Status 204).

### C. Pruebas de Comportamiento BDD (Behave)
* Escenarios escritos en lenguaje natural (Dado/Cuando/Entonces) para validar el flujo crítico de inicio de sesión, integrados directamente con las clases del patrón POM existentes.



## 5. Instrucciones de Ejecución

Para preparar el entorno local y ejecutar las suites de prueba, siga estos pasos desde su terminal de Windows:

### **Instalar todas las dependencias requeridas**


   ```bash
   pip install -r requirements.txt
  ```

### **Ejecución de las suites**

* **Para correr Pytest (Web + API):** `pytest`
* **Para correr Behave (BDD):** `behave` 



## 6. Reportes y Evidencias


* **Interpretación del Reporte:** Tras finalizar la ejecución de Pytest, se actualizará el archivo **`report_Final.html`** dentro de la carpeta del proyecto. Al abrirlo en cualquier navegador web, este reporte interactivo muestra:
  - El estado final de cada test (Pasado / Fallado / Erróneo).
  - La duración exacta de cada prueba.
  - El historial de logs técnicos detallados para depuración.


* **Manejo Automático de Capturas (Screenshots):** Si alguna prueba de UI llega a fallar, el framework captura automáticamente la pantalla en ese instante preciso y la incrusta directamente dentro del reporte HTML, guardando además la evidencia física `.png` con la fecha y hora exacta del suceso.

## 7. Integración Continua (CI/CD)

El proyecto cuenta con una integración de **GitHub Actions**. Ante cada evento de `push` o `pull_request` en las ramas principales, un contenedor virtual levanta el entorno de forma automatizada, instala las dependencias mediante el archivo `requirements.txt` y ejecuta la totalidad de las pruebas en la nube en modo **Headless (navegador invisible)**, garantizando un flujo continuo de calidad (CI).

---

## 8. Información del Proyecto

* **Desarrollado por:** Ivana Papaño - QA Automation
* **Proyecto Final:** Curso de Automation Testing 
* **Programa:** Talento Tech 2026
* **Profesor/Tutor:** José Montezuma

---

