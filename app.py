import sqlite3
import colorama
from colorama import Fore, Style

# Inicializar colorama para que funcione en Windows y otros sistemas
colorama.init(autoreset=True)

# Crear la base de datos y la tabla si no existen
def crear_base_de_datos():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL
    )
    """)
    conexion.commit()
    conexion.close()

# Función para registrar un producto
def registrar_producto():
    print(Fore.CYAN + "\n--- Registrar Producto ---" + Style.RESET_ALL)
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    cantidad = int(input("Cantidad del producto: "))
    precio = float(input("Precio del producto: "))
    categoria = input("Categoría del producto: ")

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute("""
    INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
    VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Producto registrado con éxito." + Style.RESET_ALL)

# Función para visualizar todos los productos
def visualizar_productos():
    print(Fore.YELLOW + "\n--- Visualizar Productos ---" + Style.RESET_ALL)
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        # Imprime un encabezado para mejorar la organización
        print(Fore.GREEN + f"{'ID':<6} {'Nombre':<25} {'Descripción':<45} {'Cantidad':<12} {'Precio':<12} {'Categoría':<20}" + Style.RESET_ALL)
        print("-" * 120)  # Línea separadora

        # Itera sobre los productos y los mostramos en formato organizado
        for producto in productos:
            print(Fore.MAGENTA + f"{producto[0]:<6} {producto[1]:<25} {producto[2]:<45} {producto[3]:<12} ${producto[4]:<12} {producto[5]:<20}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "No hay productos registrados." + Style.RESET_ALL)



# Función para actualizar la cantidad de un producto
def actualizar_producto():
    print(Fore.CYAN + "\n--- Actualizar Producto ---" + Style.RESET_ALL)
    id_producto = int(input("Ingrese el ID del producto a actualizar: "))

    # Conectar a la base de datos
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    # Consultar el producto actual
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()

    # Verificar si el producto existe
    if producto:
        # Mostrar los datos actuales del producto
        print("\nProducto encontrado:")
        print(f"ID: {producto[0]} - Nombre: {producto[1]} - Descripción: {producto[2]} - Cantidad: {producto[3]} - Precio: {producto[4]} - Categoría: {producto[5]}")

        # Solicitar nuevos datos para el producto, dejar los actuales si no se ingresan nuevos valores
        nombre = input(f"Nuevo nombre ({producto[1]}): ")
        descripcion = input(f"Nueva descripción ({producto[2]}): ")
        cantidad = input(f"Nueva cantidad ({producto[3]}): ")
        precio = input(f"Nuevo precio ({producto[4]}): ")
        categoria = input(f"Nueva categoría ({producto[5]}): ")

        # Si no se ingresan nuevos valores, se mantienen los actuales
        nombre = nombre if nombre else producto[1]
        descripcion = descripcion if descripcion else producto[2]
        cantidad = int(cantidad) if cantidad else producto[3]
        precio = float(precio) if precio else producto[4]
        categoria = categoria if categoria else producto[5]

        # Actualizar los datos del producto en la base de datos
        cursor.execute("""
            UPDATE productos
            SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
            WHERE id = ?
        """, (nombre, descripcion, cantidad, precio, categoria, id_producto))

        conexion.commit()
        print(Fore.GREEN + "Producto actualizado con éxito." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Producto no encontrado con ese ID." + Style.RESET_ALL)

    # Cerrar la conexión
    conexion.close()

# Función para eliminar un producto
def eliminar_producto():
    print(Fore.RED + "\n--- Eliminar Producto ---" + Style.RESET_ALL)
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
    conexion.commit()
    conexion.close()

    print(Fore.GREEN + "Producto eliminado con éxito." + Style.RESET_ALL)

# Función para obtener productos de la base de datos
def obtener_productos():
    conexion = sqlite3.connect('inventario.db')  # Conexión a la base de datos
    cursor = conexion.cursor()

    # Consulta para obtener todos los productos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()  # Obtener todos los productos

    conexion.close()  # Cerrar la conexión
    return productos

# Función para obtener productos de la base de datos
def obtener_productos():
    conexion = sqlite3.connect('inventario.db')  # Conexión a la base de datos
    cursor = conexion.cursor()

    # Consulta para obtener todos los productos
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()  # Obtener todos los productos

    conexion.close()  # Cerrar la conexión
    return productos

# Función para buscar un producto por ID, nombre o categoría
def buscar_producto():
    # Obtener productos desde la base de datos
    productos = obtener_productos()

    # Preguntar al usuario qué criterio usar para la búsqueda
    criterio = input(Fore.CYAN + "¿Buscar por ID, nombre o categoría? (ingrese ID/nombre/categoría): ").lower()

    if criterio not in ['id', 'nombre', 'categoría']:
        print(Fore.RED + "Criterio no válido.")
        return

    # Si el criterio es ID, se solicita el ID y se busca por ese campo
    if criterio == 'id':
        try:
            producto_id = int(input(Fore.GREEN + "Ingrese el ID del producto: "))
            producto_encontrado = False
            for producto in productos:
                if producto[0] == producto_id:  # Asumiendo que el ID está en la primera columna
                    print(Fore.YELLOW + f"\nProducto encontrado:")
                    print(Fore.YELLOW + f"{'ID':<10}: {producto[0]}")
                    print(Fore.YELLOW + f"{'Nombre':<10}: {producto[1]}")
                    print(Fore.YELLOW + f"{'Descripción':<10}: {producto[2]}")
                    print(Fore.YELLOW + f"{'Cantidad':<10}: {producto[3]}")
                    print(Fore.YELLOW + f"{'Precio':<10}: ${producto[4]}")
                    print(Fore.YELLOW + f"{'Categoría':<10}: {producto[5]}")
                    producto_encontrado = True
                    break
            if not producto_encontrado:
                print(Fore.RED + "Producto no encontrado.")
        except ValueError:
            print(Fore.RED + "Por favor ingrese un ID válido.")
        
    # Si el criterio es nombre, se solicita el nombre del producto
    elif criterio == 'nombre':
        nombre_producto = input(Fore.GREEN + "Ingrese el nombre del producto: ").lower()
        producto_encontrado = False
        for producto in productos:
            if nombre_producto in producto[1].lower():  # Compara el nombre, que está en la segunda columna
                print(Fore.YELLOW + f"\nProducto encontrado:")
                print(Fore.YELLOW + f"{'ID':<10}: {producto[0]}")
                print(Fore.YELLOW + f"{'Nombre':<10}: {producto[1]}")
                print(Fore.YELLOW + f"{'Descripción':<10}: {producto[2]}")
                print(Fore.YELLOW + f"{'Cantidad':<10}: {producto[3]}")
                print(Fore.YELLOW + f"{'Precio':<10}: ${producto[4]}")
                print(Fore.YELLOW + f"{'Categoría':<10}: {producto[5]}")
                producto_encontrado = True
        if not producto_encontrado:
            print(Fore.RED + "Producto no encontrado.")

    # Si el criterio es categoría, se solicita la categoría
    elif criterio == 'categoría':
        categoria_producto = input(Fore.GREEN + "Ingrese la categoría del producto: ").lower()
        producto_encontrado = False
        for producto in productos:
            if categoria_producto in producto[5].lower():  # Compara la categoría, que está en la sexta columna
                print(Fore.YELLOW + f"\nProducto encontrado:")
                print(Fore.YELLOW + f"{'ID':<10}: {producto[0]}")
                print(Fore.YELLOW + f"{'Nombre':<10}: {producto[1]}")
                print(Fore.YELLOW + f"{'Descripción':<10}: {producto[2]}")
                print(Fore.YELLOW + f"{'Cantidad':<10}: {producto[3]}")
                print(Fore.YELLOW + f"{'Precio':<10}: ${producto[4]}")
                print(Fore.YELLOW + f"{'Categoría':<10}: {producto[5]}")
                producto_encontrado = True
        if not producto_encontrado:
            print(Fore.RED + "Producto no encontrado.")


# Función para generar un reporte de productos con bajo stock
def reporte_bajo_stock():
    print(Fore.RED + "\n--- Reporte de Bajo Stock ---" + Style.RESET_ALL)
    limite_stock = int(input("Ingrese el límite de stock para el reporte: "))

    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite_stock,))
    productos = cursor.fetchall()
    conexion.close()

    if productos:
        for producto in productos:
            print(Fore.MAGENTA + f"ID: {producto[0]} - Nombre: {producto[1]} - Cantidad: {producto[3]} - Precio: ${producto[4]} - Categoría: {producto[5]}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "No hay productos con bajo stock." + Style.RESET_ALL)

# Función para mostrar el menú principal y manejar las opciones
def menu_principal():
    while True:
        print(Fore.CYAN + "\n--- Menú Principal ---" + Style.RESET_ALL)
        print("1. Agregar Producto")
        print("2. Mostrar Productos")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Buscar Producto")
        print("6. Reporte de Bajo Stock")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            visualizar_productos()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            buscar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print(Fore.GREEN + "Saliendo del sistema... Gracias por usar la aplicación." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Intente nuevamente." + Style.RESET_ALL)

# Función principal de ejecución
def main():
    crear_base_de_datos()
    menu_principal()

if __name__ == "__main__":
    main()
