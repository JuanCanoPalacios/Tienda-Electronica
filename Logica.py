import BD

def MostrarTodosClientes():
    BD.Mostrar("SELECT * FROM Usuarios")

def MostrarProductos():
    BD.Mostrar("SELECT * FROM Productos")
    
def CrearNuevoUsuario(TipoUsuario):
    Nombre = input("Ingrese su nombre\n")
    Telefono = input("Ingrese su telefono\n")
    Direccion = input("Ingrese email\n")
    Id_producto = input("Ingrese los productos\n")
    sql = "INSERT INTO "+TipoUsuario+" (Nombre,Telefono,Direccion,ID_Productos_Proveedor) VALUES (%s,%s,%s,%s)"
    val  = [(Nombre,Telefono,Direccion, Id_producto )]
    BD.EjecutarSQL_VAL(sql,val)

def Mostrar(Tabla):
    BD.Mostrar("SELECT * FROM "+Tabla)

def BorrarUsuario(ID):
    BD.EjecutarSQL("DELETE FROM Clientes WHERE ID_Cliente="+ID)

def BorrarProductos(ID):
    BD.EjecutarSQL("DELETE FROM Productos WHERE ID_Producto="+ID)

def CrearProductos():
    descripcion = input("Ingrese los productos\n")
    stock = input("Ingrese su stock\n")
    precio = input("Ingrese precio\n")
    sql = "INSERT INTO Productos (Descripcion,Id_Stock,Precio) VALUES (%s,%s,%s)"
    val  = [(descripcion,stock,precio)]
    BD.EjecutarSQL_VAL(sql,val)

def ModificarProductos():
    Idpedir=input("Ingrese su Id\n")
    descripcion = input("Ingrese la nueva descripcion\n")
    stock = input("Ingrese el nuevo stock\n")
    precio = input("Ingrese el nuevo precio\n")
    sql = ("UPDATE Productos SET Descripcion=%s ,ID_Stock=%s,Precio=%s WHERE ID_Producto=%s")
    val  = [(descripcion,stock,precio,Idpedir)]
    BD.EjecutarSQL_VAL(sql,val)
