CREATE DATABASE IF NOT EXISTS Python_test;
USE Python_test;

CREATE TABLE IF NOT EXISTS productos (
    id_producto INT PRIMARY KEY,
    nombre_producto VARCHAR(100),
    categoria VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS ventas (
    id_venta INT PRIMARY KEY AUTO_INCREMENT,
    id_producto INT,
    continente VARCHAR(50),
    pais VARCHAR(50),
    cliente VARCHAR(100),
    unidades INT,
    importe DECIMAL(10,2),
    año INT,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
