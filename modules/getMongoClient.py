from getEnv import getVariable
from pymongo import MongoClient
def getClient():
    return MongoClient("mongodb://localhost:27017/")