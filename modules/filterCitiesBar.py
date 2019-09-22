def filterBar(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'bar',10000,lim=55)
    try:
        if len(json['response']['groups'][0]['items'])>50:
            return True
        return False
    except Exception():
        return False

def filterVegan(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'vegan',10000,lim=21)
    try:
        if len(json['response']['groups'][0]['items'])>20:
            return True
        return False
    except Exception():
        return False