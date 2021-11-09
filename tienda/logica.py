import db

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
    sql = ("UPDATE Productos SET Descripcion=%s,Precio=%s,Cantidad=%s WHERE ID_Producto=%s")
    val  = [(descripcion,precio,Cantidad,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#ProductoProveedor
def altaProductoProveedor():
    ID_Producto =  input("Ingrese el ID del producto al cual hace referencia:\t")
    ID_Proveedor = input("Ingrese el Id del proveedor: \t")
    Precio = input("Ingrese el costo del producto:\t")
    sql = "INSERT INTO Productos_Proveedor (ID_Producto,ID_Proveedor,Precio) VALUES (%s,%s,%s)"
    val  = [(ID_Producto,ID_Proveedor,Precio)]
    db.ejecutarSQL_VAL(sql,val)

def bajaProductoProveedor(ID):
    db.ejecutarSQL("DELETE FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID)

def modificarProductoProveedor(ID_MOD):
    ID_Producto =  input("Ingrese el ID del producto al cual hace referencia:\t")
    ID_Proveedor = input("Ingrese el Id del proveedor: \t")
    Precio = input("Ingrese el costo del producto:\t")
    sql = "UPDATE Productos_Proveedor SET ID_Producto=%s,ID_Proveedor=%s,Precio=%s WHERE ID_Productos_Proveedor=%s"
    val  = [(ID_Producto,ID_Proveedor,Precio,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#Ventas
def realizarVenta():#Falta que cuando se realice una venta se baje el stock
    Id_Cliente = input("Ingrese el id del cliente: \t")
    Id_Producto = input("Ingrese el id del producto: \t")
    sql = "INSERT INTO Ventas (ID_Cliente, ID_Producto) VALUES (%s,%s)"
    val  = [(Id_Cliente,Id_Producto)]
    db.ejecutarSQL_VAL(sql,val)

def borrarVenta(ID):#Cuando se borre una venta se sume el stock de la misma
    db.ejecutarSQL("DELETE FROM Ventas WHERE ID_Venta="+ID)

def modificarVenta(ID_MOD):#Cuando se modifique una venta se debera cambiar el stock
    ID_Cliente = input("Ingrese el nuevo Id del cliente: \t")
    ID_Producto = input("Ingrese el nuevo Id del producto: \t")
    sql = "UPDATE Ventas SET ID_Cliente=%s, ID_Producto=%s WHERE ID_Venta=%s"
    val  = [(ID_Cliente,ID_Producto,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)

#Compras
def crearCompra():#Teoricamente esto esta terminado
    ID_Producto_Proveedor = input("Ingrese el ID del Producto del Proveedor:\t")
    Cantidad = input("Ingrese la cantidad del producto a comprar:\t")
    sql = "INSERT INTO Compras (ID_Producto_Proveedor, Cantidad) VALUES (%s,%s)"
    val  = [(ID_Producto_Proveedor, Cantidad)]
    db.ejecutarSQL_VAL(sql,val)
    ID_Producto=db.dato("SELECT * FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID_Producto_Proveedor)[0]
    mod_id=str(ID_Producto[0])
    Producto=db.dato('SELECT * FROM Productos WHERE ID_Producto='+mod_id+'')
    cantidad=int(Cantidad)
    cantidad+=int(Producto[0][3])
    sql=("UPDATE Productos SET Descripcion=%s,Precio=%s,Cantidad=%s WHERE ID_Producto=%s")
    val  = [(Producto[0][1],Producto[0][2],str(cantidad),Producto[0][0])]
    db.ejecutarSQL_VAL(sql,val)

def borrarCompra(ID):#Falta que cuando se borre una compra se baje dicha cantidad de stock
    db.ejecutarSQL("DELETE FROM Compras WHERE ID_Compra="+ID)

def modificarCompra(ID_MOD):#Cuando se modifique la compra debera cambiarse respectivamente el stock
    ID_ProductoProveedor = input("Ingrese el nuevo ID del proveedor:\t")
    Cantidad = input("Ingrese la nueva cantidad de la compra:\t")
    sql = "UPDATE Compras SET ID_Producto_Proveedor=%s, Cantidad=%s WHERE ID_Compra=%s"
    val  = [(ID_ProductoProveedor, Cantidad,ID_MOD)]
    db.ejecutarSQL_VAL(sql,val)
