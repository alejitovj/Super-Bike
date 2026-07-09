<?php
// Primero traemos la conexión que ya creamos en el otro archivo
include("conexion.php");

// Aquí recibimos los datos del formulario (de registro.html)
$nombre = $_POST['nombre'];
$email = $_POST['email'];

// Aquí guardamos los datos
$sql = "INSERT INTO usuarios (nombre, email) VALUES ('$nombre', '$email')";

if ($conexion->query($sql) === TRUE) {
    echo "¡Registro exitoso!";
} else {
    echo "Error: " . $sql . "<br>" . $conexion->error;
}
?>