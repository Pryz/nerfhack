$(document).ready(function () {
    
    $(".save-players").on('click', function(){
        var player1 = $('#player1').val();
        var player2 = $('#player2').val();
        
        $.ajax({
            url: "http://192.168.162.136:5000/create/"+player1+'/'+player2,
            type: "GET",
            beforeSend: function(e){
              console.log('sending now');  
            },
            success: function (response) {
                console.log(response);
            }
        });
        $('#myModal').modal('hide');
    }); 
    
    $(".create-players").on('click', function(){
        $('#myModal').modal({
            show: true,
            refresh: true,
        });
    });
});



