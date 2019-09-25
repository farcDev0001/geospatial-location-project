from pymongo import MongoClient
import pandas as pd
from getMongoClient import getClient
from getEnv import getVariable
def officePhilaOk():
    client = getClient()
    dbCompanies = client.companies
    cambridge1m = list(dbCompanies.philadelphia.find())
    listCambridge = getListOffice2km(cambridge1m,dbCompanies)


    return listCambridge


def getCompaniesNear(lat,long, max_Distance,db):
    return list(db.cambridge.find({
        "position": {
            "$near": {
               "$geometry": {
                  "type": "Point" ,
                  "coordinates": [ long , lat ]
               },
               "$maxDistance": max_Distance
               
             }
       }
    }))

def getListOffice2km(listOffice,db):
    listDf = []
    for ele in listOffice:
        if ele['founded_year'] > 2008:
            df = pd.DataFrame(getCompaniesNear(ele['lat'],ele['long'],2000,db))
            listDf.append({'office':ele,'df':df.reset_index().drop(columns='index')})
    return listDf