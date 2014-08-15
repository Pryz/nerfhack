$(document).ready(function() {

    $(".save-players").on('click', function() {
        var player1 = $('#player1').val();
        var player2 = $('#player2').val();

        if (!player1 || !player2) {
            alert('Enter both the player names');
            return;
        }

        $.ajax({
            url: "http://192.168.162.136/api/create/" + player1 + '/' + player2,
            type: "GET",
            beforeSend: function(e) {
                console.log('sending now');
            },
            success: function(response) {
                console.log('response.id');
            }
        });
        
        $('#myModal').modal('hide');
    });
    
    $(".create-players").on('click', function() {
        $('#myModal').modal({
            show: true,
            refresh: true,
        });
    });
    
    var i = 0,
    max = 20,
    
    timer = function() {
        console.log('i=' + i);
        i++;
        
        if(i % 2 == 0){
            console.log('updating 1');
            $('#player1-score').html(("0" + i).slice(-2));
        } else {
            console.log('updating 2');
            $('#player2-score').html(("0" + i).slice(-2));
        }
        
        if(i > max) return;
        setTimeout(timer, 1000);
    }

    //timer();
});



