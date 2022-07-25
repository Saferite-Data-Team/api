from dataclasses import dataclass
from saferite.core import BCBase, strict_types
from ..data import CustomerData, AddressData

@dataclass
class Customer:
    def __init__(self, token:str, client:str, store_hash:str):
        self.module = 'customers'
        self.base = BCBase(token, client, store_hash, 3)

    def get_all(self, **kwargs) -> dict:
        return self.base.api._standard_call(self.module, 'get', **kwargs)

    @strict_types
    def get_by_id(self, customer_ids:list) -> dict:
        return self.base.api._standard_call(f'{self.module}?id:in={self.base._convert_ids(customer_ids)}', 'get')

    @strict_types
    def create(self, data:list[CustomerData]) -> dict:
        return self.base.api._standard_call(self.module, 'post', self.base._serializer(data))

    @strict_types
    def update(self, data:list[CustomerData]) -> dict:
        return self.base.api._standard_call(f'{self.module}', 'put', self.base._serializer(data))

    @strict_types
    def delete(self, customer_ids:list) -> dict:
        return self.base.api._standard_call(f'{self.module}?id:in={self.base._convert_ids(customer_ids)}', 'delete')

    def get_all_addresses(self, **kwargs) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses', 'get')

    def get_address_by_id(self, customer_ids:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses?customer_id:in={self.base._convert_ids(customer_ids)}')

    @strict_types
    def create_address(self, data:AddressData) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses', 'post', data)

    @strict_types
    def update_address(self, data:list) -> dict:
        return self.base.api._standard_call(f'{self.module}/addresses', 'put', data)

    @strict_types
    def delete_address(self, customer_address_ids:list) -> dict:
        return self.base.api._standard_call(f'{self.module}/address?id:in={self.base._convert_ids(customer_address_ids)}', 'delete')
