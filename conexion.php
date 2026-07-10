<?php
$server="localhost";
$user="root";
$pass="";
$db="usuarios";

$conexion=new mysqli($server,$user,$pass,$db);

if($conexion->connect_errno){
    die("Conexión fallida: ".$conexion->connect_error);
}
?>