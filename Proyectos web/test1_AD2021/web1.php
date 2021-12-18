<!DOCTYPE html>
<html>
    <head>
        <title>
            Formulario para registro de vacunación.
        </title>
    </head>
    <body>

    <form action="#" method="get" accept-charset="utf-8">
    <h1> Formulario para registro de vacunación. </h1>

    <h4> Instrucciones: Llena todos los campos con tus datos. </h4>

    <div id="curp">
        <label>CURP:</label>
        <input type="text" name="f_curp" id="f_curp" placeholder="Ingrese su CURP" required="true">
    </div>

    <br>

    <div id="nombre">
        <label>Nombre:</label>
        <input type="text" name="f_nombre" id="f_nombre" placeholder="Ingrese su nombre" required="true">
    </div>

    <div id="paterno">
        <label>Apellido paterno:</label>
        <input type="text" name="f_paterno" id="f_paterno" placeholder="Ingrese su apellido paterno" required="true">
    </div>

    <div id="materno">
        <label>Apellido materno:</label>
        <input type="text" name="f_materno" id="f_materno" placeholder="Ingrese su apellido materno">
    </div>

    <br>

    <div id="fecha_nac">
        <label>Fecha de nacimiento:</label>
        <input type="date" name="f_fecha_nac" id="f_fecha_nac" placeholder="Ingrese su fecha de nacimiento" required="true">
    </div>

    <br>

    <div id="estado">
        <label>Estado donde reside:</label>
        <select name="f_estado" id="f_estado" required="true">
            <option value="0"> Seleccione su estado </option>
            <option value="01"> Aguascalientes </option>
            <option value="02"> Colima </option>
            <option value="03"> Coahuila </option>
        </select>
    </div>

    <br>

    <div id="municipio">
        <label>Municipio donde reside:</label>
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
    </div>

    <div id="f_submit">
        <input type="submit" name="f_grabar" value="Guardar datos">
    </div>

    </form>

    </body>
</html>