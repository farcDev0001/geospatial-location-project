def filterStarbucks(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'Starbucks',10000,lim = 15)
    try:
        if len(json['response']['groups'][0]['items'])>10:
            return True
        return False
    except Exception():
        return False