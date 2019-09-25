from apiQueries import getJsonFourSquare
def filterCitiesAirport(city):
    try:
        json = getJsonFourSquare(city['lat'],city['long'],'airport terminal',30000,lim =15)
        for ele in json['response']['groups'][0]['items']:
            if ele['venue']['name'].upper().find('TERMINAL')!=-1:
                return True
        return False
    except Exception():
        return False

