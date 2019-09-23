# geospatial-location-project

In this project I locate a company based on given conditions. My starting point is a Crunchbase dataset.

## Results in Tableau
https://public.tableau.com/profile/francisco.rodrigo#!/vizhome/MONGO-PROJECTFranciscoRodrigo/MongoProject?publish=yes


## Results capture (OpenStreetMaps+Plotly)

![Alt text](./outputs/map.png?raw=true "Map")

## Steps
* To import the dataset to a MongoDb Server
* Queries and $near functions to locate the companies.
* Filtering the cities of companies offices using the FourSquare API.
* Choosing a city using filtering criteria and some web scraping.
* Adding interest points near companies in the city using FourSquare API.
* Drawing a map using plotly and OpenStreetMaps.

## Next Steps
* Refactorize code



