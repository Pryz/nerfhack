$(document).ready(function() {
    newGameId = 0;
    var i = 0,max = 20, player1, player2;
    
    $(".save-players").on('click', function() {
        player1 = $('#player1').val();
        player2 = $('#player2').val();

        if (!player1 || !player2) {
            alert('Enter both the player names');
            return;
        }

        $.ajax({
            url: "http://192.168.162.136/api/create/" + player1 + '/' + player2,
            type: "GET",
            success: function(response) {
                newGameId = response.id;
                console.log('New Game Id = ' + newGameId);
                setPlayerNames();
            }
        });
        //setPlayerNames();
        $('#myModal').modal('hide');
    });
    
    $(".create-players").on('click', function() {
        $('#myModal').modal({
            show: true,
            refresh: true,
        });
    });
    
    setPlayerNames = function(){
        $('#player1-score, #player1-score').html('00');
        $('#player1-name').html(player1);
        $('#player2-name').html(player2);
        $('.start-button-container').hide();
        $('.players-list').show();
        updateScore();
    }
    
    updateScore = function() {
        console.log('Calling updateScore');
        $.ajax({
            url: "http://192.168.162.136/api/game/" + newGameId,
            type: "GET",
            success: function(response) {
                /**
                 * "Id": 1,
                    "Player1": "p1",
                    "Player2": "p2",
                    "Score1": 0,
                    "Score2": 0
                 */
                console.log('Score1 = ' + response.Score1);
                console.log('Score2 = ' + response.Score2);
                $('#player1-score').html(("0" + response.Score1).slice(-2));
                $('#player2-score').html(("0" + response.Score2).slice(-2));
            }
        });
        setTimeout(updateScore, 1000);
    }
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



