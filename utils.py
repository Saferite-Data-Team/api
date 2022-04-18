import pymongo
from bson import ObjectId

def get_token(db: pymongo.database, service: str) -> str:
    tokens = {'Books': '60101de5d25a83d3ca0d8139'} #[TODO] Update database to find token by keyword
    return db.OAuth.find({'_id': ObjectId(tokens[service])}, {'_id': 0}).next()['token']