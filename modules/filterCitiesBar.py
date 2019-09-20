def filterBar(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'bar',10000,lim=100)
    try:
        if len(json['response']['groups'][0]['items'])>90:
            return True
        return False
    except Exception():
        return False

def filterVegan(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'vegan',10000,lim=60)
    try:
        if len(json['response']['groups'][0]['items'])>55:
            return True
        return False
    except Exception():
        return False