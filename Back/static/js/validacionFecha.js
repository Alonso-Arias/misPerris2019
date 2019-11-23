/*Función Para que el Usuario deba ingresar una fecha de Nacimiento Menor al Año 2001*/
$('#fechaNac').keyup(function() {
    var fecha = new Date($('#fechaNac').val());
    if (fecha.getFullYear() < 2001) {
        fecha.setCustomValidity("");}
    else{
        fecha.setCustomValidity("La fecha de nacimiento debe ser anterior al año 2001");
    }
return;
});