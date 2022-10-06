from dataclasses import dataclass
from saferite.core import BCBase, strict_types
from ..data import BrandData

@dataclass
class Brand:
    def __init__(self, token:str, store_hash:str):
        self.module = 'catalog/brands'
        self.base = BCBase(token, store_hash, 3)

    def get_all(self, **kwargs) -> dict:
        return self.base.api._standard_call(self.module, 'get', **kwargs)

    def get_by_id(self, brand_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{brand_id}', 'get')

    @strict_types
    def create(self, data:BrandData) -> dict:
        return  self.base.api._standard_call(self.module, 'post', data)

    @strict_types
    def update(self, brand_id:str, data:BrandData) -> dict:
        return self.base.api._standard_call(f'{self.module}/{brand_id}', 'put', data)

    def delete(self, brand_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{brand_id}', 'delete')
