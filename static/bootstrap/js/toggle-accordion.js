
$('#h2-icon-1').click(function(){
    if($('#icon-1').hasClass('fa-minus')){
        $('#icon-1').toggleClass('fa-minus fa-plus')			
    }
    else if($('#icon-1').hasClass('fa-plus')){
        $('#icon-1').toggleClass('fa-minus fa-plus')
        if($('#icon-2').hasClass('fa-minus')){
            $('#icon-2').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-3').hasClass('fa-minus')){
            $('#icon-3').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-4').hasClass('fa-minus')){
            $('#icon-4').toggleClass('fa-minus fa-plus')
        }
    }
});

$('#h2-icon-2').click(function(){
    if($('#icon-2').hasClass('fa-minus')){
        $('#icon-2').toggleClass('fa-minus fa-plus')
    }
    else if($('#icon-2').hasClass('fa-plus')){
        $('#icon-2').toggleClass('fa-minus fa-plus')
        if($('#icon-1').hasClass('fa-minus')){
            $('#icon-1').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-3').hasClass('fa-minus')){
            $('#icon-3').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-4').hasClass('fa-minus')){
            $('#icon-4').toggleClass('fa-minus fa-plus')
        }
    }
});

$('#h2-icon-3').click(function(){
    if($('#icon-3').hasClass('fa-minus')){
        $('#icon-3').toggleClass('fa-minus fa-plus')			
    }
    else if($('#icon-3').hasClass('fa-plus')){
        $('#icon-3').toggleClass('fa-minus fa-plus')
        if($('#icon-1').hasClass('fa-minus')){
            $('#icon-1').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-2').hasClass('fa-minus')){
            $('#icon-2').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-4').hasClass('fa-minus')){
            $('#icon-4').toggleClass('fa-minus fa-plus')
        }
    }
});

$('#h2-icon-4').click(function(){
    if($('#icon-4').hasClass('fa-minus')){
        $('#icon-4').toggleClass('fa-minus fa-plus')			
    }
    else if($('#icon-4').hasClass('fa-plus')){
        $('#icon-4').toggleClass('fa-minus fa-plus')
        if($('#icon-1').hasClass('fa-minus')){
            $('#icon-1').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-2').hasClass('fa-minus')){
            $('#icon-2').toggleClass('fa-minus fa-plus')
        }
        if($('#icon-3').hasClass('fa-minus')){
            $('#icon-3').toggleClass('fa-minus fa-plus')
        }
    }
});