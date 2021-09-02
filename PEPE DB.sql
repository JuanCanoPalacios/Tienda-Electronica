DROP DATABASE IF EXISTS Tienda_Electronica;
CREATE DATABASE Tienda_Electronica;

USE Tienda_Electronica;

CREATE TABLE Clientes
(
	ID_Cliente INT NOT NULL AUTO_INCREMENT,
    Nombre VARCHAR(45) NOT NULL,
    Telefono INT NOT NULL,
    Direccion VARCHAR(45) NOT NULL,
    PRIMARY KEY (ID_Cliente)
);
CREATE TABLE Productos
(
	ID_Producto INT NOT NULL AUTO_INCREMENT,
    ID_Stock INT NOT NULL,
    Precio INT NOT NULL, 
    Descripcion VARCHAR(100),
    PRIMARY KEY (ID_Producto)
);
CREATE TABLE Stock
(
	ID_Stock INT NOT NULL AUTO_INCREMENT,
    ID_Producto INT NOT NULL,
    Cantidad INT NOT NULL,
    PRIMARY KEY (ID_Stock),
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto)
);
CREATE TABLE Productos_Proveedor
(
	ID_Productos_Proveedor INT NOT NULL AUTO_INCREMENT,
    ID_Producto INT NOT NULL,
    PRIMARY KEY (ID_Productos_Proveedor),
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto)
);
CREATE TABLE Productos_Reservados
(
	ID_Producto_Reservado INT NOT NULL AUTO_INCREMENT,
    ID_Producto INT NOT NULL,
    PRIMARY KEY (ID_Producto_Reservado),
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto)
    
);
CREATE TABLE Proveedor
(
	ID_Proveedor INT NOT NULL AUTO_INCREMENT,
    ID_Productos_Proveedor INT NOT NULL,
    Nombre VARCHAR(45) NOT NULL,
    Telefono INT NOT NULL,
    PRIMARY KEY  (ID_Proveedor),
    FOREIGN KEY (ID_Productos_Proveedor) REFERENCES Productos_Proveedor(ID_Productos_Proveedor)
);
CREATE TABLE Compras
(
	ID_Venta INT NOT NULL AUTO_INCREMENT,
    ID_Proveedor INT NOT NULL,
    Fecha DATETIME,
    PRIMARY KEY (ID_Venta),
    FOREIGN KEY (ID_Proveedor) REFERENCES Proveedor(ID_Proveedor)  
);
CREATE TABLE Ventas
(
	ID_Venta INT NOT NULL AUTO_INCREMENT,
    ID_Cliente INT NOT NULL,
    Fecha DATETIME,
    PRIMARY KEY (ID_Venta),
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)  
);
SELECT * FROM Clientes;
INSERT INTO Clientes(Nombre,Telefono,Direccion) VALUES ('PEPE','11557709','Urquiza 559')





