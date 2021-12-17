<!DOCTYPE html>
<html>
    <head>
        <title>
            Tarea 3 parcial 1 DanielSalazar Matricula:17289193
        </title>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="css/estilo.css">
    </head>
    <body>

    <div id="contenedorprincipal">

    <form action="#" method="get" accept-charset="utf-8">
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
        <input type="text" name="f_telefono" id="f_telefono" placeholder="Ingrese su telefono de casa">

        <label id="labels">Celular:</label>
        <input type="text" name="f_celular" id="f_celular" placeholder="Ingrese su celular" required="true">

        <label id="labels">Correo:</label>
        <input type="text" name="f_correo" id="f_correo" placeholder="Ingrese su correo eletronico" required="true">

        </div>

        <br>

        <div id="niveldeestudios">

        <label>Nivel al que desea ingresar o que ya cursa el alumno:</label>
        <select name="f_nivel" id="f_nivel" required="true" >
            <option value="0"> Seleccione el nivel </option>
            <option value="01"> Primero </option>
            <option value="02"> Segundo </option>
            <option value="03"> Tercero </option>
            <option value="04"> Cuarto </option>
            <option value="05"> Quinto </option>
            <option value="06"> Sexto </option>
            <option value="07"> Septimo </option>
            <option value="08"> Octavo </option>
            <option value="09"> Noveno </option>
            <option value="10"> Otro </option>
        </select>

        </div>

        <br>

        <div id="municipio" >

        <label>Municipio donde desea estudiar el alumno:</label>
        <select name="f_municipio" id="f_municipio" required="true" >
            <option value="0"> Seleccione el municipio </option>
            <option value="01"> Saltillo </option>
            <option value="02"> San pedro de las colonias </option>
            <option value="03"> Piedras Negras </option>
            <option value="04"> Ciudad Acuña </option>
            <option value="05"> Nueva Rosita </option>
            <option value="06"> Allende </option>
            <option value="07"> Parras de la fuente </option>
        </select>

        </div>

        <br>

        <div id="asunto">

        <label>Seleccione el asunto que va a tratar:</label>
        <select name="f_asunto" id="f_asunto" required="true" >
            <option value="0"> Seleccione el asunto a tratar </option>
            <option value="01"> Baja </option>
            <option value="02"> Baja temporal </option>
            <option value="03"> Inscripcion </option>
            <option value="04"> Credito de inscripción </option>
        </select>

        </div>

        <br>

        <div id="f_submit">

        <input type="submit" name="f_generarturno" value="Generar Turno">

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