from saferite.core import ShipstationBase

class Orders(ShipstationBase):
    def __init__(self, username:str, password:str):
        self.base = ShipstationBase(username, password)
        self.module = 'orders'
        
    def get_by_id(self, order_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}', 'get')
    
    def create(self, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/createorder', 'post', data)