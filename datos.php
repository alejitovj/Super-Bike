<?php
include("conexion.php");

$nombre=$_POST["nombre"];
$email=$_POST["email"];
$usuario=$_POST["usuario"];
$password=$_POST["password"];

$sql="INSERT INTO usuarios(nombre,email,nombre_usuario,password)
VALUES('$nombre','$email','$usuario','$password')";

if($conexion->query($sql)===TRUE){
    echo "ok";
}else{
    echo "Error: ".$conexion->error;
}

$conexion->close();
?>