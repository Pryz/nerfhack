$(document).ready(function() {
    
    $("#matches > tbody").html("");

    $.ajax({
        url: "http://192.168.162.136/api/list",
        type: "GET",
        success: function(response) {
            console.log('Response for list : ' + response);
            newRow = "<tr>" +
                "<td>"+ response.Player1 +"</td>" +
                "<td>"+ response.Score1 +"</td>" +
                "<td>"+ response.Player2 +"</td>" +
                "<td>"+ response.Score2 +"</td>" +
                "<td>"+ (parseInt(response.Score1) > parseInt(response.Score2)) ? response.Player1 : response.Player2 +"</td>" +
                "</tr>";
            $('#matches > tbody').append(newRow);
        }
    });
});