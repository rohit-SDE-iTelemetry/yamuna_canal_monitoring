// // Initialize and add the map
// function initMap() {
//     // The location of Uluru
//     const uluru = { lat: 30.3, lng: 77.583333 };
//     // The map, centered at Uluru
//     const map = new google.maps.Map(document.getElementById("map"), {
//       zoom: 15,
//       center: uluru,
//     });
//     // The marker, positioned at Uluru
//     const marker = new google.maps.Marker({
//       position: uluru,
//       map: map,
//     });
//   }
  
//   window.initMap = initMap;

var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
  });
}

var marker1 = new google.maps.Marker({
  position: {lat: -34.397, lng: 150.644},
  map: map
});
var marker2 = new google.maps.Marker({
  position: {lat: -35.397, lng: 151.644},
  map: map
});
var marker3 = new google.maps.Marker({
  position: {lat: -36.397, lng: 152.644},
  map: map,
  title: 'Marker 3',
  icon: 'https://example.com/marker3.png',
  label: '3'
});
