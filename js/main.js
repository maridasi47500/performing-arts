

if (window.location.pathname === "/voir") {
    const latitude = member_lat.value;
    const longitude = member_lon.value;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);

var map = L.map('map').setView([latitude, longitude], 13);
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
setTimeout(function () {
    map.invalidateSize();
}, 0);
}


if ((window.location.pathname === "/signup" || window.location.pathname === "/ajouter1chanson") && latuser.innerHTML === "" && lonuser.innerHTML === "" && myuserid.innerHTML !== "") {
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(function(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);

var map = L.map('map').setView([latitude, longitude], 13);
member_lat.value=latitude;
member_lon.value=longitude;
L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);
setTimeout(function () {
    map.invalidateSize();
}, 0);
	  map.on('mouseup', function(e) {
    const latitude = e.latlng.lat;
    const longitude = e.latlng.lng;
member_lat.value=latitude;
member_lon.value=longitude;
var popup = L.popup()
    .setLatLng([parseFloat(latitude), parseFloat(longitude)])
    .setContent("cette personne est ici")
    .openOn(map);
	  });
  });


} else {
  console.log("Geolocation is not supported by this browser.");
}


}
if (document.getElementById("somepic")){
    function readFile() {
	          if (this.files && this.files[0]) {
			          var FR= new FileReader();
			          FR.onload = function(e) {
					            document.getElementById("imgupload").src = e.target.result;
					            document.getElementById("imgupload").style.width = "80px";

					          };
			          FR.readAsDataURL( this.files[0] );
			        }
	        }

    document.getElementById("somepic").addEventListener("change", readFile, false);

}
