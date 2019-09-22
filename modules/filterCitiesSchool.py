def filterUniversity(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'university',10000,lim = 5)
    try:
        if len(json['response']['groups'][0]['items'])>3:
            return True
        return False
    except Exception():
        return False

