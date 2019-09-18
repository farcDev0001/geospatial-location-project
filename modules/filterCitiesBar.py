def filterBar(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'bar',10000)
    try:
        if len(json['response']['groups'][0]['items'])>70:
            return True
        return False
    except BaseException():
        return False