def getJsonByLiteralQuery(literalQuery,place):
    import requests as re
    from getEnv import getVariable
    url= "https://maps.googleapis.com/maps/api/place/autocomplete/json?input={}%20{}&inputtype=textquery&key={}".format(literalQuery,place,getVariable('mapsToken'))
    r = re.get(url)
    return r.json()

def getJsonByPositionRadius(lat,long,radius,placeType='',keyword=''):
    import requests as re
    from getEnv import getVariable
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&keyword={}&key={}".format(lat,long,radius,placeType,keyword,getVariable('mapsToken'))
    r = re.get(url)
    return r.json()
    