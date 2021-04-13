
//Geolocation script

var x = document.getElementById("result");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    x.innerHTML = "Your coordinates are - " + "<br><br>LAT: " + position.coords.latitude +
        "<br>LONG: " + position.coords.longitude + "<br><br> We can see you ;)";
}

