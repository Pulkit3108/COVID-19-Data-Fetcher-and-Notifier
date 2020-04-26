# CSF_Ninjas

First we imported notification package from plyer library so that the output will be shown as a notification bar.
Then we imported BeautifulSoup package from bs4 library so that we can pull data out of website.
Then the function notify_me() takes two arguments title and message . It will be shown in our notification bar.
Then the function getDataFromUrl() will fetch data from the listed website which is mohfw.gov.in.
Then we display the fetched data using for loop which can be shown both on notification bar and terminal.

New feature: Realtime Corona MAP-JS

For creating a realtime corona map we used Js Mapbox.
In function updateMap() we fetched data from covid-19 data set from various websites.
Then we took their latitude and longitude to display on map.
Also we wrote a condition regarding corona cases so that we can show places with different color markers(easyto identify).
Also we set interval for updating the data set to 20 sec.
