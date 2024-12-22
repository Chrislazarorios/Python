# imports
import sqlite3
from colorama import init, Fore, Back, Style
import os

os.system("clear")
# iniciar colorama
init(autoreset=True)



# conexion a db
def conectar(database):
    conexion = sqlite3.connect(database)
    return conexion



# crear tabla en db
def crear_tabla():
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT NOT NULL, 
        nombre TEXT NOT NULL,
        descripcion TEXT NULL,
        cantidad INTEGER NOT NULL,
        precio FLOAT NOT NULL, 
        talle TEXT NOT NULL,
        color TEXT NOT NULL)
        """
    )

    conn.commit()

    conn.close()


# crear tabla

crear_tabla()

# functions

# insertar

def insertar_producto():
    codigo = int(input("Ingrese el codigo del producto: "))
    nombre = input("Ingrese nombre del producto: ")
    descripcion = input("Ingrese descripcion del producto: ")
    cantidad = int(input("Ingrese cantidad del producto: "))
    precio = float(input("Ingrese precio del producto: "))
    talle = input("Ingrese talle del producto: ")
    color = input("Ingrese color del producto: ")

    # conectar a db
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo FROM productos WHERE codigo = ?", (codigo,))
    respuesta = cursor.fetchone()
    if respuesta is None:
        cursor.execute(
            "INSERT INTO productos (codigo, nombre, descripcion, cantidad, precio, talle, color) VALUES (?,?,?,?,?,?,?)",
            (codigo, nombre, descripcion, cantidad, precio, talle, color)
        )
        conn.commit()
        print("Producto insertado con exito\n")
    else:
        print(f"{Fore.YELLOW}\nError. Codigo existente, ingrese otro codigo\n{Style.RESET_ALL}")
    
    conn.close()


# mostrar
def mostrar_productos():
    # connection
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    respuesta = cursor.fetchall()
    if len(respuesta) > 0:
        print(f"{Fore.YELLOW}Lista de productos")
        for item in respuesta:
            print(
                f""" {Fore.MAGENTA}ID: {item[0]} | CODIGO {item[1]} | NOMBRE {item[2]} | DESC {item[3]} | CANTIDAD {item[4]} | PRECIO ${item[5]} | TALLE {item[6]} | COLOR {item[7]} """
            )
        print("\n")
    else:
        print("No hay productos\n")
    conn.close()


# buscar
def buscar_producto():
    codigo = input("Ingrese código del producto a buscar: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE codigo = ? ", (codigo,))
    item = cursor.fetchone()
    if item != None:
        print("Producto encontrado")
        print(
            f""" {Fore.MAGENTA}ID: {item[0]} | CODIGO {item[1]} | NOMBRE {item[2]} | DESC {item[3]} | CANTIDAD {item[4]} | PRECIO ${item[5]} | TALLE {item[6]} | COLOR {item[7]} """
            )
        print("\n")
    else:
       print(f"{Fore.YELLOW}Producto no encontrado, código inexistente\n")
    conn.close()


# actualizar
def actualizar_cantidad():
    codigo = input("Ingrese código del producto a actualizar: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT cantidad FROM productos WHERE codigo = ?", (codigo))
    cantActual = cursor.fetchone()

    if cantActual != None:
        print("Cantidad actual del producto:", cantActual[0])
        nueva_cantidad = input("Ingrese nueva cantidad del producto a actualizar: ")
        cursor.execute("UPDATE productos SET cantidad = ? WHERE codigo = ?", (nueva_cantidad, codigo,))
        conn.commit()
        print("Producto actualizado con exito\n")
    else:
        print(f"{Fore.YELLOW}Producto no encontrado, código inexistente\n")
    conn.close()

# eliminar
def eliminar_producto():
    codigo = input("Ingrese código del producto a eliminar: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT codigo FROM productos WHERE codigo = ? ", (codigo,))
    respuesta = cursor.fetchone()
    if respuesta != None:
        cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
        conn.commit()
        print("Producto eliminado con exito\n")
    else:
        print(f"{Fore.YELLOW}Producto no encontrado, código inexistente\n")
    conn.close()


# reporte
def reporte_bajo_stock():
    bajo_stock = input("Ingrese la cantidad de stock que considere baja: ")
    conn = conectar("inventario.db")
    cursor = conn.cursor()
    cursor.execute("SELECT  * FROM productos WHERE cantidad < ?", (bajo_stock,))
    respuesta = cursor.fetchall()
    if len(respuesta) > 0:
        print(f"{Fore.YELLOW}Productos con bajo stock")
        for item in respuesta:
            print(
                f""" {Fore.MAGENTA}ID: {item[0]} | CODIGO {item[1]} | NOMBRE {item[2]} | DESC {item[3]} | CANTIDAD {item[4]} | PRECIO ${item[5]} | TALLE {item[6]} | COLOR {item[7]} """
            )
        print("\n")
    else:
        print("No hay productos con bajo stock\n")
    conn.close()
    

def mostrar_menu():
    while True:
        print(
            f"{Back.BLUE}{Fore.RED} {Style.BRIGHT}Seleccione una opción para comenzar a operar el sistema:"
        )
        print(
            Fore.GREEN
            + """
    1-Ingresar producto
    2-Mostrar productos
    3-Buscar producto
    4-Actualizar producto
    5-Eliminar producto
    6-Reporte bajo stock
    7-Salir
        """
        )

        # Ingreso de datos
        opcion = input(f"{Fore.YELLOW}Opción: {Style.RESET_ALL}")

        if opcion == "1":
            insertar_producto()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            actualizar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            reporte_bajo_stock()
        elif opcion == "7":
            print("Saliendo del sistema")
            break
        else:
            print("Opcion no válida")


mostrar_menu()


