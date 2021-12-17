<!DOCTYPE html>
<html>
<head>
	<title>Registro de Aspirantes</title>
	<link rel="stylesheet" type="text/css" href="css/estilos.css">
</head>
<body>

<div class="container">

<h2>Ingrese sus datos para el pre-registro a los cursos</h2>
<p>Completar los datos requeridos, esta pantalla esta adaptada para operar en dispositivos móviles</p>


	<form action="inserta_aspirante.php" method="post" onsubmit="return valida_aspirante();">
	<div class="row">
		<div class="col-25" style="white-space:nowrap">
			<label for="lrfc">R.F.C</label>
			<label id="estatus"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="irfc" id="irfc" maxlength="13" size="20"  placeholder="Ingrese su RFC">
		</div>
		</div>
	


	<div class="row">	
		<div class="col-25">	
			<label for="lnom">Nombre</label>
			<label id="estatus_nom"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="inombre" id="inombre" maxlength="30" size="40"  placeholder="Ingrese su Nombre" >
		</div>
	</div>

	<div class="row">
		<div class="col-25">	
			<label for="lpat">Paterno</label>
			<label id="estatus_pat"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="ipaterno" id="ipaterno" maxlength="30" size="40"  placeholder="Ingrese su Apellido Paterno" >
		</div>
	</div>


	<div class="row">
		<div class="col-25">
			<label for="lmat">Materno</label>
			<label id="estatus_mat"></label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="imaterno" id="imaterno" maxlength="30" size="40"  placeholder="Ingrese su Apellido Materno" >
		</div>
	</div>	

	<div class="row">
		<div class="col-25">	
			<label for="lemp">Empresa</label>
		</div>
		<div class="col-75">
			<input type="text" class="mayusculas" name="iempresa" id="iempresa" maxlength="30" size="40" placeholder="Ingrese nombre de la empresa" >
		</div>
	</div>

	<div class="row">
		<div class="col-25">
			<label for="ltel">Teléfono</label>
		</div>
		<div class="col-75">
			<input type="tel" pattern="[0-9]{10}" name="itelefono" id="itelefono" maxlength="10" size="15"  placeholder="Ingrese su el telefono a 10 dígitos" >
		</div>
	</div>

	<div class="row">
		<div class="col-25">
			<label for="lmail">Email</label>
		</div>
		<div class="col-75">
			<input type="email" name="iemail" id="iemail" maxlength="60" size="80"  placeholder="Ingrese su corro electrónico" >
		</div>
	</div>

	<div class="row">

		<div class="col-25">
			<label for="lcur">Cursos disponibles</label>
		</div>
		<div class="col-75">
			<select name="scurso" id="scurso">
				<option value="">Seleccione</option>
				<option value="1">EL SMOG Y SUS EFECTOS</option>				
				<option value="2">PLANTAS MEDICINALES</option>
				<option value="3">DESARROLLO URBANO SUSTENTABLE</option>				
				<option value="4">CIUDADANIA Y COMUNIDAD ECOLOGÍA</option>
			</select>
		</div>
	</div>

	<div class="row2">
	<div class="boton">
		<input type="submit" name="btn_registro" value="Registrar">
	</div>
	</div>
	</form>	

</div><!-- cierre container -->
<script src="js/funciones.js"></script>
</body>
</html>