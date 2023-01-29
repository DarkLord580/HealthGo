let map;

function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

//usage:

function attachSecretMessage(marker, secretMessage) {
    const infowindow = new google.maps.InfoWindow({
      content: secretMessage,
    });
  
    marker.addListener("click", () => {
      infowindow.open(marker.get("map"), marker);
    });
}
function initMap() {
    const myLatlng = { lat: 37.242360, lng: -121.888214}, 
    map = new google.maps.Map(document.getElementById("map"), {
      center: myLatlng,
      zoom: 20,
    });
    readTextFile("./static/geo.json", function(text){
      var data = JSON.parse(text);
      console.log(data);
      for(x in data){
        const contentString =
        '<div id="content">' +
        '<div id="siteNotice">' +
        "</div>" +
        '<h1 style = "padding:20px;"id="firstHeading" class="firstHeading">Problem/Fun fact!</h1>' +
        '<div id="bodyContent">' +
        "<p> " +
        data[x].question+
        "</p>" +
        "<input type=\"text\" id=\"\">" + 
        "<button class= \"button4\" onclick=>Click Me</button>" +
        "</div>" +
        "</div>";
          console.log(data[x].latitude)
          console.log(typeof data[x].latitude)
          console.log(data[x].longitude)
          const marker = new google.maps.Marker({
              position: {lat: Number(data[x].latitude), lng:Number(data[x].longitude)},
              map,
              title: "Waypoint: " + data[x].id,
              
            });
            attachSecretMessage(marker, contentString);
      }
   
  });
    
  }
  
  window.initMap = initMap;
  