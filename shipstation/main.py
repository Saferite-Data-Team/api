from shipstation.api import *

class Shipstation:
    def __init__(self, username:str, password:str):
        self.orders = orders.Orders(username, password)
        self.shipments = shipments.Shipments(username, password)