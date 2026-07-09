<?php
// 1. Conectamos a la base de datos
include("conexion.php");

// 2. Capturamos los datos del formulario (deben coincidir con el 'name' en HTML)
$nombre = $_POST['nombre'];
$email = $_POST['email'];
$usuario = $_POST['usuario'];
$password = $_POST['password'];

// 3. Insertamos los datos en el orden correcto
$sql = "INSERT INTO usuarios (nombre, email, nombre_usuario, password) 
        VALUES ('$nombre', '$email', '$usuario', '$password')";

// 4. Verificamos si funcionó
if ($conexion->query($sql) === TRUE) {
    echo "¡Registro exitoso! Tus datos ya están en la base de datos.";
} else {
    echo "Error: " . $sql . "<br>" . $conexion->error;
}
?>