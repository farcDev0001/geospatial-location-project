from pymongo import MongoClient
import pandas as pd
from getMongoClient import getClient

def getDictOffice(offices):
    listdictOffice = []
    for ele in offices:
        if len(ele['offices']) > 0:
            for i in range(len(ele['offices'])):
                city = ele['offices'][i]['city']
                if city == 'Philadelphia':
                    name = ele['name']
                    cat = ele['category_code']
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

def writeJson():
    client = getClient()
    dbCompanies = client.companies

    

    phi = list(dbCompanies.companies.find({
                                            "offices.city":{'$regex':'Philadel'},
                                            'founded_year':{'$ne':None},
                                           "offices.latitude":{'$ne':None},
                                           "offices.longitude":{'$ne':None}}, 
    {'name':1,'category_code':1,"offices.city":1,'total_money_raised':1,"offices.latitude":1,"offices.longitude":1,'founded_year':1},
                                 ))

    data = getDictOffice(phi)
    dfOffice = pd.DataFrame(data)
    dfOffice['position']=dfOffice.apply(createGeoJson,axis = 1)
    dfOffice.to_json('../outputs/philaOffices.json',orient="records")