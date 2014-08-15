$(document).ready(function() {
    
    $("#matches > tbody").html("");

    $.ajax({
        url: "http://192.168.162.136/api/list",
        type: "GET",
        success: function(response) {
            console.log('Response for list : ' + response);
            var len = response.length();
            for (var i = 0; i<= len; i++) {
                var newRow = "<tr>" +
                "<td>"+ response[i][3]+"</td>" +
                "<td>"+ response[i][5] +"</td>" +
                "<td>"+ response[i][4] +"</td>" +
                "<td>"+ response[i][6] +"</td>" +
                "<td>"+ (parseInt(response[i][5]) > parseInt(response[i][6])) ? response[i][3] : response[i][4] +"</td>" +
                "</tr>";
                $('#matches > tbody').append(newRow);
            }
            
        }
    });
});