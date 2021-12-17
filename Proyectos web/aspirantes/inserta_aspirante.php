<?php
/*if (isset($_POST["irfc"])){
    $rfc=strtoupper($_POST["irfc"]);
}
else{
    $rfc=null;
    echo "no se introdujo un rfc";
}*/

$rfc = isset($_POST["irfc"]) ? $rfc=strtoupper($_POST["irfc"]) : $rfc=null;
$nom = isset($_POST["inombre"]) ? $nom=strtoupper($_POST["inombre"]) : $nom=null;
$pat = isset($_POST["ipaterno"]) ? $pat=strtoupper($_POST["ipaterno"]) : $pat=null;
$mat = isset($_POST["imaterno"]) ? $mat=strtoupper($_POST["imaterno"]) : $mat=null;
$emp = isset($_POST["iempresa"]) ? $emp=strtoupper($_POST["iempresa"]) : $emp=null;
$tel = isset($_POST["itelefono"]) ? $tel=strtoupper($_POST["itelefono"]) : $tel=null;
$ema = isset($_POST["iemail"]) ? $rfc=$_POST["iemail"] : $ema=null;
$cur = isset($_POST["scurso"]) ? $rfc=$_POST["scurso"] : $cur=null;

echo $rfc.'-'.$nom.'-'.$pat.'-'.$mat.'-'.$emp.'-'.$tel.'-'.$ema.'-'.$cur;
?>