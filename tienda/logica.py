import db
import ui

def mostrar(Tabla):
    db.mostrar("SELECT * FROM "+Tabla)

#Cliente
def crearCliente():
    try:
        ui.banner()
        Nombre = str(input("[*] Ingrese su nombre: \t"))
        Telefono = int(input("[*] Ingrese su telefono: \t"))
        Direccion = str(input("[*] Ingrese email: \t"))
        sql = ("INSERT INTO Clientes (Nombre,Telefono,Direccion) VALUES (%s,%s,%s)")
        val = [(Nombre,str(Telefono),Direccion)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, compruebe que los datos esten bien colocados.")

def borrarCliente(ID):
    if db.dato("SELECT * FROM Clientes Where ID_Cliente="+ID)!=[]:
        db.ejecutarSQL("DELETE FROM Clientes WHERE ID_Cliente="+ID)
        print("El usuario fue borrado con exito.")
    else:
        print("El usuario no fue borrado porque no existe en la base de datos.")

def modificarCliente(ID_MOD):
    try:
        ui.banner()
        Nombre = str(input("[*] Ingrese su nombre: \t"))
        Telefono = int(input("[*] Ingrese su Telefono: \t"))
        Direccion = str(input("[*] Ingrese Direccion: \t"))
        sql = ("UPDATE Clientes SET Nombre=%s,Telefono=%s,Direccion=%s WHERE ID_Cliente=%s")
        val = [(Nombre,str(Telefono),Direccion,ID_MOD)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Uno de lo datos ingresados son incorrectos, porfavor reintente la operación.")

#Proveedor
def crearProveedor():
    try:
        ui.banner()
        Nombre = str(input("[*] Ingrese su nombre: \t"))
        Telefono = int(input("[*] Ingrese su telefono: \t"))
        Email = str(input("[*] Ingrese email: \t"))
        sql = "INSERT INTO Proveedor (Nombre,Telefono,Email) VALUES (%s,%s,%s)"
        val = [(Nombre,str(Telefono),Email)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Uno de lo datos ingresados son incorrectos, porfavor reintente la operación.")

def borrarProveedor(ID):#Complicado
    try:
        if db.dato("SELECT * FROM Proveedor Where ID_Proveedor="+ID)!=[]:
            db.ejecutarSQL("DELETE FROM Productos_Proveedor WHERE ID_Proveedor="+ID)
            db.ejecutarSQL("DELETE FROM Proveedor WHERE ID_Proveedor="+ID)
        else:
            print("El proveedor no fue borrado porque no existe en la base de datos.")
    except:
        print("Borrar todos los registros relacionados a dicho proveedor. Que tenga buen día. <3")
    
def modificarProveedor(ID_MOD):#Testeado
    try:
        ui.banner()
        Nombre = str(input("[*] Ingrese su nombre: \t"))
        Telefono = int(input("[*] Ingrese su telefono: \t"))
        Email = str(input("[*] Ingrese email: \t"))
        sql = ("UPDATE Proveedor SET Nombre=%s,Telefono=%s, Email=%s WHERE ID_Proveedor=%s")
        val = [(Nombre,str(Telefono),Email,ID_MOD)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo modificar el proveedor.")

#Productos
def crearProductos():
    try:
        ui.banner()
        descripcion = str(input("[*] Ingrese nombre del producto:\t"))
        precio = int(input("[*] Ingrese precio:\t"))
        cantidad = int(input("[*] Ingrese su stock actual:\t"))
        sql = "INSERT INTO Productos (Descripcion,Precio,Cantidad) VALUES (%s,%s,%s)"
        val = [(descripcion,str(precio),str(cantidad))]
        db.ejecutarSQL_VAL(sql,val)
    except: 
        print("Hay un dato mal ingresado, por lo cual no se pudo crear el producto.")

def borrarProductos(ID):
    if db.dato("SELECT * FROM Productos Where ID_Producto="+ID)!=[]:
        db.ejecutarSQL("DELETE FROM Productos WHERE ID_Producto="+ID)
    else:
        print("El producto no fue borrado porque no existe en la base de datos.")
    
def modificarProductos(ID_MOD):
    try:
        ui.banner()
        descripcion = str(input("[*] Ingrese la nueva descripcion: \t"))
        cantidad = int(input("[*] Ingrese la nueva Cantidad: \t"))
        precio = int(input("[*] Ingrese el nuevo precio: \t"))
        sql = ("UPDATE Productos SET Descripcion=%s,Precio=%s,Cantidad=%s WHERE ID_Producto=%s")
        val = [(descripcion,str(precio),str(cantidad),ID_MOD)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo modificar el producto.")

#ProductoProveedor
def altaProductoProveedor():#Testeado
    try:
        ui.banner()
        ID_Producto =  int(input("[*] Ingrese el ID del producto al cual hace referencia:\t"))
        ID_Proveedor = int(input("[*] Ingrese el ID del proveedor: \t"))
        Precio = int(input("[*] Ingrese el costo del producto:\t"))
        sql = "INSERT INTO Productos_Proveedor (ID_Producto,ID_Proveedor,Precio) VALUES (%s,%s,%s)"
        val = [(str(ID_Producto),str(ID_Proveedor),str(Precio))]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo crear el producto-proveedor.")

def bajaProductoProveedor(ID):#Testeado
    if db.dato("SELECT * FROM Productos_Proveedor Where ID_Productos_Proveedor="+ID)!=[]:
        db.ejecutarSQL("DELETE FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID)
    else:
        print("El producto-proveedor no fue borrado porque no existe en la base de datos.")

def modificarProductoProveedor(ID_MOD):
    try:   
        ui.banner()
        ID_Producto = int(input("[*] Ingrese el ID del producto al cual hace referencia:\t"))
        ID_Proveedor = int(input("[*] Ingrese el ID del proveedor: \t"))
        Precio = int(input("[*] Ingrese el costo del producto:\t"))
        sql = "UPDATE Productos_Proveedor SET ID_Producto=%s,ID_Proveedor=%s,Precio=%s WHERE ID_Productos_Proveedor=%s"
        val = [(str(ID_Producto),str(ID_Proveedor),str(Precio),ID_MOD)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo modificar el producto-proveedor.")

#Ventas
def realizarVenta():#Testeado
    try: 
        ui.banner()
        ID_Cliente = int(input("[*] Ingrese el ID del cliente: \t"))
        ID_Producto = int(input("[*] Ingrese el ID del producto: \t"))
        Cantidad = int(input("[*] Ingrese la cantidad deseada: \t"))
        cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+str(ID_Producto))[0][0])
        sql = ("INSERT INTO Ventas (ID_Cliente, ID_Producto, Cantidad) VALUES (%s,%s,%s)")
        val = [(str(ID_Cliente),str(ID_Producto),str(Cantidad))]
        db.ejecutarSQL_VAL(sql,val)
        sql = ("UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s")
        val = [(str(cantidad_actual-Cantidad), str(ID_Producto))]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo realizar la venta.")

def borrarVenta(ID):#A testear
    try:
        ID_Producto = (db.dato("SELECT ID_Producto FROM Ventas WHERE ID_Venta="+ID)[0][0])
        cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_Producto)[0][0])
        cantidad_venta = int(db.dato("SELECT Cantidad FROM Ventas WHERE ID_Venta="+ID)[0][0])
        sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
        val = [(str(cantidad_actual+cantidad_venta), ID_Producto)]
        db.ejecutarSQL_VAL(sql,val)
        db.ejecutarSQL("DELETE FROM Ventas WHERE ID_Venta="+ID)
    except:
        print("La venta no fue borrada porque no existe en la base de datos.")

def modificarVenta(ID_MOD):#A testear
    try:
        ui.banner()
        cantidad = int(input("[*] Ingrese la nueva cantidad: \t"))
        ID_Cliente = (db.dato("SELECT ID_Cliente FROM Ventas WHERE ID_Venta="+ID_MOD)[0][0])
        ID_Producto = (db.dato("SELECT ID_Producto FROM Ventas WHERE ID_Venta="+ID_MOD)[0][0])
        cantidad_venta = int(db.dato("SELECT Cantidad FROM Ventas WHERE ID_Venta="+ID_MOD)[0][0])
        cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_Producto)[0][0])
        sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
        val = [(str(cantidad_actual-cantidad_venta+cantidad), ID_Producto)]
        db.ejecutarSQL_VAL(sql,val)
        sql = "UPDATE Ventas SET ID_Cliente=%s, ID_Producto=%s, Cantidad=%s WHERE ID_Venta=%s"
        val = [(str(ID_Cliente),str(ID_Producto),str(cantidad),str(ID_MOD))]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo modificar la venta.")

#Compras
def crearCompra():#Testeado
    try:
        ui.banner()
        ID_Producto_Proveedor = int(input("[*] Ingrese el ID del Producto del Proveedor:\t"))
        Cantidad = int(input("[*] Ingrese la cantidad del producto a comprar:\t"))
        ID_Producto = (db.dato("SELECT ID_Producto FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID_Producto_Proveedor)[0][0])
        cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto = "+ID_Producto)[0][0])
        sql = "INSERT INTO Compras (ID_Producto_Proveedor, Cantidad) VALUES (%s,%s)"
        val = [(str(ID_Producto_Proveedor), str(Cantidad))]
        db.ejecutarSQL_VAL(sql,val)
        sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
        val = [(str(cantidad_actual+Cantidad),ID_Producto)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo crear la compra.")

def borrarCompra(ID):#Testeado
    try:
        cantidad = int(db.dato("SELECT Cantidad FROM Compras WHERE ID_Compra="+ID)[0][0])
        ID_Producto_Proveedor=str(db.dato("SELECT ID_Producto_Proveedor FROM Compras WHERE ID_Compra="+ID)[0][0])
        ID_Producto = str(db.dato("SELECT ID_Producto FROM Productos_Proveedor WHERE ID_Productos_Proveedor="+ID_Producto_Proveedor)[0][0])
        cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_Producto)[0][0])
        sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
        val = [(str(cantidad_actual-cantidad),ID_Producto)]
        db.ejecutarSQL_VAL(sql,val)
        db.ejecutarSQL("DELETE FROM Compras WHERE ID_Compra="+ID)
    except:
        print("La compra no fue borrada porque no existe en la base de datos.")

def modificarCompra(ID_MOD):#Testeado
    try:
        ui.banner()
        ID_ProductoProveedor = int(input("[*] Ingrese el ID del producto a modificar:\t"))
        Cantidad = int(input("[*] Ingrese la nueva cantidad de la compra:\t"))
        cantidad_actual = int(db.dato("SELECT Cantidad FROM Productos WHERE ID_Producto="+ID_ProductoProveedor)[0][0])
        cantidad_compra = int(db.dato("SELECT Cantidad FROM Compras WHERE ID_Compra="+ID_MOD)[0][0])
        sql = "UPDATE Productos SET Cantidad=%s WHERE ID_Producto=%s"
        val = [(str(cantidad_actual-cantidad_compra+Cantidad),ID_ProductoProveedor)]
        db.ejecutarSQL_VAL(sql,val)
        sql = "UPDATE Compras SET ID_Producto_Proveedor=%s, Cantidad=%s WHERE ID_Compra=%s"
        val = [(str(ID_ProductoProveedor),str(Cantidad),ID_MOD)]
        db.ejecutarSQL_VAL(sql,val)
    except:
        print("Hay un dato mal ingresado, por lo cual no se pudo modificar la compra.")
