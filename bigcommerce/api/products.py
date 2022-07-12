from dataclasses import dataclass
from saferite.core import BCBase
from ..data import ProductData

@dataclass
class Product:
    def __init__(self, token:str, client:str, store_hash:str):
        self.module = 'catalog/products'
        self.base = BCBase(token, client, store_hash, 3)

    def list(self, **kwargs) -> dict:
        return self.base.api._standard_call(self.module, 'get', **kwargs)

    def get_by_id(self, product_id:str,) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}', 'get')

    def create(self, data:ProductData) -> dict:
        return self.base.api._standard_call(self.module, 'post', data)

    def update(self, product_id:str, data:ProductData) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}', 'put', data)

    def delete(self, product_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}', 'delete')

    def list_bulk_pricing(self, product_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/bulk-pricing-rules', 'get')

    def get_bulk_pricing_by_id(self, product_id:str, bulk_pricing_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/bulk-pricing-rules/{bulk_pricing_id}', 'get')

    def create_bulk_pricing(self, product_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/bulk-pricing-rules', 'post', data)

    def update_bulk_pricing(self, product_id:str, bulk_pricing_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/bulk-pricing-rules/{bulk_pricing_id}', 'put', data)

    def delete_bulk_pricing(self, product_id:str, bulk_pricing_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/bulk-pricing-rules/{bulk_pricing_id}', 'delete')

    def list_metafields(self, product_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/metafields', 'get')

    def get_metafield_by_id(self, product_id:str, metafield_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/metafields/{metafield_id}', 'get')

    def create_metafield(self, product_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/metafields', 'post', data)

    def update_metafield(self, product_id:str, metafield_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/metafields/{metafield_id}', 'put', data)

    def delete_metafield(self, product_id:str, metafield_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/metafields/{metafield_id}', 'delete')

    def list_variants(self, product_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/variants', 'get')

    def get_variant_by_id(self, product_id:str, variant_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/variants/{variant_id}', 'get')

    def create_variant(self, product_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/variants', 'post', data)

    def update_variant(self, product_id:str, variant_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/variants/{variant_id}', 'put', data)

    def delete_variant(self, product_id:str, variant_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/variants/{variant_id}', 'delete')

    def list_options(self, product_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/options', 'get')

    def get_option_by_id(self, product_id:str, option_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/options/{option_id}', 'get')

    def create_option(self, product_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/options', 'post', data)

    def update_option(self, product_id:str, option_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/options/{option_id}', 'put', data)

    def delete_option(self, product_id:str, option_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/options/{option_id}', 'delete')

    def list_custom_fields(self, product_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/custom-fields', 'get')

    def get_custom_fields_by_id(self, product_id:str, custom_field_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/custom-fields/{custom_field_id}', 'get')

    def create_custom_field(self, product_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/custom-fields', 'post', data)

    def update_custom_field(self, product_id:str, custom_field_id:str, data:dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/custom-fields/{custom_field_id}', 'put', data)

    def delete_custom_field(self, product_id:str, custom_field_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{product_id}/custom-fields/{custom_field_id}', 'delete')
