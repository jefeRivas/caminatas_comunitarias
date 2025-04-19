
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

-- 5. Tabla de rutas disponibles
CREATE TABLE rutas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    distancia_km DECIMAL(5,2),
    dificultad ENUM('fácil', 'moderada', 'difícil'),
    descripcion TEXT,
    puntos_referencia TEXT,
    tiempo_estimado_min INT
);

-- 6. Tabla de horarios disponibles
CREATE TABLE horarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dia_semana ENUM('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'),
    hora_inicio TIME,
    hora_fin TIME,
    max_voluntarios INT
);

-- 7. Tabla de caminatas programadas
CREATE TABLE caminatas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    horario_id INT,
    ruta_id INT,
    estado ENUM('pendiente', 'en_progreso', 'completada', 'cancelada') DEFAULT 'pendiente',
    FOREIGN KEY (horario_id) REFERENCES horarios(id),
    FOREIGN KEY (ruta_id) REFERENCES rutas(id)
);

-- 8. Tabla de registro de caminatas (relación muchos a muchos entre usuarios y caminatas)
CREATE TABLE registro_caminatas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    caminata_id INT,
    perro_id INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    asistencia BOOLEAN DEFAULT FALSE,
    comentarios TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (caminata_id) REFERENCES caminatas(id),
    FOREIGN KEY (perro_id) REFERENCES perros(id)
);

-- 9. Tabla de preferencias de perros por usuario
CREATE TABLE preferencias_perros (
    usuario_id INT,
    perro_id INT,
    preferencia INT, -- 1 a 5, siendo 5 la mayor preferencia
    PRIMARY KEY (usuario_id, perro_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (perro_id) REFERENCES perros(id)
);

-- 10. Tabla de preferencias de rutas por usuario
CREATE TABLE preferencias_rutas (
    usuario_id INT,
    ruta_id INT,
    preferencia INT, -- 1 a 5, siendo 5 la mayor preferencia
    PRIMARY KEY (usuario_id, ruta_id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (ruta_id) REFERENCES rutas(id)
);

-- 11. Tabla de historial de caminatas
CREATE TABLE historial_caminatas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_caminata_id INT,
    duracion_real_min INT,
    distancia_real_km DECIMAL(5,2),
    comportamiento_perro ENUM('excelente', 'bueno', 'regular', 'malo'),
    observaciones TEXT,
    FOREIGN KEY (registro_caminata_id) REFERENCES registro_caminatas(id)
);

-- 12. Tabla de requisitos para pasear perros
CREATE TABLE requisitos_perros (
    perro_id INT,
    requisito VARCHAR(255),
    PRIMARY KEY (perro_id, requisito),
    FOREIGN KEY (perro_id) REFERENCES perros(id)
);

-- 13. Tabla de equipamiento para caminatas
CREATE TABLE equipamiento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    cantidad_disponible INT
);

-- 14. Tabla de préstamo de equipamiento
CREATE TABLE prestamo_equipamiento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    registro_caminata_id INT,
    equipamiento_id INT,
    cantidad INT,
    devuelto BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (registro_caminata_id) REFERENCES registro_caminatas(id),
    FOREIGN KEY (equipamiento_id) REFERENCES equipamiento(id)
);