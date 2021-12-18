<!DOCTYPE html>
<html>
    <head>
        <title>Parcial 1 - Daniel Salazar</title>
	    <link rel="stylesheet" type="text/css" href="css/estilo.css">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <meta charset="utf-8">
    </head>
<body>
<div class="contenedor">

    <div class="contenedorarriba">
    <img src="descarga.jpeg" alt="Logo agencia de viajes">
    <h1>Reservacion de viajes</h1>
    </div>

    <div class="contenedor2">
        <form action="#" method="post" onsubmit="return valida_campos();">

        <p>Las reservaciones se respetan solo por 2 dias a partir de la fecha de registro</p>
        <hr/>

        <div class="row">
		<div class="labels">	
			<label>Nombre Completo: </label>
		</div>
		<div class="inputs">
			<input type="text" class="mayusculas" name="fnombre" id="fnombre" maxlength="30" size="40"  placeholder="Ingrese su Nombre" >
		</div>
	    </div>

        <div class="row">
		<div class="labels">	
			<label>Correo electronico: </label>
		</div>
		<div class="inputs">
			<input type="email" name="femail" id="femail"  placeholder="Ingrese su correo electronico" >
		</div>
	    </div>

        <div class="row">
		<div class="labels">	
			<label>Seleccione el paquete de viaje: </label>
		</div>
		<div class="inputs">
        <select name="fpaquete" id="fpaquete">
				<option value="0">Seleccione un paquete</option>
				<option value="1">Walt Disney</option>				
				<option value="2">San miguel de Allende</option>
				<option value="3">Rivera Maya</option>				
				<option value="4">Acapulco</option>
			</select>
		</div>
	    </div>

        <div class="row">
		<div class="labels">	
			<label>Fecha de llegada: </label>
		</div>
		<div class="inputs">
			<input type="date" name="ffecha" id="ffecha">
		</div>
	    </div>

        <div class="row">
		<div class="labels">	
			<label>Numero de personas: </label>
		</div>
		<div class="inputs">
        <select name="fnumpersonas" id="fnumpersonas">
				<option value="0">0</option>
				<option value="1">1</option>				
				<option value="2">2</option>
				<option value="3">3</option>				
				<option value="4">4</option>
                <option value="4">5</option>
			</select>
		</div>
	    </div>

        <div class="row">
		<div class="labels">	
			<label>¿Que beneficios le gustaria obtener? </label>
		</div>
		<div class="inputs">
            <input type="checkbox" id="beneficio1" name="beneficio1" value="Traslados">
            <label for="vehicle1"> Traslados </label><br>
            <input type="checkbox" id="beneficio2" name="beneficio2" value="Alimentacion">
            <label for="vehicle2"> Alimentacion </label><br>
            <input type="checkbox" id="beneficio3" name="beneficio3" value="Visita Lugares Turisiticos">
            <label for="vehicle3"> Visitar Lugares Turisticos </label>
            <input type="checkbox" id="beneficio4" name="beneficio4" value="Paseos Nocturnos">
            <label for="vehicle3"> Paseos Nocturnos </label>
		</div>
	    </div>

        <div class="row">
		<div class="labels">	
			<label>Si obtuvo cupón de descuento ingreselo: </label>
		</div>
		<div class="inputs">
			<input type="text" name="fcupon" id="fcupon" placeholder="Cupon de descuento">
		</div>
	    </div>

        <div class="row">
		    <div class="labels">	
			    <label> ¿Acepta terminos y condiciones? </label>
		    </div>
		        <div class="inputs" id="radiobuttons">
                    <input type="radio" id="facepto" name="fterminosycondiciones" value="HTML">
                    <label>Acepto</label><br>
                    <input type="radio" id="fnoacepto" name="fterminosycondiciones" value="CSS">
                <label>No acepto</label>
                </div>
		    </div>
	    </div>
        
        <div class="boton">
		    <input type="submit" name="btn_reservacion" value="Enviar Reservacion">
	    </div>

        </form>
    </div>

</div><!-- cierre del contenedor -->
<script src="js/funciones.js"></script>
</body>
</html>