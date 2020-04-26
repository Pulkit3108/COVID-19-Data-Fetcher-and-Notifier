function updateMap(){
    console.log("Updating map with realtime data")
    fetch("/csvjson.json")
    .then(response => response.json())
    .then(rsp => {
        //console.log(rsp)
        rsp.forEach(element => {
            latitude = element.Lat;
            longitude = element.Long_;   
            
            cases = element.Confirmed;
            if(cases > 255) {
                colo = "rgb(255,0,0)";
            } 

            else {
                colo = `rgb(${cases},0,0)`
            }

            new mapboxgl.Marker({
                draggable: false,
                color : colo
                })
                .setLngLat([longitude, latitude])
                .addTo(map);

           
        });
    })
}
let interval = 20000;
setInterval(updateMap , interval)
