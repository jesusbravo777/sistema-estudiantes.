# Sistema de registro de estudiantes

Aplicación web educativa para agregar, consultar y eliminar estudiantes con **Python, Flask y SQLite**.

## Funciones
- Agregar nombre, RUT y curso.
- Listar estudiantes registrados.
- Evitar RUT duplicados.
- Eliminar un registro.
- Guardar los datos localmente en SQLite.

## Ejecutar en Windows
1. Instala Python 3.
2. Abre PowerShell en esta carpeta.
3. Crea un entorno virtual: `py -m venv .venv`
4. Actívalo: `.\.venv\Scripts\Activate.ps1`
5. Instala dependencias: `pip install -r requirements.txt`
6. Ejecuta: `python app.py`
7. Abre `http://127.0.0.1:5000`

> Proyecto educativo. No uses datos reales o sensibles de estudiantes en una demostración pública. Antes de desplegarlo, configura una clave secreta segura y añade protección CSRF y autenticación.
