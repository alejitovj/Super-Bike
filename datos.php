<?php
include("conexion.php");

$nombre = $_POST['nombre'];
$email = $_POST['email'];
$usuario = $_POST['usuario'];
$password = $_POST['password'];

$sql = "INSERT INTO usuarios (nombre, email, nombre_usuario, password) 
        VALUES ('$nombre', '$email', '$usuario', '$password')";

if ($conexion->query($sql) === TRUE) {
    // Redirigimos a una página de éxito (crearemos este archivo abajo)
    header("Location: exito.html");
    exit(); 
} else {
    echo "Error en el registro: " . $conexion->error;
}
?>