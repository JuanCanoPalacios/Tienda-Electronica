import os
import Logica
def MenuAdmin():
    while(1):
        os.system('cls')
        Opcion = input("1.Gestionar Clientes\n2.Gestionar Prooveedores\n3.Gestionar Productos\n9.Salir\n")
        if(Opcion=='1'):
            GestionarClientes()
        if(Opcion=='2'):
            GestionarClientes()
        elif(Opcion=='3'):
            GestionarProductos()
        elif(Opcion=='9'):
            break
        else:
            print("Valor ingresado incorrecto\n")  

def GestionarClientes():
    while(1):
        Opcion = input("1.Mostrar todos los clientes\n2.Nuevo Cliente\n3.Borrar Cliente\n4.Modificar Cliente\n9.Salir\n")
        if(Opcion=='1'):
            Logica.Mostrar("Clientes")
        if(Opcion=='2'):
            Logica.CrearNuevoUsuario("Clientes")
        if(Opcion=='3'):
            ID_Borrar = input("Ingrese el id del Cliente que desea borrar\n")
            Logica.BorrarCliente(ID_Borrar)
        if(Opcion=='4'):
            ID_Modificar = input("Ingrese el id del Cliente a modificar\n")
            Logica.ModificarCliente(ID_Modificar)
        if(Opcion=='9'):
            break
        else:
            print("Valor ingresado incorrecto\n")

def GestionarProveedores():
    while(1):
        Opcion = input("1.Mostrar todos los Proveedores\n2.Nuevo Proveedor\n3.Borrar Proveedor\n4.Modificar Proveedor\n9.Salir\n")
        if(Opcion=='1'):
            Logica.Mostrar("Proveedor")
        if(Opcion=='2'):
            Logica.CrearNuevoUsuario("Proveedor")
        if(Opcion=='3'):
            ID_Borrar = input("Ingrese el id del Proveedor que desea borrar\n")
            Logica.BorrarProovedor(ID_Borrar)
        if(Opcion=='4'):
            ID_Modificar = input("Ingrese el id del Proovedor a modificar\n")
            Logica.ModificarProovedor(ID_Modificar)
        if(Opcion=='9'):
            break
        else:
            print("Valor ingresado incorrecto\n")

def GestionarProductos():
    while(1):
        Opcion = input("1.Mostrar todos los libros\n2.Alta libro\n3.Baja Libro\n4.Modificar libro\n9.Salir\n")
        if(Opcion=='1'):
            Logica.MostrarUsuarios()
        if(Opcion=='2'):
            pass
        if(Opcion=='3'):
            ID_Borrar = ("Ingrese el id del usuario que desea borrar\n")
            Logica.BorrarUsuario(ID_Borrar)
        if(Opcion=='4'):
            pass
        if(Opcion=='9'):
            break
        else:
            print("Valor ingresado incorrecto\n")
MenuAdmin()