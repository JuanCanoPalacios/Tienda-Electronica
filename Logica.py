import BD

def MostrarTodosClientes():
    BD.Mostrar("SELECT * FROM Usuarios")
    
def CrearNuevoUsuario(TipoUsuario):
    Nombre = input("Ingrese su nombre\n")
    Telefono = input("Ingrese su telefono\n")
    Direccion = input("Ingrese email\n")
    sql = "INSERT INTO "+TipoUsuario+" (Nombre,Telefono,Direccion) VALUES (%s,%s,%s)"
    val  = [(Nombre,Telefono,Direccion)]
    BD.EjecutarSQL_VAL(sql,val)

def Mostrar(Tabla):
    BD.Mostrar("SELECT * FROM "+Tabla)

def BorrarUsuario(ID):
    BD.EjecutarSQL("DELETE FROM Clientes WHERE ID_Cliente="+ID)
