DELIMITER //

CREATE PROCEDURE obtener_caminatas_completas()
BEGIN
    SELECT c.id, c.fecha, c.estado, 
           u.nombre AS usuario_nombre, 
           p.nombre AS perro_nombre, 
           h.dia_semana, 
           r.nombre AS ruta_nombre
    FROM caminatas c
    JOIN registro_caminatas rc ON rc.caminata_id = c.id
    JOIN usuarios u ON u.id = rc.usuario_id
    JOIN perros p ON p.id = rc.perro_id
    JOIN horarios h ON h.id = c.horario_id
    JOIN rutas r ON r.id = c.ruta_id;
END //

DELIMITER ;

DELIMITER //

-- Obtener todos los usuarios
CREATE PROCEDURE obtener_usuarios()
BEGIN
    SELECT id, nombre, correo, contrasena, rol, fecha_registro
    FROM usuarios;
END //

-- Insertar un nuevo usuario
CREATE PROCEDURE insertar_usuario(
    IN p_nombre VARCHAR(100),
    IN p_correo VARCHAR(100),
    IN p_contrasena VARCHAR(100),
    IN p_rol VARCHAR(50),
    IN p_fecha_registro DATETIME
)
BEGIN
    INSERT INTO usuarios (nombre, correo, contrasena, rol, fecha_registro)
    VALUES (p_nombre, p_correo, p_contrasena, p_rol, p_fecha_registro);
END //

-- Actualizar un usuario
CREATE PROCEDURE actualizar_usuario(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_correo VARCHAR(100),
    IN p_contrasena VARCHAR(100),
    IN p_rol VARCHAR(50)
)
BEGIN
    UPDATE usuarios
    SET nombre = p_nombre,
        correo = p_correo,
        contrasena = p_contrasena,
        rol = p_rol
    WHERE id = p_id;
END //

-- Eliminar un usuario
CREATE PROCEDURE eliminar_usuario(
    IN p_id INT
)
BEGIN
    DELETE FROM usuarios
    WHERE id = p_id;
END //

DELIMITER ;
DELIMITER //

-- Procedimiento para obtener todos los perros con información de refugio
CREATE PROCEDURE ObtenerPerrosCompletos()
BEGIN
    SELECT 
        p.id,
        p.nombre,
        p.edad,
        p.raza,
        p.tamanio,
        p.energia,
        p.descripcion,
        p.estado,
        p.refugio_id,
        r.nombre AS refugio_nombre
    FROM 
        Perros p
    LEFT JOIN 
        Refugios r ON p.refugio_id = r.id;
END //

-- Procedimiento para obtener un perro por su ID
CREATE PROCEDURE ObtenerPerroPorID(IN PerroID INT)
BEGIN
    SELECT 
        p.id,
        p.nombre,
        p.edad,
        p.raza,
        p.tamanio,
        p.energia,
        p.descripcion,
        p.estado,
        p.refugio_id,
        r.nombre AS refugio_nombre
    FROM 
        Perros p
    LEFT JOIN 
        Refugios r ON p.refugio_id = r.id
    WHERE 
        p.id = PerroID;
END //

-- Procedimiento para crear un nuevo perro
CREATE PROCEDURE CrearPerro(
    IN p_nombre VARCHAR(100),
    IN p_edad INT,
    IN p_raza VARCHAR(50),
    IN p_tamanio VARCHAR(20),
    IN p_energia VARCHAR(20),
    IN p_descripcion TEXT,
    IN p_estado VARCHAR(20),
    IN p_refugio_id INT,
    OUT p_nuevo_id INT
)
BEGIN
    INSERT INTO Perros (
        nombre,
        edad,
        raza,
        tamanio,
        energia,
        descripcion,
        estado,
        refugio_id
    )
    VALUES (
        p_nombre,
        p_edad,
        p_raza,
        p_tamanio,
        p_energia,
        p_descripcion,
        p_estado,
        p_refugio_id
    );
    
    SET p_nuevo_id = LAST_INSERT_ID();
END //

-- Procedimiento para actualizar un perro existente
CREATE PROCEDURE ActualizarPerro(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_edad INT,
    IN p_raza VARCHAR(50),
    IN p_tamanio VARCHAR(20),
    IN p_energia VARCHAR(20),
    IN p_descripcion TEXT,
    IN p_estado VARCHAR(20),
    IN p_refugio_id INT
)
BEGIN
    UPDATE Perros
    SET 
        nombre = p_nombre,
        edad = p_edad,
        raza = p_raza,
        tamanio = p_tamanio,
        energia = p_energia,
        descripcion = p_descripcion,
        estado = p_estado,
        refugio_id = p_refugio_id
    WHERE 
        id = p_id;
END //

-- Procedimiento para eliminar un perro
CREATE PROCEDURE EliminarPerro(IN p_id INT)
BEGIN
    DELETE FROM Perros WHERE id = p_id;
END //

-- Procedimiento para obtener perros por refugio
CREATE PROCEDURE ObtenerPerrosPorRefugio(IN p_refugio_id INT)
BEGIN
    SELECT 
        p.id,
        p.nombre,
        p.edad,
        p.raza,
        p.tamanio,
        p.energia,
        p.descripcion,
        p.estado,
        p.refugio_id,
        r.nombre AS refugio_nombre
    FROM 
        Perros p
    LEFT JOIN 
        Refugios r ON p.refugio_id = r.id
    WHERE 
        p.refugio_id = p_refugio_id;
END //

DELIMITER ;

DELIMITER //

-- Procedimiento para obtener todos los refugios
CREATE PROCEDURE ObtenerRefugios()
BEGIN
    SELECT 
        id,
        nombre,
        direccion,
        telefono,
        correo
    FROM 
        Refugios;
END //

-- Procedimiento para obtener un refugio por ID
CREATE PROCEDURE ObtenerRefugioPorID(IN p_id INT)
BEGIN
    SELECT 
        id,
        nombre,
        direccion,
        telefono,
        correo
    FROM 
        Refugios
    WHERE 
        id = p_id;
END //

-- Procedimiento para crear un nuevo refugio
CREATE PROCEDURE CrearRefugio(
    IN p_nombre VARCHAR(100),
    IN p_direccion VARCHAR(200),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100),
    OUT p_nuevo_id INT
)
BEGIN
    INSERT INTO Refugios (
        nombre,
        direccion,
        telefono,
        correo
    )
    VALUES (
        p_nombre,
        p_direccion,
        p_telefono,
        p_correo
    );
    
    SET p_nuevo_id = LAST_INSERT_ID();
END //

-- Procedimiento para actualizar un refugio
CREATE PROCEDURE ActualizarRefugio(
    IN p_id INT,
    IN p_nombre VARCHAR(100),
    IN p_direccion VARCHAR(200),
    IN p_telefono VARCHAR(20),
    IN p_correo VARCHAR(100)
)
BEGIN
    UPDATE Refugios
    SET 
        nombre = p_nombre,
        direccion = p_direccion,
        telefono = p_telefono,
        correo = p_correo
    WHERE 
        id = p_id;
END //

-- Procedimiento para eliminar un refugio
CREATE PROCEDURE EliminarRefugio(IN p_id INT)
BEGIN
    DELETE FROM Refugios WHERE id = p_id;
END //

DELIMITER ;