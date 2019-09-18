def getCities(dictCities):
    cities = list(filter(filterCitiesAirport,dictCities))
    cities = list(filter(filterCitiesTrain,cities))
    return cities

def filterCitiesAirport(city):
    try:
        from apiQueries import getJsonFourSquare
        json = getJsonFourSquare(city['lat'],city['long'],'airport terminal',30000,lim =15)
        for ele in json['response']['groups'][0]['items']:
            if ele['venue']['name'].upper().find('TERMINAL')!=-1:
                return True
        return False
    except Exception():
        return False

def filterCitiesTrain(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'train station',20000,lim = 15)
    if len(json['response']['groups'][0]['items'])>10:
        return True
    return False