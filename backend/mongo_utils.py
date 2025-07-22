from pymongo import MongoClient

def get_trade_collection():
    client = MongoClient('mongodb://mongo:27017/')
    db = client['trading_db']
    return db['trades']
