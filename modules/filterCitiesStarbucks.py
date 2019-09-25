from apiQueries import getJsonFourSquare
def filterStarbucks(city):
    json = getJsonFourSquare(city['lat'],city['long'],'Starbucks',10000,lim = 10)
    try:
        if len(json['response']['groups'][0]['items'])>5:
            return True
        return False
    except Exception():
        return False

