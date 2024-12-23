# Gestor de Inventario en Python

## Descripción

El **Gestor de Inventario en Python** es el proyecto integrador final del curso de Python en **Talento Tech**. Esta aplicación de consola permite gestionar un inventario con operaciones como agregar, actualizar, eliminar y visualizar productos. Además, incluye búsqueda avanzada y generación de reportes para productos con bajo stock, utilizando una base de datos SQLite.

El proyecto demuestra el uso práctico de Python para resolver problemas reales, aplicando conceptos aprendidos durante el curso.

## Funcionalidades

- **Registrar Producto**: Permite agregar nuevos productos al inventario con información como nombre, descripción, cantidad, precio y categoría.
- **Visualizar Productos**: Muestra todos los productos registrados en el inventario de forma organizada.
- **Actualizar Producto**: Permite modificar la información de un producto existente, como nombre, descripción, cantidad, precio y categoría.
- **Eliminar Producto**: Elimina un producto del inventario según su ID.
- **Buscar Producto**: Permite buscar productos por ID, nombre o categoría.
- **Reporte de Bajo Stock**: Genera un reporte mostrando los productos cuya cantidad esté por debajo de un límite especificado.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3.x y algunas bibliotecas, como:

- **sqlite3** (ya incluido con Python)
- **colorama** (para mejorar la salida visual en la terminal)

## Instalación
1. Clona el repositorio:
   
  ```
     git clone https://github.com/tu_usuario/gestor-inventario-python.git
     cd gestor-inventario-python
  ```
2. Crea y activa un entorno virtual:

  ```
     python -m venv venv
     .\venv\Scripts\activate
  ```
3. Instala las dependencias:

  ```
     pip install colorama
  ```
4. Ejecuta el sistema:

  ```
     python app.py
  ```
## Uso
Cuando ejecutas el programa, se te presentará un menú interactivo con las siguientes opciones:

1. Agregar Producto
2. Mostrar Productos
3. Actualizar Producto
4. Eliminar Producto
5. Buscar Producto
6. Reporte de Bajo Stock
7. Salir

Cada opción te guiará a través del proceso correspondiente. La base de datos inventario.db se utiliza para almacenar todos los productos y su información.

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad)
3. Realiza tus cambios y haz commit (git commit -am 'Agrega nueva funcionalidad')
4. Sube tus cambios (git push origin feature/nueva-funcionalidad)
5. Crea un pull request
   
