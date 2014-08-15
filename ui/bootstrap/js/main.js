$(document).ready(function() {

    //$('#game-start-audio').get(0).play();
    
    newGameId = 0;
    var player1, player2, mode;

    $(".save-players").on('click', function() {
        player1 = $('#player1').val();
        player2 = $('#player2').val();
        mode = $('input[name=mode]:checked').val();

        if (!player1 || (mode === 'double' && !player2)) {
            alert('Player name is missing');
            return;
        }

        var APIurl = "http://192.168.162.136/api/create/" + mode + '/' + player1;

        if (mode === 'double')
            APIurl += '/' + player2;

        $.ajax({
            url: APIurl,
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

    /*Show/hide player two*/
    $('input[name=mode]').on('change', function() {
        var radioValue = $('input[name=mode]:checked').val();
        if (radioValue === 'double') {
            $('.control-group.double').show();
        } else {
            $('.control-group.double').hide();
        }
    });

    setPlayerNames = function() {
        $('#player1-score').html('00');
        $('#player1-name').html(player1);

        if (mode === 'double') {
            $('#player2-score').html('00');
            $('#player2-name').html(player2);
        }
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

                if (mode === 'double') {
                    if (response.Score1 == 16)
                        winningMessage(1);
                    if (response.Score2 == 16)
                        winningMessage(2);
                }

                $('#player1-score').html(("0" + response.Score1).slice(-2));
                if (mode === 'double') {
                    $('#player2-score').html(("0" + response.Score2).slice(-2));
                }
            }
        });
        setTimeout(updateScore, 1000);
    }

    winningMessage = function(playerNumber) {
        $(".player-dashboard").not('.player-' + playerNumber).hide();
        $('.winning-trophy').show();
    }
    
    playAudioAgain = function() {
        $('#game-start-audio').get(0).play();
    }
});



