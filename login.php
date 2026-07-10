<?php
session_start();
include("conexion.php");

$email=$_POST["email"];
$password=$_POST["password"];

$sql="SELECT * FROM usuarios WHERE email='$email' AND password='$password'";
$resultado=$conexion->query($sql);

if($resultado->num_rows>0){
    $usuario=$resultado->fetch_assoc();

    $_SESSION["id"]=$usuario["id"];
    $_SESSION["nombre"]=$usuario["nombre"];

    echo "ok";
}else{
    echo "error";
}

$conexion->close();
?>