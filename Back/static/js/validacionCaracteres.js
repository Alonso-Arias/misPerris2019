/*Función Para que el Campo Solo Acepte Letras y Espacios*/
$('#nombre').on('input', function() {
    if (!/^[ a-z áéíóúüñ]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^ a-z áéíóúüñ]+/ig,"");
    }
});

$('#usuario').on('input', function() {
    if (!/^[a-z/0-9/-/-_.]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^a-z/0-9/-/-_.]+/ig,"");
    }
});

$('#password').on('input', function() {
    if (!/^[a-z/0-9/-/-_.]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^a-z/0-9/-/-_.]+/ig,"");
    }
});

$('#password2').on('input', function() {
    if (!/^[a-z/0-9/-/-_.]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^a-z/0-9/-/-_.]+/ig,"");
    }
});

/*Función Para que el Campo Solo Acepte Números*/
$('#telefonoCon').on('input', function() {
    if (!/^[0-9]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^0-9]+/ig,"");
    }
});

/*Función Para que el Campo del Rut Acepte los Caracteres Correctos*/
$('#rut').on('input', function() {
    if (!/^[k/0-9/-/-.]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^k/0-9/-/-.]+/ig,"");
    }
});

/*Función Para que el Campo de Correo Electrónico Acepte los Caracteres Correctos*/
$('#correoElectronico').on('input', function() {
    if (!/^[a-z-/áéíóúüñ/0-9/./-/_/@]*$/i.test(this.value)) {
        this.value = this.value.replace(/[^a-z-/áéíóúüñ/0-9/./-/_/@]+/ig,"");
    }
});

/*Función Para que el Campo del Teléfono Acepte Como Máximo 8 Caracteres*/
$(document).ready(function(){
    $('#telefonoCon').attr('maxlength','8');
});

/*Función Para que el Campo del Teléfono Acepte Como Máximo 8 Caracteres*/
$(document).ready(function(){
    $('#correoElectronico').attr('maxlength','76');
});

//*Función Para que el Campo del Nombre Acepte Como Máximo 30 Caracteres*
$(document).ready(function(){
    $('#nombre').attr('maxlength','30');
});




