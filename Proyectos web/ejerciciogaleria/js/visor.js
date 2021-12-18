window.onload= function(){
    visor1 = document.getElementById("visor");//referencia al visor
    mititulo = document.getElementById("titulo");//referencia al pie de foto
}

function miimagen(num) {//cambio de imagenes
    f = "imagenes/"+num+".jpeg";//rutaimagen
    document.images["imagenVisor"].src=f;//cambia imagen
    t = document.images["imagen"+num].alt;//texto de el pie de foto
    mititulo.innerHTML=t;//cambia pie de foto
}