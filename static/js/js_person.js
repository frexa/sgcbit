    $(document).ready(function () {
        $('#sidebarCollapse').on('click', function () {
            $('#sidebar').toggleClass('active');
        });
    });

    $('#carrusel').carousel({
        interval:6000,
        pause:false,
        wrap:true
    });

setTimeout(function() {
    if ($('#msg').length>0)
        {
            $('#msg').remove();
        }
    },2000)

function abrir_modal(url){
    $('#modal').load(url,function(){
        $(this).modal({
            backdrop:'static',
            keyboard:false
        })
        $(this).modal('show');
    });
    return false;
}

function cerrar_modal(){
    $('#modal').modal('hide');
    return false;
}

    window.onload = function () {
        var contenedor = document.getElementById('carga_container');
        contenedor.style.visibility = 'hedden';
        contenedor.style.opacity = '0';
    }