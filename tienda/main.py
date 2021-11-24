import os
import logica
import ui

ui.banner()

def iniciarSesion():

    if(logica.db.mydb is None or logica.db.mycursor is None):
            input()
            return
    usuario = input("[*] Ingrese el nombre de usuario: ")
    contraseña = input("[*] Ingrese la contraseña:\t")
    
    if(usuario == "admin" and contraseña == "admin"):
        menuAdmin()
    else:
        print("Datos incorrectos.")

def menuAdmin():
    while(1):
        ui.banner()
        opcion = input('''
 _______________________________________
| [1] Gestionar Clientes                |
| [2] Gestionar Prooveedores            |
| [3] Gestionar Productos               |   
| [4] Gestionar Productos por Proveedor |
| [5] Gestionar Compras                 |
| [6] Gestionar Ventas                  |
| [9] Salir                             |
|_______________________________________|
  [*] Tu Opcion: ''')
        if(opcion=='1'):
            gestionarClientes()
        if(opcion=='2'):
            gestionarProveedores()
        if(opcion=='3'):
            gestionarProductos()
        if(opcion=='4'):
            gestionarProductosProveedores()
        if(opcion=='5'):
            gestionarCompras()
        if(opcion=='6'):
            gestionarVentas()
        elif(opcion=='9'):
            break
        confirmar()
         
def gestionarClientes():
    while(1):
        ui.banner()
        opcion = input('''
 ________________________________
| [1] Mostrar todos los clientes |
| [2] Nuevo Cliente              |
| [3] Borrar Cliente             |
| [4] Modificar Cliente          |
| [9] Salir                      |
|________________________________|
  [*] = ''')
        if(opcion=='1'):
            logica.mostrar("Clientes")#Listo       
        if(opcion=='2'):
            logica.crearCliente()#Listo
        if(opcion=='3'):
            logica.borrarCliente(input("[*] Ingrese el ID del Cliente que desea borrar: \t"))#Listo
        if(opcion=='4'):
            logica.modificarCliente(input("[*] Ingrese el ID del Cliente a modificar: \t"))#Listo
        if(opcion=='9'):
            break
        confirmar()
        
def gestionarProveedores():
    while(1):
        ui.banner()
        opcion = input('''
 __________________________________
| [1] Mostrar todos los Proveedores|
| [2] Nuevo Proveedor              |
| [3] Borrar Proveedor             |
| [4] Modificar Proveedor          |
| [9] Salir                        |
|__________________________________|
  [*] = ''')
        if(opcion=='1'):
            logica.mostrar("Proveedor")
        if(opcion=='2'):
            logica.crearProveedor()
        if(opcion=='3'):
            logica.borrarProveedor(input("[*] Ingrese el ID del Proveedor que desea borrar: \t"))
        if(opcion=='4'): 
            logica.modificarProveedor(input("[*] Ingrese el ID del Proveedor a modificar: \t"))
        if(opcion=='9'):
            break
        confirmar()
        
def gestionarProductos():
    while(1):
        ui.banner()
        opcion = input('''
 _________________________________
| [1] Mostrar todos los productos |
| [2] Alta productos              |
| [3] Baja productos              |
| [4] Modificar productos         |
| [9] Salir                       |
|_________________________________|
  [*] = ''')
        if(opcion=='1'):
            logica.mostrar("Productos")
        if(opcion=='2'):
            logica.crearProductos()
        if(opcion=='3'):
            logica.borrarProductos(input("[*] Ingrese el ID del Producto que desea borrar: \t"))
        if(opcion=='4'):
            logica.modificarProductos(input("[*] Ingrese el ID del Producto a modificar: \t"))
        if(opcion=='9'):
            break
        confirmar()

def gestionarProductosProveedores():
    while(1):
        ui.banner()
        opcion = input('''
 __________________________________
| [1] Mostrar producto proveedor   |
| [2] Alta producto proveedor      |
| [3] Baja producto proveedor      |
| [4] Modificar producto proveedor |
| [9] Salir                        |
|__________________________________|
  [*] = ''')
        if(opcion=='1'):
            logica.mostrar("Productos_Proveedor")
        if(opcion=='2'):
            logica.altaProductoProveedor()
        if(opcion=='3'):
            logica.bajaProductoProveedor(input("[*] Ingrese el ID del Producto a que desee dar de baja: \t"))
        if(opcion=='4'):
            logica.modificarProductoProveedor(input("[*] Ingrese el ID que desea modificar: \t"))
        if(opcion=='9'):
            break
        confirmar()

def gestionarVentas():
    while(1 ):
        ui.banner()
        opcion = input('''    
 ________________________________
| [1] Mostrar historial de ventas |
| [2] Realizar venta              |
| [3] Eliminar venta              |
| [4] Modificar venta             |
| [9] Salir                       |
|_________________________________|
  [*] = ''')
        if(opcion=='1'):
            logica.mostrar("Ventas")
        if(opcion=='2'):
            logica.realizarVenta()
        if(opcion=='3'):
            logica.borrarVenta(input("[*] Ingrese el ID de la venta a que desee borrar: \t"))
        if(opcion=='4'):
            logica.modificarVenta(input("[*] Ingrese el ID que desea modificar: \t"))
        if(opcion=='9'):
            break
        confirmar()

def gestionarCompras():
    while(1):
        ui.banner()
        opcion = input('''
 _________________________________
| [1] Mostrar historial de compras |
| [2] Realizar compra              |
| [3] Eliminar compra              |
| [4] Modificar compra             |
| [9] Salir                        |
|__________________________________|
  [*] = ''')
        if(opcion=='1'):
            logica.mostrar("Compras")
        if(opcion=='2'):
            logica.crearCompra()
        if(opcion=='3'):
            ID=input("[*] Ingrese el ID de la compra a que desee borrar:\t")
            logica.borrarCompra(ID)
        if(opcion=='4'):
            ID=input("[*] Ingrese el ID que desea modificar:\t")
            logica.modificarCompra(ID)
        if(opcion=='9'):
            break
        confirmar()

def confirmar():
    PEPE = input("\n\nPresione para 'Enter' continuar: \t")
    os.system('clear')
       
iniciarSesion()
