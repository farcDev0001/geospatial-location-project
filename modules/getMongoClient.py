def getClient():
    from getEnv import getVariable
    from pymongo import MongoClient
    return MongoClient("mongodb://localhost:27017/")