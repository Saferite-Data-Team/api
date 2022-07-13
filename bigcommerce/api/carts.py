from dataclasses import dataclass
from saferite.core import BCBase, strict_types
from ..data import CartData

@dataclass
class Cart:
    def __init__(self, token:str, client:str, store_hash:str):
        self.module = 'carts'
        self.base = BCBase(token, client, store_hash, 3)

    def get_by_id(self, cart_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{cart_id}', 'get')

    @strict_types
    def create(self, data:CartData) -> dict:
        return self.base.api._standard_call(self.module, 'get', data)

    def create_redirect_url(self, cart_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{cart_id}/redirect_urls', 'post')

    def delete(self, cart_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{cart_id}', 'delete')
