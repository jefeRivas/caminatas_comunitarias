-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS caminatas_comunitarias;
USE caminatas_comunitarias;

-- 1. Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    contraseña VARCHAR(255),
    rol ENUM('voluntario', 'admin') DEFAULT 'voluntario',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Tabla de perfiles de voluntarios
CREATE TABLE perfiles_voluntarios (
    id INT PRIMARY KEY,
    telefono VARCHAR(20),
    direccion TEXT,
    experiencia TEXT,
    FOREIGN KEY (id) REFERENCES usuarios(id)
);

-- 3. Tabla de refugios
CREATE TABLE refugios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    direccion TEXT,
    telefono VARCHAR(20),
    correo VARCHAR(100)
);

-- 4. Tabla de perros
CREATE TABLE perros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    edad INT,
    raza VARCHAR(100),
    tamaño ENUM('pequeño', 'mediano', 'grande'),
    energia ENUM('baja', 'media', 'alta'),
    descripcion TEXT,
    estado ENUM('disponible', 'adoptado', 'en paseo') DEFAULT 'disponible',
    refugio_id INT,
    FOREIGN KEY (refugio_id) REFERENCES refugios(id)
);