let map;

function initMap() {
  const myLatlng = { lat: -34.397, lng: 150.644 }
  map = new google.maps.Map(document.getElementById("map"), {
    center: myLatlng,
    zoom: 8,
  });
  const marker = new google.maps.Marker({
    position: myLatlng,
    map,
    title: "Click to zoom",
  });
}

window.initMap = initMap;

