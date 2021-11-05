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
    Email = input("Ingrese el email:")
    Telefono = input("Ingrese su telefono: \t")
    sql = "INSERT INTO Proveedor (Nombre,Email,Telefono) VALUES (%s,%s,%s)"
    val  = [(Nombre,Email,Telefono)]
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
    descripcion = input("Ingrese Nombre de los productos\n")
    stock = input("Ingrese su stock\n")
    precio = input("Ingrese precio\n")
    sql = "INSERT INTO Productos (Descripcion,Cantidad,Precio) VALUES (%s,%s,%s)"
    val  = [(descripcion,stock,precio)]
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

def altaProductoProveedor():
    Nombre = input("Ingrese su nombre: \t")
    Descripcion = input("Ingrese la descripcion: \t")
    Precio = input("Ingrese el precio: \t")
    ID_Proveedor = input("Ingrese el Id del proveedor: \t")
    sql = "INSERT INTO Productos_Proveedor (Nombre,Descripcion,Precio,ID_Proveedor) VALUES (%s,%s,%s,%s)"
    val  = [(Nombre,Descripcion,Precio,ID_Proveedor)]
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
    Id_Venta = input("Ingrese el id de la venta: \t")
    Id_Cliente = input("Ingrese el id del cliente: \t")
    sql = "INSERT INTO Compras (ID_Venta, ID_Cliente) VALUES (%s,%s)"
    val  = [(Id_Venta, Id_Cliente)]
    db.ejecutarSQL_VAL(sql,val)

def borrarCompra(ID):
    db.ejecutarSQL("DELETE FROM Compras WHERE ID_Venta="+ID)

def modificarCompra(ID_MOD):
    Id_Venta = input("Ingrese el nuevo Id de la venta: \t")
    Id_Cliente = input("Ingrese el nuevo Id del cliente: \t")
    sql = "UPDATE Compras SET ID_Venta=%s, ID_Cliente WHERE ID_Venta=%s"
    val  = [(Id_Venta, Id_Cliente,ID)]
    db.ejecutarSQL_VAL(sql,val)
