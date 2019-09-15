def getCities(dictCities):
    cities = list(filter(filterCitiesAirport,dictCities))
    return cities

def filterCitiesAirport(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'airport terminal',30000)
    for ele in json['response']['groups'][0]['items']:
        if ele['venue']['name'].upper().find('TERMINAL')!=-1:
            return True
    return False