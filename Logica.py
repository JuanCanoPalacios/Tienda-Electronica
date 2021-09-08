import BD
def MostrarTodosClientes():
    BD.Mostrar("SELECT * FROM Usuarios")
    
def CrearNuevoUsuario(TipoUsuario):
    Nombre = input("Ingrese su nombre\n")
    Telefono = input("Ingrese su apellido\n")
    Direccion = input("Ingrese email\n")
    sql = "INSERT INTO "+TipoUsuario+" (Nombre,Telefono,Direccion) VALUES (%s,%s,%s)"
    val  = [(Nombre,Telefono,Direccion)]
    BD.EjecutarSQL(sql,val)

def Mostrar(Tabla):
    BD.Mostrar("SELECT * FROM "+Tabla)