function validar()  {

    //declaración de variables
    var nombrecompleto = document.getElementById("f_nombrecompleto").value.trim();
    var curp = document.getElementById("f_curp").value.trim().toUpperCase();
    var nombre = document.getElementById("f_nombre").value.trim();
    var apellidopaterno = document.getElementById("f_paterno").value.trim();
    var apellidomaterno = document.getElementById("f_materno").value.trim();
    var telefono = document.getElementById("f_telefono").value.trim();
    var celular = document.getElementById("f_celular").value.trim();
    var correo = document.getElementById("f_correo").value.trim();
    var niveldeestudios = document.getElementById("f_nivel").value;
    var municipio = document.getElementById("f_municipio").value;
    var asunto = document.getElementById("f_asunto").value;

    //estas lineas son para ir cambiando el cuantos tickets van pero aun no se bien como hacerlo
    //var tickets = document.getElementById("alinearnumerocambiable").value;
    //document.getElementById("alinearnumerocambiable").innerHTML = tickets + 1;

    //aqui opte por hacer toda la condicional en una linea y no if anidados, los nombres se validan que no queden solos, los telefonos que los digitos sean 10 y el que sean numericos
    //esta establecido desde el html asi que no puede haber otro tipo de dato, y los ultimos tres del form se valida que no se quede en la opción por defecto.
    //asi solo continua si todo esta correcto.
    if (nombrecompleto.length != 0 && curpValida(curp) == true && nombre.length != 0 && apellidopaterno.length != 0 && apellidomaterno.length != 0 && telefono.length == 10 && celular.length == 10 && correo.length != 0 && niveldeestudios != "Seleccione el nivel" && municipio != "Seleccione el municipio" && asunto != "Seleccione el asunto a tratar") {
      return alert("El formato fue llenado de forma correcta");
      } else {
      return alert("Revise su información, puede haber dejado un campo vacio o haber llenado mal un campo");  
    }
}

//Función para validar una CURP, esta función no es de mi autoria, la encontre en: https://es.stackoverflow.com/questions/31039/cómo-validar-una-curp-de-méxico
function curpValida(curp) {
    var re = /^([A-Z][AEIOUX][A-Z]{2}\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\d])(\d)$/,
        validado = curp.match(re);
	
    if (!validado)  //Coincide con el formato general?
    	return false;
    
    //Validar que coincida el dígito verificador
    function digitoVerificador(curp17) {
        //Fuente https://consultas.curp.gob.mx/CurpSP/
        var diccionario  = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ",
            lngSuma      = 0.0,
            lngDigito    = 0.0;
        for(var i=0; i<17; i++)
            lngSuma = lngSuma + diccionario.indexOf(curp17.charAt(i)) * (18 - i);
        lngDigito = 10 - lngSuma % 10;
        if (lngDigito == 10) return 0;
        return lngDigito;
    }
  
    if (validado[2] != digitoVerificador(validado[1])) 
    	return false;
        
    return true; //Validado
}