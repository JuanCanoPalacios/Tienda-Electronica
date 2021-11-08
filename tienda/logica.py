
import db
import time

def mostrar(Tabla):
    db.mostrar("SELECT * FROM "+Tabla)

#CLIENTE
def crearCliente():
    Nombre = input("Ingrese su nombre: \t")
    Telefono = input("Ingrese su telefono: \t")
    Direccion = input("Ingrese email: \t")
    sql = "INSERT INTO Clientes (Nombre,Telefono,Direccion) VALUES (%s,%s,%s)"
    val  = [(Nombre,Telefono,Direccion)]
    db.ejecutarSQL_VAL(sql,val)

def borrarCliente(ID):
    db.ejecutarSQL("DELETE FROM Clientes WHERE ID_Cliente="+ID)

def modificarCliente(ID_MOD):
    Nombre = input("Ingrese su nombre: \t")
    Telefono = input("Ingrese su Telefono: \t")
    Direccion = input("Ingrese Direccion: \t")
    sql = ("UPDATE Clientes SET Nombre=%s,Telefono=%s,Direccion=%s WHERE ID_Cliente=%s")
    val  = [(Nombre,Telefono,Direccion,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#PROVEEDOR
def crearProveedor():
    Nombre = input("Ingrese su nombre: \t")
    Telefono = input("Ingrese su telefono: \t")
    sql = "INSERT INTO Proveedor (Nombre,Telefono) VALUES (%s,%s)"
    val  = [(Nombre,Telefono)]
    db.ejecutarSQL_VAL(sql,val)

def borrarProveedor(ID):
    db.ejecutarSQL("DELETE FROM Proveedor WHERE ID_Proveedor="+ID)

def modificarProveedor(ID_MOD):
    Nombre = input("Ingrese su nombre: \t")
    Telefono = input("Ingrese su telefono: \t")
    Email = input("Ingrese email: \t")
    sql = ("UPDATE Proveedor SET Nombre=%s,Telefono=%s, Email=%s WHERE ID_Proveedor=%s")
    val  = [(Nombre,Telefono,Email,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#PRODUCTOS
def crearProductos():
    descripcion = input("Ingrese nombre del producto:\t")
    precio = input("Ingrese precio:\t")
    cantidad = input("Ingrese su stock actual:\t")
    sql = "INSERT INTO Productos (Descripcion,Precio,Cantidad) VALUES (%s,%s,%s)"
    val  = [(descripcion,precio,cantidad)]
    db.ejecutarSQL_VAL(sql,val)

def borrarProductos(ID):
    db.ejecutarSQL("DELETE FROM Productos WHERE ID_Producto="+ID)

def modificarProductos(ID_MOD):
    descripcion = input("Ingrese la nueva descripcion: \t")
    Cantidad = input("Ingrese la nueva Cantidad: \t")
    precio = input("Ingrese el nuevo precio: \t")
    sql = ("UPDATE Productos SET Descripcion=%s,Cantidad=%s,Precio=%s WHERE ID_Producto=%s")
    val  = [(descripcion,Cantidad,precio,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)
#ProductoProveedor
def altaProductoProveedor():
    ID_Producto =  input("Ingrese el ID del producto al cual hace referencia:\t")
    ID_Productos_Proveedor = input("Ingrese el ID del producto del proveedor:\t")
    ID_Proveedor = input("Ingrese el Id del proveedor: \t")
    Precio = input("Ingrese el costo del producto:\t")
    sql = "INSERT INTO Productos_Proveedor (ID_Producto,ID_Productos_Proveedor,ID_Proveedor) VALUES (%s,%s,%s,%s)"
    val  = [(ID_Producto,ID_Productos_Proveedor,ID_Proveedor,Precio)]
    db.ejecutarSQL_VAL(sql,val)

def bajaProductoProveedor(ID):
    db.ejecutarSQL("DELETE FROM Productos_Proveedor WHERE ID_Producto="+ID)

def modificarProductoProveedor(ID_MOD):
    Nombre = input("Ingrese el nuevo nombre: \t")
    Descripcion = input("Ingrese la nueva descripcion: \t")
    Precio = input("Ingrese el nuevo precio: \t")
    ID_Proveedor=input("Ingrese el nuevo Id del proveedor: \t")
    sql = "UPDATE Productos_Proveedor SET Nombre=%s,Descripcion=%s,Precio=%s,ID_Proveedor=%s WHERE ID_Producto=%s"
    val  = [(Nombre,Descripcion,Precio,ID_Proveedor,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#Ventas
def realizarVenta():
    Id_Cliente = input("Ingrese el id del cliente: \t")
    Id_Producto = input("Ingrese el id del producto: \t")
    sql = "INSERT INTO Ventas (ID_Cliente, ID_Producto) VALUES (%s,%s)"
    val  = [(Id_Cliente,Id_Producto)]
    db.ejecutarSQL_VAL(sql,val)

def borrarVenta(ID):
    db.ejecutarSQL("DELETE FROM Ventas WHERE ID_Venta="+ID)

def modificarVenta(ID):
    Id_Cliente = input("Ingrese el nuevo Id del cliente: \t")
    Id_Producto = input("Ingrese el nuevo Id del producto: \t")
    sql = "UPDATE Ventas SET ID_Cliente=%s, ID_Producto WHERE ID_Venta=%s"
    val  = [(Id_Cliente,Id_Producto,ID)]
    db.ejecutarSQL_VAL(sql,val)
#Compras
def crearCompra():
    ID_ProductoProveedor = input("Ingrese el id del cliente: \t")
    Cantidad = input("Ingrese la cantidad del prodcuto a comprar:\t")
    sql = "INSERT INTO Compras (ID_Venta, ID_C) VALUES (%s,%s,%s)"
    val  = [(ID_Producto_Proveedor, Cantidad)]
    db.ejecutarSQL_VAL(sql,val)

def borrarCompra(ID):
    db.ejecutarSQL("DELETE FROM Compras WHERE ID_Venta="+ID)

def modificarCompra(ID_MOD):
    ID_ProductoProveedor = input("Ingrese el nuevo ID del proveedor:\t")
    Cantidad = input("Ingrese la nueva cantidad de la compra:\t")
    sql = "UPDATE Compras SET ID_Producto_Proveedor=%s, Cantidad WHERE ID_Compra=%s"
    val  = [(ID_ProductoProveedor, Cantidad,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)
