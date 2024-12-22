# Lista para almacenar los productos
productos = []


# Función principal para el sistema de inventario (NO ELIMINAR)
def main():
  # AQUÍ PUEDES COMENZAR A DESARROLLAR LA SOLUCIÓN 
  print("Hola mundo")

  opcion = 0
  
  while opcion != 3:

    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")
    opcion = int(input("Seleccione una opcion(1-3):"))

    
    if opcion in (1,2,3):
      if opcion == 1:
        print("1. Agregar producto")
        nombre = str(input('Ingrese nombre del producto: '))
        cantidad = int(input('Ingrese la cantidad del producto: '))
        producto = [nombre, cantidad]
        productos.append(producto)
        print('Producto agregado con éxito.')
      elif opcion == 2:
        print("2. Mostrar productos")
        if len(productos) == 0:
          print('No hay productos registrados.')
        else:
          print('\nProductos: \n')
          print(productos)
      elif opcion == 3:
        print('\nSaliste del menu\n')
        break
    else:
      print('Opcion inválida')


# Ejecución de la función main() - (NO ELIMINAR)
if __name__ == "__main__":
    main()

