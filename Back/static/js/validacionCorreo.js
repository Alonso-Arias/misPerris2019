/*Función Para Verificar que el Usuario Ingrese un Correo Electronico Correcto*/
$('#correoElectronico').on('blur', function () {
   if (/^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/.test(this.value)){}
   else {
   var defaults = $.extend({
			error_html: '<span class="rut-error">Rut Incorrecto</span>',
			fn_error : function(input){
				mostrar_error(input, defaults.error_html);
  }
});