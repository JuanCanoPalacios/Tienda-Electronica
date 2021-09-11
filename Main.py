import os
import Logica

def MenuAdmin():
    while(1):
        if(Logica.BD.mydb is None):
            break
        os.system('cls')
        Opcion = input("1.Gestionar Clientes\n2.Gestionar Prooveedores\n3.Gestionar Productos\n4.Gestionar Productos por Proveedor\n5.Gestionar Compras\n6.Gestionar Ventas\n9.Salir\n")
        if(Opcion=='1'):
            GestionarClientes()
            Confirmar()
        if(Opcion=='2'):
            GestionarProveedores()
            Confirmar()
        if(Opcion=='3'):
            GestionarProductos()
            Confirmar()
        if(Opcion=='4'):
            GestionarProductosProveedores()
            Confirmar()
        if(Opcion=='5'):
            pass
            #GestionarCompras()
        if(Opcion=='6'):
            GestionarVentas()
        elif(Opcion=='9'):
            break
         
def GestionarClientes():
    while(1):
        Opcion = input("1.Mostrar todos los clientes\n2.Nuevo Cliente\n3.Borrar Cliente\n4.Modificar Cliente\n9.Salir\t")
        if(Opcion=='1'):
            Logica.Mostrar("Clientes")#Listo       
            Confirmar()
        if(Opcion=='2'):
            Logica.CrearCliente()#Listo
            Confirmar()
        if(Opcion=='3'):
            Logica.BorrarCliente(input("Ingrese el ID del Cliente que desea borrar: \t"))#Listo
            Confirmar()
        if(Opcion=='4'):
            Logica.ModificarCliente(input("Ingrese el ID del Cliente a modificar: \t"))#Listo
            Confirmar()
        if(Opcion=='9'):
            break
        
def GestionarProveedores():
    while(1):
        Opcion = input("1.Mostrar todos los Proveedores\n2.Nuevo Proveedor\n3.Borrar Proveedor\n4.Modificar Proveedor\n9.Salir\t")
        if(Opcion=='1'):
            Logica.Mostrar("Proveedor")
            Confirmar()
        if(Opcion=='2'):
            Logica.CrearProveedor()
            Confirmar()
        if(Opcion=='3'):
            Logica.BorrarProveedor(input("Ingrese el ID del Proveedor que desea borrar: \t"))
            Confirmar()
        if(Opcion=='4'): 
            Logica.ModificarProveedor(input("Ingrese el ID del Proveedor a modificar: \t"))
            Confirmar()
        if(Opcion=='9'):
            break
        
def GestionarProductos():
    while(1):
        Opcion = input("1.Mostrar todos los productos\n2.Alta productos\n3.Baja productos\n4.Modificar productos\n5.Alta producto proveedor\n6.Baja producto proveedor\n7.Modificar producto proveedor\n8.Mostrar producto proveedor\n9.Salir\t")
        if(Opcion=='1'):
            Logica.Mostrar("Productos")
            Confirmar()
        if(Opcion=='2'):
            Logica.CrearProductos()
            Confirmar()
        if(Opcion=='3'):
            Logica.BorrarProductos(input("Ingrese el ID del Producto que desea borrar: \t"))
            Confirmar()
        if(Opcion=='4'):
            Logica.ModificarProductos(input("Ingrese el ID del Producto a modificar: \t"))
            Confirmar()
        if(Opcion=='9'):
            break
def GestionarProductosProveedores():
    while(1):
        Opcion = input("1.Mostrar producto proveedor\n2.Alta producto proveedor\n3.Baja producto proveedor\n4.Modificar producto proveedor\n9.Salir\t")
        if(Opcion=='1'):
            Logica.Mostrar("Productos_Proveedor")
            Confirmar()
        if(Opcion=='2'):
            Logica.AltaProductoProveedor()
            Confirmar()
        if(Opcion=='3'):
            Logica.BajaProductoProveedor(input("Ingrese el ID del Producto a que desee dar de baja: \t"))
            Confirmar()
        if(Opcion=='4'):
            Logica.ModificarProductoProveedor(input("Ingrese el ID que desea modificar: \t"))
            Confirmar()
        if(Opcion=='9'):
            break

def GestionarVentas():
    while(1):
        Opcion = input("1.Mostrar historial de ventas\n2.Realizar venta\n3.Eliminar venta\n4.Modificar venta\n9.Salir\t")
        if(Opcion=='1'):
            Logica.Mostrar("Ventas")
            Confirmar()
        if(Opcion=='2'):
            Logica.RealizarVenta()
            Confirmar()
        if(Opcion=='3'):
            Logica.BorrarVenta(input("Ingrese el ID de la venta a que desee dar de baja: \t"))
            Confirmar()
        if(Opcion=='4'):
            Logica.ModificarVenta(input("Ingrese el ID que desea modificar: \t"))
            Confirmar()


def Confirmar():
    PEPE= input("\n\nPresione para 'Enter' continuar: \t")
    os.system('cls')
       
MenuAdmin()
