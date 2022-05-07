function updateMap() {
    fetch('https://coronadatascraper.com/latest.json')
        .then(response => response.json())
        .then(data => {
            data.forEach(element => {
                longitude = element.coordinates[0];
                latitude = element.coordinates[1];
                cases = element.cases;
                if (cases > 255) {
                    color = "rgb(255,0,0)";
                } else {
                    color = `rgb(${cases},0,0)`;
                }
                new mapboxgl.Marker({
                        draggable: false,
                        color: color,
                    })
                    .setLngLat([longitude, latitude])
                    .addTo(map);
            });
        });
}
let interval = 20000;
setInterval(updateMap, interval)