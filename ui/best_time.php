<!DOCTYPE html>
<html>
    <head>
        <title>Ad Invaders - Best Time</title>
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
        <style>
            @font-face{
                font-family:"digital-7";
                src: url(bootstrap/fonts/digital-7/digital-7-mono.ttf) format("truetype");
            }
        </style>

    </head>
    <body>
        <div class="navbar navbar-inverse navbar-fixed-top">
            <div class="navbar-inner">
                <div class="container">
                    <div class="nav-collapse collapse">
                        <ul class="nav">
                            <li class="active"><a href="main.php">New Game</a></li>
                            <li class="active"><a href="best_time.php">Best Time</a></li>
                            <li class="active"><a href="matches.php">Matches</a></li>
                        </ul>
                    </div><!--/.nav-collapse -->
                </div>
            </div>
        </div>
        <div class="logo-container">
            <img src="bootstrap/img/logo.png" alt="Logo">
        </div>
        
        <table id='best_time' class="table table-striped">
            <thead>
                <th>Player Name</th>
                <th>Score</th>
                <th>Time</th>
            </thead>
            <tbody>
                <tr>
                    <td>PGO</td>
                    <td>32</td>
                    <td>10 secs</td>
                </tr>
                <tr>
                    <td>JULIEN</td>
                    <td>32</td>
                    <td>14 secs</td>
                </tr>
                <tr>
                    <td>NATE</td>
                    <td>32</td>
                    <td>16 secs</td>
                </tr>
                <tr>
                    <td>TONY</td>
                    <td>32</td>
                    <td>19 secs</td>
                </tr>
                <tr>
                    <td>CJ</td>
                    <td>12</td>
                    <td>42 secs</td>
                </tr>
                <tr>
                    <td>CJ</td>
                    <td>16</td>
                    <td>49 secs</td>
                </tr>
                <tr>
                    <td>NATE</td>
                    <td>32</td>
                    <td>51 secs</td>
                </tr>
                <tr>
                    <td>CJ</td>
                    <td>32</td>
                    <td>59 secs</td>
                </tr>
            </tbody>
        </table>
        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://code.jquery.com/jquery.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="bootstrap/js/bootstrap.js"></script>
        <script src="bootstrap/js/best_time.js"></script>
    </body>
</html>