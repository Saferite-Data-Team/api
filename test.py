from books.main import Books
from bigcommerce.main import BC
import pymongo
from bson import ObjectId
# from env import ENV

# MONGO_USER = ENV['mongo_user']
# MONGO_PASS = ENV['mongo_pass']
# MONGO_SERVER = ENV['mongo_server']
# ISP_TOKEN = ENV['isp_token']
# ISP_HASH = ENV['isp_hash']
# ISP_CLIENT = ENV['isp_client']

# mongo = pymongo.MongoClient(f'mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_SERVER}/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')
# db = mongo['Zoho_Mirror']
# books_token = db.OAuth.find_one({'_id': ObjectId('60101de5d25a83d3ca0d8139')})['token']
# inv_token = db.OAuth.find_one({'_id':ObjectId('606c717b970ed2835e2db208')})['token']

# def main():
#     bc = BC(ISP_TOKEN, ISP_CLIENT, ISP_HASH)
#     print(bc.customer.get_by_id('127764'))
#     zoho = Books(books_token)
#     zoho.salesorder.create()
#     # print(zoho.items.list(page=2))
    
# if __name__ == '__main__':
#     main()

import datetime as dt
USER="penelope"
PASS="MongoPenelope2"
SERVER="3.210.205.130:27017"
conn = pymongo.MongoClient(f"mongodb://{USER}:{PASS}@{SERVER}/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
db = conn['taxjar']
zoho_db = conn['Zoho_Mirror']['OAuth']
zoho_token = zoho_db.find_one({'_id': ObjectId('60101de5d25a83d3ca0d8139')})['token']

organization_id = '683229417' 
book = Books(zoho_token,organization_id )
first_day_in_month = dt.datetime.now().replace(day=1).strftime("%Y-%m-%dT%H:%M:%S-0400")  
# i = book.invoices.get_all()
book.invoices.get_all_complete(last_modified_time = first_day_in_month)
json_item  ={'name': 'SSH3505017',
 'rate': '253.79',
 'purchase_rate': '177.65',
 'is_returnable': True,
 'vendor_id': '1729377000002322717',
 'custom_fields': [
     {
         'customfield_id': '1729377000400744226',
         'value': '2022-09-30'
     }
]}
r = book.items.update('1729377000002268054',json_item)
print(r['message'])