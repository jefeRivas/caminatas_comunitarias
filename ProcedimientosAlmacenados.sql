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
