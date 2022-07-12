from books.main import Books
from bigcommerce.main import BC
import pymongo
from bson import ObjectId
from env import ENV

MONGO_USER = ENV['mongo_user']
MONGO_PASS = ENV['mongo_pass']
MONGO_SERVER = ENV['mongo_server']
ISP_TOKEN = ENV['isp_token']
ISP_HASH = ENV['isp_hash']
ISP_CLIENT = ENV['isp_client']

mongo = pymongo.MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_SERVER}/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
db = mongo['Zoho_Mirror']
books_token = db.OAuth.find_one({'_id': ObjectId('60101de5d25a83d3ca0d8139')})['token']
inv_token = db.OAuth.find_one({'_id':ObjectId('606c717b970ed2835e2db208')})['token']

def main():
    bc = BC(ISP_TOKEN, ISP_CLIENT, ISP_HASH)
    print(bc.customer.get_by_id('127764'))
    zoho = Books(books_token)
    zoho.salesorder.create()
    # print(zoho.items.list(page=2))
    
if __name__ == '__main__':
    main()
