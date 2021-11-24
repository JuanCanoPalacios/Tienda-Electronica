import db
import ui

def mostrar(Tabla):
    db.mostrar("SELECT * FROM "+Tabla)

#Cliente
def crearCliente():
    ui.banner()
    Nombre = input("[*] Ingrese su nombre: \t")
    Telefono = input("[*] Ingrese su telefono: \t")
    Direccion = input("[*] Ingrese email: \t")
    sql = "INSERT INTO Clientes (Nombre,Telefono,Direccion) VALUES (%s,%s,%s)"
    val = [(Nombre,Telefono,Direccion)]
    db.ejecutarSQL_VAL(sql,val)

def borrarCliente(ID):
    db.ejecutarSQL("DELETE FROM Clientes WHERE ID_Cliente="+ID)

def modificarCliente(ID_MOD):
    ui.banner()
    Nombre = input("[*] Ingrese su nombre: \t")
    Telefono = input("[*] Ingrese su Telefono: \t")
    Direccion = input("[*] Ingrese Direccion: \t")
    sql = ("UPDATE Clientes SET Nombre=%s,Telefono=%s,Direccion=%s WHERE ID_Cliente=%s")
    val = [(Nombre,Telefono,Direccion,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#Proveedor
def crearProveedor():
    ui.banner()
    Nombre = input("[*] Ingrese su nombre: \t")
    Telefono = input("[*] Ingrese su telefono: \t")
    Email = input("[*] Ingrese email: \t")
    sql = "INSERT INTO Proveedor (Nombre,Telefono,Email) VALUES (%s,%s,%s)"
    val = [(Nombre,Telefono,Email)]
    db.ejecutarSQL_VAL(sql,val)

def borrarProveedor(ID):
    db.ejecutarSQL("DELETE FROM Proveedor WHERE ID_Proveedor="+ID)

def modificarProveedor(ID_MOD):
    ui.banner()
    Nombre = input("[*] Ingrese su nombre: \t")
    Telefono = input("[*] Ingrese su telefono: \t")
    Email = input("[*] Ingrese email: \t")
    sql = ("UPDATE Proveedor SET Nombre=%s,Telefono=%s, Email=%s WHERE ID_Proveedor=%s")
    val = [(Nombre,Telefono,Email,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#Productos
def crearProductos():
    ui.banner()
    descripcion = input("[*] Ingrese nombre del producto:\t")
    precio = input("[*] Ingrese precio:\t")
    cantidad = input("[*] Ingrese su stock actual:\t")
    sql = "INSERT INTO Productos (Descripcion,Precio,Cantidad) VALUES (%s,%s,%s)"
    val = [(descripcion,precio,cantidad)]
    db.ejecutarSQL_VAL(sql,val)

def borrarProductos(ID):
    db.ejecutarSQL("DELETE FROM Productos WHERE ID_Producto="+ID)

def modificarProductos(ID_MOD):
    ui.banner()
    descripcion = input("[*] Ingrese la nueva descripcion: \t")
    cantidad = input("[*] Ingrese la nueva Cantidad: \t")
    precio = input("[*] Ingrese el nuevo precio: \t")
    sql = ("UPDATE Productos SET Descripcion=%s,Precio=%s,Cantidad=%s WHERE ID_Producto=%s")
    val = [(descripcion,precio,cantidad,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#ProductoProveedor
def altaProductoProveedor():
    ui.banner()
    ID_Producto =  input("[*] Ingrese el ID del producto al cual hace referencia:\t")
    ID_Proveedor = input("[*] Ingrese el ID del proveedor: \t")
    Precio = input("[*] Ingrese el costo del producto:\t")
    sql = "INSERT INTO Productos_Proveedor (ID_Producto,ID_Proveedor,Precio) VALUES (%s,%s,%s)"
    val = [(ID_Producto,ID_Proveedor,Precio)]
    db.ejecutarSQL_VAL(sql,val)

def bajaProductoProveedor(ID):
    db.ejecutarSQL("DELETE FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID)

def modificarProductoProveedor(ID_MOD):
    ui.banner()
    ID_Producto =  input("[*] Ingrese el ID del producto al cual hace referencia:\t")
    ID_Proveedor = input("[*] Ingrese el ID del proveedor: \t")
    Precio = input("[*] Ingrese el costo del producto:\t")
    sql = "UPDATE Productos_Proveedor SET ID_Producto=%s,ID_Proveedor=%s,Precio=%s WHERE ID_Productos_Proveedor=%s"
    val = [(ID_Producto,ID_Proveedor,Precio,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#Ventas
def realizarVenta():#A testear
    ui.banner()
    ID_Cliente = input("[*] Ingrese el ID del cliente: \t")
    ID_Producto = input("[*] Ingrese el ID del producto: \t")
    Cantidad = input("[*] Ingrese la cantidad deseada: \t")
    cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_Producto)[0][0])
    sql = "INSERT INTO Ventas (ID_Cliente, ID_Producto, Cantidad) VALUES (%s,%s,%s)"
    val = [(ID_Cliente,ID_Producto,Cantidad)]
    db.ejecutarSQL_VAL(sql,val)
    sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
    val = [(str(cantidad_actual-int(Cantidad)), ID_Producto)]
    db.ejecutarSQL_VAL(sql,val)

def borrarVenta(ID):#A testear
    ID_Producto = (db.dato("SELECT ID_Producto FROM Ventas WHERE ID_Venta="+ID)[0][0])
    cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_Producto)[0][0])
    cantidad_venta = int(db.dato("SELECT Cantidad FROM Ventas WHERE ID_Venta="+ID)[0][0])
    sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
    val = [(str(cantidad_actual+cantidad_venta), ID_Producto)]
    db.ejecutarSQL_VAL(sql,val)
    db.ejecutarSQL("DELETE FROM Ventas WHERE ID_Venta="+ID)

def modificarVenta(ID_MOD):#A testear
    ui.banner()
    cantidad = input("[*] Ingrese la nueva cantidad: \t")
    ID_Producto = (db.dato("SELECT ID_Producto FROM Ventas WHERE ID_Venta="+ID_MOD)[0][0])
    cantidad_venta = int(db.dato("SELECT Cantidad FROM Ventas WHERE ID_Venta="+ID_MOD)[0][0])
    cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_Producto)[0][0])
    sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
    val = [(str(cantidad_actual-cantidad_venta+cantidad), ID_Producto)]
    db.ejecutarSQL_VAL(sql,val)
    sql = "UPDATE Ventas SET ID_Cliente=%s, ID_Producto=%s, Cantidad=%s WHERE ID_Venta=%s"
    val = [(ID_Cliente,ID_Producto,Cantidad,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#Compras
def crearCompra():#Testeado
    ui.banner()
    ID_Producto_Proveedor = input("[*] Ingrese el ID del Producto del Proveedor:\t")
    Cantidad = input("[*] Ingrese la cantidad del producto a comprar:\t")
    sql = "INSERT INTO Compras (ID_Producto_Proveedor, Cantidad) VALUES (%s,%s)"
    val = [(ID_Producto_Proveedor, Cantidad)]
    db.ejecutarSQL_VAL(sql,val)
    ID_Producto = (db.dato("SELECT ID_Producto FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID_Producto_Proveedor)[0][0])
    cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto = "+ID_Producto)[0][0])
    sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
    val = [(str(cantidad_actual+int(Cantidad)),ID_Producto)]
    db.ejecutarSQL_VAL(sql,val)

def borrarCompra(ID):#Testeado
    cantidad=int(db.dato("SELECT Cantidad FROM Compras WHERE ID_Compra="+ID)[0][0])
    ID_Producto_Proveedor=str(db.dato("SELECT ID_Producto_Proveedor FROM Compras WHERE ID_Compra="+ID)[0][0])
    ID_Producto = str(db.dato("SELECT ID_Producto FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID_Producto_Proveedor)[0][0])
    cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_Producto)[0][0])
    sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
    val = [(str(cantidad_actual-cantidad),ID_Producto)]
    db.ejecutarSQL_VAL(sql,val)
    db.ejecutarSQL("DELETE FROM Compras WHERE ID_Compra="+ID)

def modificarCompra(ID_MOD):#Testeado
    ui.banner()
    ID_ProductoProveedor = input("[*] Ingrese el ID del producto a modificar:\t")
    Cantidad = input("[*] Ingrese la nueva cantidad de la compra:\t")
    cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_ProductoProveedor)[0][0])
    cantidad_compra = int(db.dato("SELECT Cantidad FROM Compras WHERE ID_Compra="+ID_MOD)[0][0])
    sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
    val = [(str(cantidad_actual-cantidad_compra+int(Cantidad)), ID_ProductoProveedor)]
    db.ejecutarSQL_VAL(sql,val)
    sql = "UPDATE Compras SET ID_Producto_Proveedor=%s, Cantidad=%s WHERE ID_Compra=%s"
    val = [(ID_ProductoProveedor,Cantidad,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)
