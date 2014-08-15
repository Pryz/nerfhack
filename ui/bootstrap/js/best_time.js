$(document).ready(function() {
    return;
    $("#best_time > tbody").html("");

    $.ajax({
        url: "http://192.168.162.136/api/bestTime",
        type: "GET",
        success: function(response) {
            console.log('Response for bestTime : ' + response);
            newRow = "<tr>" +
                "<td>"+ response.Player1 +"</td>" +
                "<td>"+ response.Score1 +"</td>" +
                "<td>"+ response.Time +"</td>" +
                "</tr>";
            $('#best_time > tbody').append(newRow);
        }
    });
});