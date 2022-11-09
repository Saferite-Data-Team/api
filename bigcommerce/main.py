from bigcommerce.api import *
from saferite.core import BCBase


class BC:
    def __init__(self, token:str, store_hash:str):
        self.customer = customers.Customer(token, store_hash)
        self.order = orders.Order(token, store_hash)
        self.product = products.Product(token, store_hash)
        self.brand = brands.Brand(token, store_hash)
