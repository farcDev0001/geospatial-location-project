def getJsonByLiteralQuery(literalQuery,place):
    import requests as re
    from getEnv import getVariable
    url= "https://maps.googleapis.com/maps/api/place/autocomplete/json?input={}%20{}&inputtype=textquery&key={}".format(literalQuery,place,getVariable('mapsToken'))
    r = re.get(url)
    return r.json()

def getJsonByPositionRadius(listPosition,radius,placeType='',keyword=''):
    import requests as re
    from getEnv import getVariable
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&keyword={}&key={}".format(listPosition[0],listPosition[1],radius,placeType,keyword,getVariable('mapsToken'))
    r = re.get(url)
    return r.json()

def getJsonFourSquare(lat,long,query,radius,lim=1000):
    from getEnv import getVariable
    import requests as re
    url = 'https://api.foursquare.com/v2/venues/explore'

    params = {
    'client_id':getVariable('fourid'),
    'client_secret':getVariable('foursecret'),
    'v':'20180323',
    'll':'{},{}'.format(lat,long),
    'query':query,
    'radius':radius,
    'limit':lim
    }
    return re.get(url=url, params=params).json()




