def getDictOffice(offices):
    listdictOffice = []
    for ele in offices:
        if len(ele['offices']) > 0:
            for i in range(len(ele['offices'])):
                name = ele['name']
                cat = ele['category_code']
                city = ele['offices'][i]['city']
                money = ele['total_money_raised']
                year = ele['founded_year']
                latitude = ele['offices'][i]['latitude']
                longitude = ele['offices'][i]['longitude']
                listdictOffice.append({'name':name,'category':cat,'city':city,'money_raised':money,'founded_year':year,
                                      'lat':latitude,'long':longitude})
    return listdictOffice

def createGeoJson(dfOffice):
    return {
        "type":"Point",
        "coordinates":[dfOffice["long"],dfOffice["lat"]]
    }

def writeJsonOfficeCambridge():
    from pymongo import MongoClient
    import pandas as pd
    from getMongoClient import getClient
    client = getClient()
    dbCompanies = client.companies

    '''Voy a hacer una búsqueda de las compañías de videojuegos quedándome con las oficinas, 
    el nombre, el año y el dinero que han ganado, también las que tienen una M en el dinero ganado, 
    así sabré cuáles han facturado un millón o más de cualquier divisa'''

    cambridge = list(dbCompanies.companies.find({
                                            "offices.city":{'$regex':'Cambridge'},
                                            'founded_year':{'$ne':None},
                                           "offices.latitude":{'$ne':None},
                                           "offices.longitude":{'$ne':None}}, 
    {'name':1,'category_code':1,"offices.city":1,'total_money_raised':1,"offices.latitude":1,"offices.longitude":1,'founded_year':1},
                                 ))

    data = getDictOffice(cambridge)
    dfOffice = pd.DataFrame(data)
    dfOffice['position']=dfOffice.apply(createGeoJson,axis = 1)
    dfOffice.to_json('../outputs/cambridgeOffices.json',orient="records")