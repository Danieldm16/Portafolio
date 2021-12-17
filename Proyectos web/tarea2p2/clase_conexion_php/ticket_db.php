<?php

error_reporting(E_ERROR  /*|E_WARNING*/|  E_PARSE);

if(class_exists("ticket_db")!=true){
    class ticket_db{
        protected $db_conn;
        protected $db_name;
        protected $db_query;

        function __construct(){
            $this->set_db("localhost","root","","db_ticket");
        }

        function __destruct(){
            $this->close_db();
        }

        function set_db($host,$user,$password,$db){
            if(!isset($this->db_conn)){
                $this->db_conn=mysqli_connect($host,$user,$password,$db);

                if(!$this->db_conn){
                    echo "Error: No se pudo conectar a MYSQL".'<br>';
                    echo "Número de error :".mysqli_connect_errno().'<br>';
                    echo "Error de depuración: ".mysqli_connect_error();
                    exit;
                }
                $this->db_name=$db;
            }
        }

        function close_db(){
            if (isset($db_conn)){
                mysqli_close($db_conn);
            }
        }

        function set_sql($sql){
            $this->db_query=$sql;
        }

    }//fin class
}//fin de if class exists

?>