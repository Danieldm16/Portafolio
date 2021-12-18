var patternnombre=/^[a-zA-Z ]{3,30}?$/;
var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

function valida_campos(){
    var nombre = document.getElementById("fnombre").value.trim();
    var correo = document.getElementById("femail").value.trim();
    var paqueteviaje = document.getElementById("fpaquete").value;
    var fecha = document.getElementById("ffecha").value;
    var numpersonas = document.getElementById("fnumpersonas").value;
    var beneficio1 = document.getElementById("beneficio1").checked;
    var beneficio2 = document.getElementById("beneficio2").checked;
    var beneficio3 = document.getElementById("beneficio3").checked;
    var beneficio4 = document.getElementById("beneficio4").checked;
    

    if (nombre.length==0){
        alert("Error: Nombre no puede ir vacio");
        return false;
    }
    else if (!patternnombre.test(nombre)){
        alert("Error: El nombre debe llevar al menos 3 letras y maximo 30");
        return false;
    }
    else if (correo.length == 0){
        alert("Error: El email no puede ir vacio");
        return false;
    }
    else if (!emailPattern.test(correo)){
        alert("Error: El email no cumple el formato requerido");
        return false;
    }
    else if (paqueteviaje == 0){
        alert("Error: Debe seleccionar algun paquete");
        return false;
    }
    else if (fecha == ""){
        alert("Error: Debe seleccionar alguna fecha");
        return false;
    }
    else if (numpersonas == 0){
        alert("Error: Debe seleccionar algun numero de personas");
        return false;
    }
    else if (beneficio1 == false && beneficio2 == false && beneficio3 == false && beneficio4 == false){
        alert("Error: Debe seleccionar algun beneficio");
        return false;
    }


}