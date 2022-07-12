from dataclasses import dataclass
from saferite.core import BCBase
from ..data import CategoryData

@dataclass
class Category:
    def __init__(self, token:str, client:str, store_hash:str):
        self.module = 'catalog/categories'
        self.base = BCBase(token, client, store_hash, 3)

    def list(self, **kwargs) -> dict:
        return self.base.api._standard_call(self.module, 'get', **kwargs)

    def get_by_id(self, category_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{category_id}', 'get')

    def create(self, data:CategoryData) -> dict:
        return self.base.api._standard_call(self.module, 'post', data)

    def update(self, category_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{category_id}', 'put', data)

    def delete(self, category_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{category_id}', 'delete')
