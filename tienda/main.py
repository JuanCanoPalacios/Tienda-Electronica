import os
import logica

def iniciarSesion():
    os.system('cls')
    if(logica.db.mydb is None or logica.db.mycursor is None):
            input()
            return
    usuario = input("Ingrese el nombre de usuario: ")
    contraseña = input("Ingrese la contraseña: ")
    
    if(usuario == "admin" and contraseña == "admin"):
        menuAdmin()
    else:
        print("Datos incorrectos.")

def menuAdmin():
    while(1):
        os.system('cls')
        opcion = input("1. Gestionar Clientes\n2. Gestionar Prooveedores\n3. Gestionar Productos\n4. Gestionar Productos por Proveedor\n5. Gestionar Compras\n6. Gestionar Ventas\n9. Salir\n")
        if(opcion=='1'):
            gestionarClientes()
            confirmar()
        if(opcion=='2'):
            gestionarProveedores()
            confirmar()
        if(opcion=='3'):
            gestionarProductos()
            confirmar()
        if(opcion=='4'):
            gestionarProductosProveedores()
            confirmar()
        if(opcion=='5'):
            pass
            gestionarCompras()
        if(opcion=='6'):
            gestionarVentas()
        elif(opcion=='9'):
            break
         
def gestionarClientes():
    while(1):
        opcion = input("\n1. Mostrar todos los clientes\n2. Nuevo Cliente\n3. Borrar Cliente\n4. Modificar Cliente\n9. Salir\t")
        if(opcion=='1'):
            logica.mostrar("Clientes")#Listo       
            confirmar()
        if(opcion=='2'):
            logica.crearCliente()#Listo
            confirmar()
        if(opcion=='3'):
            logica.borrarCliente(input("Ingrese el ID del Cliente que desea borrar: \t"))#Listo
            confirmar()
        if(opcion=='4'):
            logica.modificarCliente(input("Ingrese el ID del Cliente a modificar: \t"))#Listo
            confirmar()
        if(opcion=='9'):
            break
        
def gestionarProveedores():
    while(1):
        opcion = input("\n1. Mostrar todos los Proveedores\n2. Nuevo Proveedor\n3. Borrar Proveedor\n4. Modificar Proveedor\n9. Salir\t")
        if(opcion=='1'):
            logica.mostrar("Proveedor")
            confirmar()
        if(opcion=='2'):
            logica.crearProveedor()
            confirmar()
        if(opcion=='3'):
            logica.borrarProveedor(input("Ingrese el ID del Proveedor que desea borrar: \t"))
            confirmar()
        if(opcion=='4'): 
            logica.modificarProveedor(input("Ingrese el ID del Proveedor a modificar: \t"))
            confirmar()
        if(opcion=='9'):
            break
        
def gestionarProductos():
    while(1):
        opcion = input("\n1. Mostrar todos los productos\n2. Alta productos\n3. Baja productos\n4. Modificar productos\n9. Salir\t")
        if(opcion=='1'):
            logica.mostrar("Productos")
            confirmar()
        if(opcion=='2'):
            logica.crearProductos()
            confirmar()
        if(opcion=='3'):
            logica.borrarProductos(input("Ingrese el ID del Producto que desea borrar: \t"))
            confirmar()
        if(opcion=='4'):
            logica.modificarProductos(input("Ingrese el ID del Producto a modificar: \t"))
            confirmar()
        if(opcion=='9'):
            break

def gestionarProductosProveedores():
    while(1):
        opcion = input("\n1. Mostrar producto proveedor\n2. Alta producto proveedor\n3. Baja producto proveedor\n4. Modificar producto proveedor\n9. Salir\t")
        if(opcion=='1'):
            logica.mostrar("Productos_Proveedor")
            confirmar()
        if(opcion=='2'):
            logica.altaProductoProveedor()
            confirmar()
        if(opcion=='3'):
            logica.bajaProductoProveedor(input("Ingrese el ID del Producto a que desee dar de baja: \t"))
            confirmar()
        if(opcion=='4'):
            logica.modificarProductoProveedor(input("Ingrese el ID que desea modificar: \t"))
            confirmar()
        if(opcion=='9'):
            break

def gestionarVentas():
    while(1):
        opcion = input("\n1. Mostrar historial de ventas\n2. Realizar venta\n3. Eliminar venta\n4. Modificar venta\n9. Salir\t")
        if(opcion=='1'):
            logica.mostrar("Ventas")
            confirmar()
        if(opcion=='2'):
            logica.realizarVenta()
            confirmar()
        if(opcion=='3'):
            logica.borrarVenta(input("Ingrese el ID de la venta a que desee borar: \t"))
            confirmar()
        if(opcion=='4'):
            logica.modificarVenta(input("Ingrese el ID que desea modificar: \t"))
            confirmar()

def gestionarCompras():
    while(1):
        opcion = input("\n1. Mostrar historial de compras\n2. Realizar compra\n3. Eliminar compra\n4. Modificar compra\n9. Salir\t")
        if(opcion=='1'):
            logica.mostrar("Ventas")
            confirmar()
        if(opcion=='2'):
            logica.crearCompra()
            confirmar()
        if(opcion=='3'):
            logica.borrarCompra(input("Ingrese el ID de la compra a que desee borrar \t"))
            confirmar()
        if(opcion=='4'):
            logica.modificarCompra(input("Ingrese el ID que desea modificar: \t"))
            confirmar()

def confirmar():
    PEPE = input("\n\nPresione para 'Enter' continuar: \t")
    os.system('cls')
       
iniciarSesion()
