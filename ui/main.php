<!DOCTYPE html>
<html>
    <head>
        <title>Nerf Hack</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- Bootstrap -->
        <link href="bootstrap/css/bootstrap.css" rel="stylesheet">
        <link rel="stylesheet" href="bootstrap/css/main.css">
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media
           queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page
           via file:// -->
        <!--[if lt IE 9]>
           <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/
              html5shiv.js"></script>
           <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/
              respond.min.js"></script>
        <![endif]-->
    </head>
    <body>

        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container">
                    <a class="brand" href="#">Project name</a>
                    <div class="nav-collapse collapse">
                        <ul class="nav">
                            <li class="active"><a href="main.php">Home</a></li>
                        </ul>
                    </div><!--/.nav-collapse -->
                </div>
            </div>
        </div>
        <div class="score-container">
            <a href="" class="btn btn-primary create-players" data-toggle="modal">Create Players</a>
        </div>

        <div class="modal hide fade" id ="myModal">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">X</button>
                        <h4 class="modal-title">Ebter Player's Name</h4>
                    </div>
                    <div class='player-container'>
                        <div class="form-group">
                            <label for="inputEmail" class="col-lg-2 control-label">Player 1</label>
                            <div class="col-lg-10">
                                <input type="text" class="form-control" id="player1" placeholder="Player 1">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="inputEmail" class="col-lg-2 control-label">Player 2</label>
                            <div class="col-lg-10">
                                <input type="text" class="form-control" id="player2" placeholder="Player 2">
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
                        <button class="btn btn-primary save-players">Save changes</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://code.jquery.com/jquery.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="bootstrap/js/bootstrap.js"></script>
        <script src="bootstrap/js/main.js"></script>
    </body>
</html>