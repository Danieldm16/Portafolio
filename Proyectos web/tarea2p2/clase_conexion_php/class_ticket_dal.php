<?php
if (class_exists('DataAccessLayer')!=true){
    class DataAccessLayer{

        //La variable "$conn" es el resultado de mysqli_connect("localhost","root","","db_ticket");
        //viene siendo la variable db_conn en ticket_db.php

        public function insertar($conn, $id, $nombrecompleto, $curp, $nombre, $apellidopaterno, $apellidomaterno, $telefono, $celular, $correo, $niveldeestudios, $municipio, $asunto){
            $query = mysqli_query($conn, "INSERT INTO datos_solicitud (solicitud_id, solicitud_nombrecompleto, solicitud_curp, solicitud_nombre, solicitud_apellidopaterno, solicitud_apellidomaterno, solicitud_telefono, solicitud_celular, solicitud_correo, solicitud_niveldeestudios, solicitud_municipio, solicitud_asunto) VALUES ('$id', '$nombrecompleto', '$curp', '$nombre', '$apellidopaterno', '$apellidomaterno', '$telefono', '$celular', '$correo', '$niveldeestudios', '$municipio', '$asunto')");
            return $query;
            //En las operaciones como insert, update o delete regresa un true o false, por si se hizo
            //o no se hizo la operación. en operaicones como "select"
            //regresa un objeto mysqli_result
        }

        public function actualizar($conn, $id, $nombrecompleto, $curp, $nombre, $apellidopaterno, $apellidomaterno, $telefono, $celular, $correo, $niveldeestudios, $municipio, $asunto){
            $query=mysqli_query($conn, "UPDATE  datos_solicitud SET solicitud_nombrecompleto='$nombrecompleto', solicitud_curp='$curp', solicitud_nombre='$nombre', solicitud_apellidopaterno='$apellidopaterno', solicitud_apellidomaterno='$apellidomaterno', solicitud_telefono='$telefono', solicitud_celular='$celular', solicitud_correo='$correo', solicitud_niveldeestudios='$niveldeestudios', solicitud_municipio='$municipio', solicitud_asunto='$asunto' WHERE solicitud_id='$id'");
            return $query;
        }

        public function leer($conn, $curp){//el read lo hice conforme al curp ya también se pedia una lectura por id, asi pues quedan las dos.
            $query = mysqli_query($conn,"SELECT * FROM datos_solicitud WHERE solicitud_curp=$curp");
            return $query;
        }

        public function borrar($conn, $id){
            $query=mysqli_query($conn,"DELETE FROM datos_solicitud WHERE solicitud_id=$id");
            return $query;
        }

        public function existe($conn, $id){
            $sql="SELECT * FROM datos_solicitud WHERE solicitud_id=$id";

            $result=mysqli_query($conn,$sql);
            
            $numresult=mysqli_num_rows($result);
            
            if ($numresult > 0){
                return true;
            } else {
                return false;
            }
            //lo primero que hace es que hace una consulta
            //después con la función mysqli_num_rows() nos dice cuantas filas hay que tengan ese id
            //si el numero de filas es mayor a cero quiere decir que si existe y regresa un true
            //si el numero de filas no es mayor a cero quiere decir que no existe y regresa un false
        }

        public function obtenerporid($conn, $id){
            $query = mysqli_query($conn,"SELECT * FROM datos_solicitud WHERE solicitud_id=$id");
            return $query;
        }

        public function listartodoslosregistros($conn){
            $query=mysqli_query($conn,"SELECT * FROM datos_solicitud");
            return $query;
        }
    }
}
?>