def filterUniversity(city):
    from apiQueries import getJsonFourSquare
    json = getJsonFourSquare(city['lat'],city['long'],'university',10000)
    if len(json['response']['groups'][0]['items'])>6:
        return True
    return False