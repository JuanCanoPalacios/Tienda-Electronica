import BD

def Mostrar(Tabla):
    BD.Mostrar("SELECT * FROM "+Tabla)

                                                    ##CLIENTE
def CrearCliente():
    Nombre = input("Ingrese su nombre: \t")
    Telefono = input("Ingrese su telefono: \t")
    Direccion = input("Ingrese email: \t")
    sql = "INSERT INTO Clientes (Nombre,Telefono,Direccion) VALUES (%s,%s,%s)"
    val  = [(Nombre,Telefono,Direccion)]
    BD.EjecutarSQL_VAL(sql,val)

def BorrarCliente(ID):
    BD.EjecutarSQL("DELETE FROM Clientes WHERE ID_Cliente="+ID)

def ModificarCliente(ID_MOD):
    Nombre = input("Ingrese su nombre: \t")
    Telefono = input("Ingrese su Telefono: \t")
    Direccion = input("Ingrese Direccion: \t")
    sql = ("UPDATE Clientes SET Nombre=%s,Telefono=%s,Direccion=%s WHERE ID_Cliente=%s")
    val  = [(Nombre,Telefono,Direccion,ID_MOD)]
    BD.EjecutarSQL_VAL(sql,val)
 
                                                    ##PROVEEDOR
def CrearProveedor():
    Nombre = input("Ingrese su nombre: \t")
    Email = input("Ingrese el email:")
    Telefono = input("Ingrese su telefono: \t")
    sql = "INSERT INTO Proveedor (Nombre,Email,Telefono) VALUES (%s,%s,%s)"
    val  = [(Nombre,Email,Telefono)]
    BD.EjecutarSQL_VAL(sql,val)

def BorrarProveedor(ID):
    BD.EjecutarSQL("DELETE FROM Proveedor WHERE ID_Proveedor="+ID)

def ModificarProveedor(ID_MOD):
    Nombre = input("Ingrese su nombre: \t")
    Telefono = input("Ingrese su telefono: \t")
    Email = input("Ingrese email: \t")
    sql = ("UPDATE Proveedor SET Nombre=%s,Telefono=%s, Email=%s WHERE ID_Proveedor=%s")
    val  = [(Nombre,Telefono,Email,ID_MOD)]
    BD.EjecutarSQL_VAL(sql,val)
                                                    ##PRODUCTOS
def CrearProductos():
    descripcion = input("Ingrese los productos\n")
    stock = input("Ingrese su stock\n")
    precio = input("Ingrese precio\n")
    sql = "INSERT INTO Productos (Descripcion,Id_Stock,Precio) VALUES (%s,%s,%s)"
    val  = [(descripcion,stock,precio)]
    BD.EjecutarSQL_VAL(sql,val)

def BorrarProductos(ID):
    BD.EjecutarSQL("DELETE FROM Productos WHERE ID_Producto="+ID)

def ModificarProductos(ID_MOD):
    descripcion = input("Ingrese la nueva descripcion: \t")
    Cantidad = input("Ingrese la nueva Cantidad: \t")
    precio = input("Ingrese el nuevo precio: \t")
    sql = ("UPDATE Productos SET Descripcion=%s,Cantidad=%s,Precio=%s WHERE ID_Producto=%s")
    val  = [(descripcion,Cantidad,precio,ID_MOD)]
    BD.EjecutarSQL_VAL(sql,val)

def AltaProductoProveedor():
    Nombre = input("Ingrese su nombre: \t")
    Descripcion = input("Ingrese la descripcion: \t")
    Precio = input("Ingrese el precio: \t")
    ID_Proveedor=input("Ingrese el Id del proveedor: \t")
    sql = "INSERT INTO Productos_Proveedor (Nombre,Descripcion,Precio,ID_Proveedor) VALUES (%s,%s,%s,%s)"
    val  = [(Nombre,Descripcion,Precio,ID_Proveedor)]
    BD.EjecutarSQL_VAL(sql,val)

def BajaProductoProveedor(ID):
    BD.EjecutarSQL("DELETE FROM Productos_Proveedor WHERE ID_Producto="+ID)

def ModificarProductoProveedor(ID_MOD):
    Nombre = input("Ingrese el nuevo nombre: \t")
    Descripcion = input("Ingrese la nueva descripcion: \t")
    Precio = input("Ingrese el nuevo precio: \t")
    ID_Proveedor=input("Ingrese el nuevo Id del proveedor: \t")
    sql = "UPDATE Productos_Proveedor SET Nombre=%s,Descripcion=%s,Precio=%s,ID_Proveedor=%s WHERE ID_Producto=%s"
    val  = [(Nombre,Descripcion,Precio,ID_Proveedor,ID_MOD)]
    BD.EjecutarSQL_VAL(sql,val)

def RealizarVenta():
    pass

def BorrarVenta(ID):
    BD.EjecutarSQL("DELETE FROM Ventas WHERE ID_Venta="+ID)

def ModificarVenta(ID):
    pass
