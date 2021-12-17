<?php
if (class_exists('datos_solicitud')!=true){
    class datos_solicitud{
        protected $solicitud_id;
        protected $solicitud_nombrecompleto;
        protected $solicitud_curp;
        protected $solicitud_nombre;
        protected $solicitud_apellidopaterno;
        protected $solicitud_apellidomaterno;
        protected $solicitud_telefono;
        protected $solicitud_celular;
        protected $solicitud_correo;
        protected $solicitud_niveldeestudios;
        protected $solicitud_municipio;
        protected $solicitud_asunto;

        public function __construct(
            $solicitud_id=NULL,
            $solicitud_nombrecompleto=NULL,
            $solicitud_curp=NULL,
            $solicitud_nombre=NULL,
            $solicitud_apellidopaterno=NULL,
            $solicitud_apellidomaterno=NULL,
            $solicitud_telefono=NULL,
            $solicitud_celular=NULL,
            $solicitud_correo=NULL,
            $solicitud_niveldeestudios=NULL,
            $solicitud_municipio=NULL,
            $solicitud_asunto=NULL        
           ){
                   $this->solicitud_id=$solicitud_id;
                   $this->solicitud_nombrecompleto=$solicitud_nombrecompleto;
                   $this->solicitud_curp=$solicitud_curp;
                   $this->solicitud_nombre=$solicitud_nombre;
                   $this->solicitud_apellidopaterno=$solicitud_apellidopaterno;
                   $this->solicitud_apellidomaterno=$solicitud_apellidomaterno;
                   $this->solicitud_telefono=$solicitud_telefono;
                   $this->solicitud_celular=$solicitud_celular;
                   $this->solicitud_correo=$solicitud_correo;
                   $this->solicitud_niveldeestudios=$solicitud_niveldeestudios;
                   $this->solicitud_municipio=$solicitud_municipio;
                   $this->solicitud_asunto=$solicitud_asunto;                           
           }//END CONSTRUCTOR
        
        public function getsolicitud_id()
        {
            return $this->solicitud_id;
        }
        public function setsolicitud_id($solicitud_id)
        {
            $this->solicitud_id = $solicitud_id;

            return $this;
        }

        public function getsolicitud_nombrecompleto()
        {
            return $this->solicitud_nombrecompleto;
        }
        public function setsolicitud_nombrecompleto($solicitud_nombrecompleto)
        {
            $this->solicitud_nombrecompleto = $solicitud_nombrecompleto;

            return $this;
        }

        public function getsolicitud_curp()
        {
            return $this->solicitud_curp;
        }
        public function setsolicitud_curp($solicitud_curp)
        {
            $this->solicitud_curp = $solicitud_curp;

            return $this;
        }

        public function getsolicitud_nombre()
        {
            return $this->solicitud_nombre;
        }
        public function setsolicitud_nombre($solicitud_nombre)
        {
            $this->solicitud_nombre = $solicitud_nombre;

            return $this;
        }
        
        public function getsolicitud_apellidopaterno()
        {
            return $this->solicitud_apellidopaterno;
        }
        public function setsolicitud_apellidopaterno($solicitud_apellidopaterno)
        {
            $this->solicitud_apellidopaterno = $solicitud_apellidopaterno;

            return $this;
        }

        public function getsolicitud_apellidomaterno()
        {
            return $this->solicitud_apellidomaterno;
        }
        public function setsolicitud_apellidomaterno($solicitud_apellidomaterno)
        {
            $this->solicitud_apellidomaterno = $solicitud_apellidomaterno;

            return $this;
        }

        public function getsolicitud_telefono()
        {
            return $this->solicitud_telefono;
        }
        public function setsolicitud_telefono($solicitud_telefono)
        {
            $this->solicitud_telefono = $solicitud_telefono;

            return $this;
        }

        public function getsolicitud_celular()
        {
            return $this->solicitud_celular;
        }
        public function setsolicitud_celular($solicitud_celular)
        {
            $this->solicitud_celular = $solicitud_celular;

            return $this;
        }

        public function getsolicitud_correo()
        {
            return $this->solicitud_correo;
        }
        public function setsolicitud_correo($solicitud_correo)
        {
            $this->solicitud_correo = $solicitud_correo;

            return $this;
        }

        public function getsolicitud_niveldeestudios()
        {
            return $this->solicitud_niveldeestudios;
        }
        public function setsolicitud_niveldeestudios($solicitud_niveldeestudios)
        {
            $this->solicitud_niveldeestudios = $solicitud_niveldeestudios;

            return $this;
        }

        public function getsolicitud_municipio()
        {
            return $this->solicitud_municipio;
        }
        public function setsolicitud_municipio($solicitud_municipio)
        {
            $this->solicitud_municipio = $solicitud_municipio;

            return $this;
        }

        public function getsolicitud_asunto()
        {
            return $this->solicitud_asunto;
        }
        public function setsolicitud_asunto($solicitud_asunto)
        {
            $this->solicitud_asunto = $solicitud_asunto;

            return $this;
        }

    }
}
?>
