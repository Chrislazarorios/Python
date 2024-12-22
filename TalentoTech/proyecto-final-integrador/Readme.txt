Esta aplicación administra una tienda de ropa, y posee las siguientes funcionalidades:

- insertar_producto
    Ingresa una prenda de ropa a la base de datos
    codigo
    nombre
    descripcion
    cantidad
    precio
    talle
    color

    Cada producto debe tener un codigo unico
- mostrar_productos
    Muestra la ropa ingresada en la base de datos
- buscar_producto
    Busca una prenda de ropa por codigo
- actualizar_cantidad
    Actualiza la cantidad de una prenda de ropa por codigo
- eliminar_producto
    Elimina una prenda de ropa por codigo
- reporte_bajo_stock
    Informe de productos con bajo stock segun indique el usuario

Ademas emplea las siguientes funciones para crear una conexion a sqlite:

- conectar
- crear_tabla

Todas las funciones poseen validaciones para evitar el ingreso de informacion inválida

- insertar_producto
    Si el codigo ingresado ya existe, el producto no se ingresa y retorna un error

- mostrar_productos
    Si no hay productos que mostrar, retorna un error

- buscar_producto
    Si el codigo ingresado no existe, el producto no se encuentra y retorna un error

- actualizar_cantidad
    Si el codigo ingresado no existe, el producto no se actualiza y retorna un error

- eliminar_producto
    Si el codigo ingresado no existe, el producto no se elimina y retorna un error

- reporte_bajo_stock
    Si la cantidad de stock buscada no existe, retorna un error