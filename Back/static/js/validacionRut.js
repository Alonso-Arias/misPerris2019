jQuery(document).ready(function($){
	$('#rut').rut();
});

;(function($){
	$.fn.rut = function(opt){
		var defaults = $.extend({
			error_html: '<td class="rut-error">Rut Incorrecto</td>',
			formatear : true,
			on : 'blur',
			required : true,
			placeholder : true,
			fn_error : function(input){
				mostrar_error(input, defaults.error_html);
			},
			fn_validado: function(input){}
		}, opt);
		return this.each(function(){
			var $t = $(this);
			$t.wrap('<div class="rut-container"></div>');
			$t.attr('pattern', '[0-9]{1,2}.[0-9]{3}.[0-9]{3}-[0-9Kk]{1}').attr('maxlength', '12')/*Define el Máximo de Caracteres y Realiza la Operación*/;
			if(defaults.required) $t.attr('required', 'required');
			if(defaults.placeholder) $t.attr('placeholder', 'Ejemplo:12.345.678-5')/*Muestra un Mensaje de fondo con un Ejemplo del Formato*/;
			if(defaults.formatear){/*Función Para Formatear el Rut*/
				$t.on('blur', function(){
					$t.val($.rut.formatear($t.val()));
				});
			}
			$t.on(defaults.on, function(){
				$('.rut-error').remove();
				if($.rut.validar($t.val()) && $.trim($t.val()) != '')
				defaults.fn_validado();
				else
				defaults.fn_error($t);
			});
		});
	}
	function mostrar_error(input, error){
		input.closest('.rut-container').append(error);
	}
})(jQuery);
jQuery.rut = {
	
	/*Función que Realiza los Calculos Para Validar el Rut*/
	validar : function(rut){
		if (!/[0-9]{1,2}.[0-9]{3}.[0-9]{3}-[0-9Kk]{1}/.test(rut))
		return false;
		var tmp = rut.split('-');
		var dv = tmp[1], rut 	= tmp[0].split('.').join('');
		if(dv == 'K') dv = 'k';
		return ($.rut.dv(rut) == dv);
	},
	dv : function(rut){
		var M=0,S=1;
		for(;rut;rut=Math.floor(rut/10))
		S=(S+rut%10*(9-M++%6))%11;
		return S ? S-1 : 'k';
	},
	/*Función que Formatea el Rut*/
	formatear : function(rut){
		var tmp = this.quitar_formato(rut);
		var rut = tmp.substring(0, tmp.length - 1), f = "";
		while(rut.length > 3) {
			f = '.' + rut.substr(rut.length - 3) + f;
			rut = rut.substring(0, rut.length - 3);
		}
		return ($.trim(rut) == '') ? '' : rut + f + "-" + tmp.charAt(tmp.length-1);
	},
	quitar_formato : function(rut){
		rut = rut.split('-').join('').split('.').join('');
		return rut;
	}
};
