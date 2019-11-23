/*Función Para Dejar la Inicial de Cada Palabra en el Nombre en Mayúscula (initcap)*/
$('#nombre').keyup(function(){
	/*Expresión Regular Para Dejar La Primera Letra en Mayúscula Cada vez que Hay un Espacio, No funciona al Poner el Teclado en Mayúscula ya que no Hay un lowercase Para los Demás Caracteres*/	
    $(this).val($(this).val().replace(/(^|\s)\S/g, l => l.toUpperCase()));
});


