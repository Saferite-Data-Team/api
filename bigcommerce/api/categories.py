from dataclasses import dataclass
from saferite.core import BCBase, strict_types
from ..data import CategoryData

@dataclass
class Category:
    def __init__(self, token:str, client:str, store_hash:str):
        self.module = 'catalog/categories'
        self.base = BCBase(token, client, store_hash, 3)

    def get_all(self, **kwargs) -> dict:
        return self.base.api._standard_call(self.module, 'get', **kwargs)

    def get_by_id(self, category_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{category_id}', 'get')

    @strict_types
    def create(self, data:CategoryData) -> dict:
        return self.base.api._standard_call(self.module, 'post', data)

    @strict_types
    def update(self, category_id:str, data:CategoryData) -> dict:
        return self.base.api._standard_call(f'{self.module}/{category_id}', 'put', data)

    def delete(self, category_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{category_id}', 'delete')
