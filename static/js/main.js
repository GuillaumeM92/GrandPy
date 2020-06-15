var myLatLng;

function initMap() {
    
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map
    });
}

$("#submit").on("click", function(e) {
    e.preventDefault();

    var user_input_value = document.getElementById("user_input").value;
    var chat = document.getElementById("chat");
    var newGrandpyText = document.createElement("div");
    var newUserText = document.createElement("p");

    if (user_input_value != "") {
        chat.appendChild(newUserText).append(user_input_value);
        document.getElementById("loading").hidden = false;

        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: "/question_handler",
            traditional: "true",
            data: JSON.stringify({user_input_value}),
            dataType: "json"
            }).done(
            function(data) {
                console.log(data)
                if (data["status"] == "ZERO_RESULTS") {
                    chat.appendChild(newGrandpyText).innerHTML = getRandomText(no_result);
                } else if (data == "ignore") {
                    chat.appendChild(newGrandpyText).innerHTML = ":)";
                } else {
                chat.appendChild(newGrandpyText).innerHTML = (getRandomText(answer1) + "<br>" + getRandomText(answer2) + data[0] + "<br>" + "<br>" + getRandomText(anecdote) + data[2]);
                myLatLng = data[1];
                initMap();
                console.log(data);
            }
        });

        setTimeout(function(){document.getElementById("loading").hidden = true;}, 2500);
        setTimeout(function(){document.getElementById("map").hidden = false;}, 2500);
        }

    else {
        chat.appendChild(newGrandpyText).append("Merci d'entrer une question valide.");
    }

});

/*
var myLatLng;

function initMap() {
    
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 18,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map
    });
}

$("#submit").on("click", function(e) {
    e.preventDefault();

    var user_input_value = document.getElementById("user_input").value;
    var chat = document.getElementById("chat");
    var newGrandpyText = document.createElement("div");
    var newUserText = document.createElement("p");

    if (user_input_value != "") {
        chat.appendChild(newUserText).append(user_input_value);
        document.getElementById("loading").hidden = false;

        $.ajax({
            type: "POST",
            contentType: "application/json; charset=utf-8",
            url: "/question_handler",
            traditional: "true",
            data: JSON.stringify({user_input_value}),
            dataType: "json"
            }).done(
            function(data) {
                if data === "ZERO_RESULTS" {
                    chat.appendChild(newGrandpyText).innerHTML = "erreur my son";
                } else {
                chat.appendChild(newGrandpyText).innerHTML = (getRandomText(answer1) + "<br>" + getRandomText(answer2) + data[0] + "<br>" + "<br>" + getRandomText(anecdote) + data[2]);
                myLatLng = data[1];
                initMap();
            }
        });

        setTimeout(function(){document.getElementById("loading").hidden = true;}, 2500);
        setTimeout(function(){document.getElementById("map").hidden = false;}, 2500);
        }

    else {
        chat.appendChild(newGrandpyText).append("Merci d'entrer une question valide.");
    }

});
*/