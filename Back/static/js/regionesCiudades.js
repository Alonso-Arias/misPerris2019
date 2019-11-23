$(document).ready(function(){
            
    //Se desactiva el select de "Ciudad" cuando carga la página
    $('#ciudad').attr("disabled", true);

    $('#region').change(function()
    {
        //Esto ocurre al cambiar la opción del select de "Región"
        //Se elimina la opción con valor 0
        $('#region option[value="0"]').hide();

        //Se inicia la opción del select de "Ciudad" en blanco
        $('#ciudad').val(0);

        //Se guarda el valor de la región seleccionada
        var region = $('#region').val();
        
        //Se evalúa la variable región
        if(region == 0)
        {
            /*
            Si la opción del select corresponde a "--Elegir una opción--" (equivalente a 0)
            se desactiva el select de "Ciudad"
            */
            $('#ciudad').attr("disabled", true);
        }
        else
        {
            //De lo contrario, se quita el atributo "disabled" para activar el select de "Ciudad"
            $('#ciudad').attr("disabled", false);

            //Se ocultan todas las regiones
            $('#ciudad option').hide();
            
            //Se utiliza la variable región para filtrar las ciudades que estén relacionadas con esta
            $('#ciudad option[value="' + region + '"]').show();
        }
    });
})