<!DOCTYPE html>
<html>
    <head>
        <title>
            Tarea 4 parcial 1 DanielSalazar Matricula:17289193
        </title>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="css/estilo.css">
        <script src="js/funcion.js"></script>
    </head>
    <body>

    <div id="contenedorprincipal">

    <form action="recoge_datos.php" method="POST" accept-charset="utf-8" id="form" onsubmit="return validar">
        <fieldset>
        
        <div id="titulo">
            <img src="sde.png" alt="Logo secretaria de educación" id="alinearimagen"/>
            <h1 id="textotitulo">Ticket de Turno</h1>
            <h1 id="alinearnumerocambiable">1</h1>
        </div>

        <br>

        <div id="nombrecompletoycurp" >

        <label>Nombre completo de quien realizara el trámite:</label>
        <input type="text" name="f_nombrecompleto" id="f_nombrecompleto" placeholder="Ingrese su nombre completo" required="true">

        <label id="labels">CURP:</label>
        <input type="text" name="f_curp" id="f_curp" placeholder="Ingrese su CURP" required="true">

        </div>

        <br>

        <div id="nombrepaternomaterno" >

        <label>Nombre:</label>
        <input type="text" name="f_nombre" id="f_nombre" placeholder="Ingrese su nombre" required="true">

        <label id="labels">Paterno:</label>
        <input type="text" name="f_paterno" id="f_paterno" placeholder="Ingrese su apellido paterno" required="true">

        <label id="labels">Materno:</label>
        <input type="text" name="f_materno" id="f_materno" placeholder="Ingrese su apellido materno" required="true">

        </div>

        <br>

        <div id="telefonocelularcorreo" >

        <label>Telefono:</label>
        <input type="number" name="f_telefono" id="f_telefono" placeholder="Ingrese su telefono de casa" required="true">

        <label id="labels">Celular:</label>
        <input type="number" name="f_celular" id="f_celular" placeholder="Ingrese su celular" required="true">

        <label id="labels">Correo:</label>
        <input type="email" name="f_correo" id="f_correo" placeholder="Ingrese su correo eletronico" required="true">

        </div>

        <br>

        <div id="niveldeestudios">

        <label>Nivel al que desea ingresar o que ya cursa el alumno:</label>
        <select name="f_nivel" id="f_nivel" required="true" >
            <option >Seleccione el nivel</option>
            <option > Primero </option>
            <option > Segundo </option>
            <option > Tercero </option>
            <option > Cuarto </option>
            <option > Quinto </option>
            <option > Sexto </option>
            <option > Septimo </option>
            <option > Octavo </option>
            <option > Noveno </option>
            <option > Otro </option>
        </select>

        </div>

        <br>

        <div id="municipio" >

        <label>Municipio donde desea estudiar el alumno:</label>
        <select name="f_municipio" id="f_municipio" required="true" >
            <option>Seleccione el municipio</option>
            <option> Saltillo </option>
            <option> San pedro de las colonias </option>
            <option> Piedras Negras </option>
            <option> Ciudad Acuña </option>
            <option> Nueva Rosita </option>
            <option> Allende </option>
            <option> Parras de la fuente </option>
        </select>

        </div>

        <br>

        <div id="asunto">

        <label>Seleccione el asunto que va a tratar:</label>
        <select name="f_asunto" id="f_asunto" required="true" >
            <option>Seleccione el asunto a tratar</option>
            <option> Baja </option>
            <option> Baja temporal </option>
            <option> Inscripcion </option>
            <option> Credito de inscripción </option>
        </select>

        </div>

        <br>

        <div id="f_submit">

        <input type="submit" name="f_generarturno" value="Generar Turno" onclick="validar()">

        </div>

        <br>

        <div id="qrcodeandbarcode">

        <img src="barcode.gif" alt="Mecanismo de autenticación 1"/>

        <img src="https://www.codigos-qr.com/qr/php/qr_img.php?d=Este ticket de turno es original de la secretaria de educación publica. &s=4&e=" alt="Mecanismo de autenticación 2"/>


        </div>

        </fieldset>
    </form>

    </div><!--Cierre de contenedor principal-->

    </body>
</html>