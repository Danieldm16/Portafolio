var pattern=/^[a-zA-Z]{4}(\d{6})(([a-zA-Z0-9]){3})?$/;
var pattern2=/^[a-zA-Z ]{3,30}?$/;
var pattern3=/^[0-9]{10}?$/;
var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

function valida_aspirante() {
    var js_rfc = document.getElementById("irfc").value.trim();
    var js_nom = document.getElementById("inombre").value.trim();
    var js_pat = document.getElementById("ipaterno").value.trim();
    var js_mat = document.getElementById("imaterno").value.trim();
    var js_emp = document.getElementById("iempresa").value.trim();
    var js_tel = document.getElementById("itelefono").value.trim();
    var js_ema = document.getElementById("iemail").value.trim();
    var js_cur = document.getElementById("scurso").value;

    if (js_rfc.length==0){
        alert("Error: RFC no puede ir vacio");
        return false;
    }
    else if (!pattern.test(js_rfc)){
        alert("Error: El rfc esta mal formado, lo correcto es un patrón como el siguiente: SASA980518RR2");
        return false;
    }
    else if (js_nom.length == 0){
        alert("Error: nombre no puede ir vacio");
        return false;
    }
    else if (!pattern2.test(js_nom)){
        alert("Error: El nomnbre no puede llevar numeros y minimo 3 caractéres.");
        return false;
    }
    else if (js_pat.length == 0){
        alert("Error: Apellido paterno no puede ir vacio");
        return false;
    }
    else if (!pattern2.test(js_pat)){
        alert("Error: El apellido paterno no puede llevar numeros y minimo 3 caractéres.");
        return false;
    }
    else if (js_mat.length == 0){
        alert("Cuidado: El apellido materno esta vacio, si usted no tiene apellido materno puede dejarlo asi, si tiene por favor introduzcalo.");
    }
    else if (js_emp.length < 3){
        alert("Error: Escriba el nombre de la empresa completo");
        return false;
    }
    else if (js_tel.length == 0){
        alert("Error: El telefono no puede ir vacio");
        return false;
    }
    else if (!pattern3.test(js_tel)){
        alert("Error: El telefono no cumple el formato requerido, por ejemplo: 8441916235");
        return false;
    }
    else if (js_ema.length == 0){
        alert("Error: El email no puede ir vacio");
        return false;
    }
    else if (!emailPattern.test(js_ema)){
        alert("Error: El email no cumple el formato requerido");
        return false;
    }
    else if (js_cur == ""){
        alert("Error: Debe seleccionar algún curso");
        return false;
    }
    
}