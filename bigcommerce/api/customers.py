from dataclasses import dataclass
from saferite.core import BCBase

@dataclass
class Customer:
    def __init__(self, token:str, client:str, store_hash:str):
        self.module = 'customers'
        self.base = BCBase(token, client, store_hash, 3)

    def list(self, **kwargs) -> dict:
        return self.base.api._standard_call(self.module, 'get', **kwargs)

    def get_by_id(self, customer_ids:list) -> dict:
        return self.base.api._standard_call(f'{self.module}?id:in={self.base._convert_ids(customer_ids)}', 'get')

    def create(self, data:list) -> dict:
        return self.base.api._standard_call(self.module, 'post', data)

    def update(self, data:list) -> dict:
        return self.base.api._standard_call(f'{self.module}', 'put', data)

    def delete(self, customer_ids:list) -> dict:
        return self.base.api._standard_call(f'{self.module}?id:in={self.base._convert_ids(customer_ids)}', 'delete')

    def list_addresses(self, **kwargs) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses', 'get')

    def get_address_by_id(self, customer_ids:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses?customer_id:in={self.base._convert_ids(customer_ids)}')

    def create_address(self, data:list) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses', 'post', data)

    def update_address(self, data:list) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses', 'put', data)

    def delete_address(self, customer_address_ids:list) -> dict:
        return self.base.api._standard_call(f'{self.module}/address?id:in={self.base._convert_ids(customer_address_ids)}', 'delete')
