from saferite.core import ShipstationBase

class Shipments(ShipstationBase):
    def __init__(self, username:str, password:str):
        self.base = ShipstationBase(username, password)
        self.module = 'shipments'
        
    def list(self, **kwargs) -> dict:
        additional_args = ''.join([f'{k}={str(v)}&' for k,v in locals()['kwargs'].items()])[:-1]
        return self.base.api._standard_call(f'{self.module}?{additional_args}', 'get', **kwargs)