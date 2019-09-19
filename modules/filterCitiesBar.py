def filterBar(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'bar',10000,lim=75)
    try:
        if len(json['response']['groups'][0]['items'])>70:
            return True
        return False
    except BaseException():
        return False

def filterVegan(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'vegan',10000,lim=15)
    try:
        if len(json['response']['groups'][0]['items'])>10:
            return True
        return False
    except BaseException():
        return False