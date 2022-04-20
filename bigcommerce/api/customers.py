from saferite.core import BCBase

class Customer:
    def __init__(self, token:str, client:str, store_hash:str):
        self.module = 'customers'
        self.base = BCBase(token, client, store_hash, 2)

    def create(self, data:dict) -> dict:
        return self.base.api._standard_call(self.module, 'POST', data)
    
    def get_by_id(self, customer_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{customer_id}', 'GET')