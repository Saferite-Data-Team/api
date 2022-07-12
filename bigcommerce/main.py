from saferite.core import BCBase
from bigcommerce.api import *

class BC:
    def __init__(self, token:str, client:str, store_hash:str):
        self.customer = customers.Customer(token, client, store_hash)
        self.order = orders.Order(token, client, store_hash)
        self.product = products.Product(token, client, store_hash)
        self.brand = brands.Brand(token, client, store_hash)
