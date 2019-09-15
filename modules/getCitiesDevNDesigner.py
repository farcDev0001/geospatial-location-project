def citiesDevNDesignerOK():
    from pymongo import MongoClient
    import pandas as pd
    from getMongoClient import getClient
    from getEnv import getVariable
    client = getClient()
    dbCompanies = client.companies
    videGamesMt1M = list(dbCompanies.officesVideo1M.find())
    listGame1M100K = getListOffice100km(videGamesMt1M,dbCompanies)
    maximo = 0
    
    for ele in listGame1M100K:
        if ele.name.count() > maximo:
            maximo = ele.name.count()
    
    '''al hacer un print de maximo sé que la maxima aglomeración de compañias 
    (radio = 100km) que me interesan (videojuegos >1M dolares ganados) es de 54
    por lo que considero aceptable quedarme con lugares en los que haya una aglomeración de más
    de la mitad (26 empresas), esos serán lugares que satisfagan a los diseñadores y a los programadores,
    a partir de ahora solo tengo que sacar una lista de esas ciudades'''

    listGame1M100K=list(filter(lambda df:False if df.name.count() in range(maximo//2,maximo+1) else True,listGame1M100K))

    cities = []
    citiesPos = []
    for df in listGame1M100K:
        for city in list(df.city.value_counts().index):
            if city not in cities:
                cities.append(city)
                citiesPos.append([df.loc[df['city'] == city].lat.mean(),df.loc[df['city'] == city].long.mean())
    return {cities[i]:citiesPos[i] for i in range(len(cities))}


def getCompaniesNear(lat,long, max_meters,db):
    return list(db.officesVideo1M.find({
        "position": {
            "$near": {
               "$geometry": {
                  "type": "Point" ,
                  "coordinates": [ long , lat ]
               },
               "$maxDistance": max_meters
             }
       }
    }))

def getListOffice100km(listOffice,db):
    import pandas as pd
    listDf = []
    for ele in listOffice:
        df = pd.DataFrame(getCompaniesNear(ele['lat'],ele['long'],100000,db))
        df.reset_index()
        listDf.append(df[['name', 'money_raised','city', 'founded_year', 'lat', 'long']])
    return listDf

