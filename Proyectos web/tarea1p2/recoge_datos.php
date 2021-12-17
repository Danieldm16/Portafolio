<?php
//tomar los valores
$v_nombrecompleto=$_POST["f_nombrecompleto"];
$v_curp=$_POST["f_curp"];
$v_nombre=$_POST["f_nombre"];
$v_apellidopaterno=$_POST["f_paterno"];
$v_apellidomaterno=$_POST["f_materno"];
$v_telefono=$_POST["f_telefono"];
$v_celular=$_POST["f_celular"];
$v_correo=$_POST["f_correo"];
$v_niveldeestudios=$_POST["f_nivel"];
$v_municipio=$_POST["f_municipio"];
$v_asunto=$_POST["f_asunto"];

//comprobar que se tomaron correctamente
echo "Información del estudiante <br>";
echo "Nombre completo del estudiante: " . $v_nombrecompleto . "<br>";
echo "CURP: " . $v_curp . "<br>";
echo "Nombre o nombres: " . $v_nombre . "<br>";
echo "Apellido paterno: " . $v_apellidopaterno . "<br>";
echo "Apellido materno: " . $v_apellidomaterno . "<br>";
echo "Télefono de casa u oficina: " . $v_telefono . "<br>";
echo "Celular personal: " . $v_celular . "<br>";
echo "Correo electronico: " . $v_correo . "<br>";
echo "Nivel de estudios: " . $v_niveldeestudios . "<br>";
echo "Municipio donde reside: " . $v_municipio . "<br>";
echo "Asunto que va a tratar: " . $v_asunto . "<br>";
?>