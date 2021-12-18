<!DOCTYPE html>
<html>
    <head>
        <title>
            Formulario para registro de vacunación.
        </title>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="css/mystyle.css">
    </head>
    <body>
        <div id="contenedor"><!-- contenedor -->
            <header>
            <h1> Formulario para registro de vacunación. </h1>
            </header>

            <div id="forma"><!-- forma-->

    <form action="#" method="post">

        <p>CURP:</p>
        <input type="text" name="f_curp" id="f_curp" placeholder="Ingrese su CURP" required="true">

        <p>Nombre:</p>
        <input type="text" name="f_nombre" id="f_nombre" placeholder="Ingrese su nombre" required="true">

        <p>Apellido paterno:</p>
        <input type="text" name="f_paterno" id="f_paterno" placeholder="Ingrese su apellido paterno" required="true">

        <p>Apellido materno:</p>
        <input type="text" name="f_materno" id="f_materno" placeholder="Ingrese su apellido materno">

        <p>Fecha de nacimiento:</p>
        <input type="date" name="f_fecha_nac" id="f_fecha_nac" placeholder="Ingrese su fecha de nacimiento" required="true">

        <p>Estado donde reside:</p>
        <select name="f_estado" id="f_estado" required="true">
            <option value="0"> Seleccione su estado </option>
            <option value="01"> Aguascalientes </option>
            <option value="02"> Colima </option>
            <option value="03"> Coahuila </option>
        </select>

        <p>Municipio donde reside:</p>
        <select name="f_municipio" id="f_municipio" required="true">
            <option value="0"> Seleccione su municipio </option>

            <option value="01-001"> Aguascalientes </option>
            <option value="01-002"> Higueras </option>
            <option value="01-003"> San Juan </option>

            <option value="02-001"> Escobedo </option>
            <option value="02-002"> Zapopan </option>
            <option value="02-003"> San Pedro </option>

            <option value="03-001"> Saltillo </option>
            <option value="03-002"> Torreon </option>
            <option value="03-003"> Acuña </option>
        </select>

        <p>Correo electronico:</p>
        <input type="email" name="f_correo" id="f_correo" placeholder="Ingrese su correo electronico" required="true">

        <p>Observaciones Médicas:</p>
        <textarea name="f_obs" id="f_obs" placeholder="Ingrese observaciones" cols="40"></textarea>

        <br/>

        <div class="botonSubmit" style="border: 2px;">
        <input type="submit" name="f_grabar" value="Guardar datos">
        </div>

    </form>
    </div><!-- aqui termina el form.-->
    </div><!-- aqui termina el contenedor.-->
    </body>
</html>