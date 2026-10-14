# Archivo md:

# Es un archivo de Markdown, un formato de texto simple que VS Code puede previsualizar con formato (títulos, listas, negritas, código). Es el estándar para documentar proyectos.

## 📘 Notas del Curso de Python Profesional

## Clase 1: Arquitectura de Software y Setup con Python

**Fecha:** 13/10/2026

---

## 🎯 Objetivos de la clase

- Entender la arquitectura Backend (servidor vs cliente)
- Configurar el entorno profesional de desarrollo
- Crear el primer servidor con Flask
- Servir contenido dinámico (JSON y HTML)

---

## 🛠️ Configuración del entorno

### 1. Python

- **Versión instalada:** Python 3.11.9
- **Verificar versión:** `python --version`
- **Verificar pip:** `pip --version`
- **Actualizar pip:** `pip install --upgrade pip`

### 2. VS Code

- **Extensiones instaladas:**
  - Python (Microsoft)
  - Pylance (Microsoft)
  - GitHub Copilot (opcional, requiere cuenta GitHub)

### 3. Pipenv (gestor de entornos virtuales)

- **Instalación global:** `pip install pipenv`
- **Verificar:** `pipenv --version` → 2026.9.1

> ⚠️ **Problema resuelto:** Pipenv se instaló pero el comando no se reconocía.
> **Solución:** Agregar al PATH de Windows la carpeta:
> `C:\Users\User\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts`
> (Variables de entorno → Variables de usuario → Path → Nuevo)

---

## 📁 Estructura del proyecto

web-flask-clase1/
├── main.py # Servidor Flask
├── Pipfile # Dependencias del proyecto (generado por pipenv)
├── Pipfile.lock # Versiones exactas (generado por pipenv)
└── NOTAS.md # Este archivo

#

**Ubicación del entorno virtual:**
`C:\Users\User\.virtualenvs\web-flask-clase1-pXx7AvQ_`

---

## 💻 Comandos esenciales

### Activar el entorno virtual

```cmd
cd C:\Users\User\Desktop\web-flask-clase1
pipenv shell

# Ejecutar el servidor: pipenv run python main.py
Detener el servidor: Ctrl + C
# Instalar un paquete nuevo: pipenv install nombre_paquete
# Ver la versión de un paquete: pipenv run python -c "import flask; print(flask.__version__)"

# 🐍 Código del primer servidor (main.py)
# 🧠 Conceptos clave aprendidos

# ¿Qué es Flask?
Microframework web de Python. Permite crear servidores web de forma sencilla.

¿Qué es un decorador @app.route()?
Asocia una URL con una función de Python. Cuando el usuario visita esa URL, Flask ejecuta la función.

¿Qué es app.run(debug=True)?
Ejecuta el servidor en modo desarrollo

debug=True → reinicia automáticamente al guardar cambios y muestra errores detallados

¿Qué es un entorno virtual?
Carpeta aislada donde se instalan las dependencias de un proyecto. Evita conflictos entre proyectos que usan diferentes versiones de una misma librería.

¿Qué es Pipenv?
Herramienta que gestiona entornos virtuales y dependencias. Usa Pipfile en lugar de requirements.txt.

#  Resultado final
El servidor corre en: http://127.0.0.1:5000

/ → Muestra "Home page" con enlace a /random_fact

/random_fact → Muestra un dato aleatorio con enlace de vuelta

# ✅ Estado de la Clase 1
☑ Python instalado
☑ pip actualizado
☑ VS Code configurado
☑ Pipenv instalado y funcional
☑ Entorno virtual creado
☑ Flask instalado
☑ Primer servidor funcionando
☑ Navegación dinámica probada

```
# Ctrl + Shift + V
# Eso abre una **vista previa** del Markdown con títulos, listas y colores. Muy útil para leerlo después.

---
