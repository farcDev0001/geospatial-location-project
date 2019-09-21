def cleanDistrites(cities):
    listCityRep = ['Brooklyn','Santa Monica','Culver City','Century City','El Segundo','Palo Alto','West Hollywood','Beverly Hills']
    cities = list(filter((lambda city:False if city['city'] in listCityRep else True),cities))
    cities[-3]['city']='Mumbai'
    return cities
    