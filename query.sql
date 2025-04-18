
-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS caminatas_comunitarias;
USE caminatas_comunitarias;

-- 1. Tabla de usuarios
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100) UNIQUE,
    contrasena VARCHAR(255),
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

-- 5. Tabla de caminatas
CREATE TABLE caminatas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME,
    duracion INT,
    ubicacion VARCHAR(255),
    descripcion TEXT
);

-- 6. Tabla de perros_caminatas
CREATE TABLE perros_caminatas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    caminata_id INT,
    perro_id INT,
    FOREIGN KEY (caminata_id) REFERENCES caminatas(id),
    FOREIGN KEY (perro_id) REFERENCES perros(id)
);

-- 7. Tabla de voluntarios_caminatas
CREATE TABLE voluntarios_caminatas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    caminata_id INT,
    usuario_id INT,
    FOREIGN KEY (caminata_id) REFERENCES caminatas(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- 8. Tabla de adopciones
CREATE TABLE adopciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    perro_id INT,
    fecha_adopcion DATETIME,
    estado ENUM('pendiente', 'aceptada', 'rechazada') DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (perro_id) REFERENCES perros(id)
);

-- 9. Tabla de reportes_perros
CREATE TABLE reportes_perros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    perro_id INT,
    descripcion TEXT,
    fecha DATETIME,
    FOREIGN KEY (perro_id) REFERENCES perros(id)
);

-- 10. Tabla de vacunas
CREATE TABLE vacunas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT
);

-- 11. Tabla de vacunas_perros
CREATE TABLE vacunas_perros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    perro_id INT,
    vacuna_id INT,
    fecha_aplicacion DATE,
    FOREIGN KEY (perro_id) REFERENCES perros(id),
    FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);

-- 12. Tabla de donaciones
CREATE TABLE donaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    monto DECIMAL(10,2),
    fecha DATETIME,
    metodo_pago VARCHAR(50),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- 13. Tabla de mensajes_contacto
CREATE TABLE mensajes_contacto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    asunto VARCHAR(100),
    mensaje TEXT,
    fecha DATETIME,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- 14. Tabla de eventos
CREATE TABLE eventos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    descripcion TEXT,
    fecha DATETIME,
    lugar VARCHAR(255)
);
