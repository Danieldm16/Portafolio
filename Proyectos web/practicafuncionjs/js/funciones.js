function validar()  {
    var entrada = document.getElementById("finput").value.trim;
    
    if (entrada == "") {
        return alert("La entrada no debe estar vacia");
      } else {
      return alert("La entrada que introdujiste es: " + entrada);
    }
}