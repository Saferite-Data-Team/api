from dataclasses import dataclass

from saferite.core import BCBase, strict_types

from ..data import OrderData, RefundData, ShipmentData, ShippingAddressData


@dataclass
class Order:
    def __init__(self, token:str, store_hash:str):
        self.module = 'orders'
        self.base = BCBase(token, store_hash, 2)
        self.base3 = BCBase(token, store_hash, 3)

    def get_all(self, **kwargs) -> list:
        return self.base.api._standard_call(self.module, 'get', **kwargs)

    def get_by_id(self, order_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}', 'get')

    @strict_types
    def create(self, data:OrderData) -> dict:
        return self.base.api._standard_call(self.module, 'post', data)

    @strict_types
    def update(self, order_id:str, data:OrderData) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}', 'put', data)

    def delete(self, order_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}', 'delete')

    def get_all_coupons(self, order_id:str) -> list:
        return self.base.api._standard_call(f'{self.module}/{order_id}/coupons', 'get')

    def get_all_products(self, order_id:str) -> list:
        return self.base.api._standard_call(f'{self.module}/{order_id}/products', 'get')

    def get_product_by_id(self, order_id:str, product_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/products/{product_id}', 'get')

    def get_all_statuses(self, **kwargs) -> list:
        return self.base.api._standard_call('order_statuses', 'get')

    def get_status_by_id(self, status_id:str) -> dict:
        return self.base.api._standard_call(f'order_statuses/{status_id}', 'get')

    def get_all_shipments(self, order_id:str) -> list:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipments', 'get')

    def get_shipment_by_id(self, order_id:str, shipment_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipments/{shipment_id}', 'get')

    @strict_types
    def create_shipment(self, order_id:str, data:ShipmentData) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipments', 'post', data)

    @strict_types
    def update_shipment(self, order_id:str, shipment_id:str, data:ShipmentData) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipments/{shipment_id}', 'put', data)

    def delete_shipments(self, order_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipments', 'delete')

    def delete_shipment_by_id(self, order_id:str, shipment_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipments/{shipment_id}', 'delete')

    def get_all_shipping_addresses(self, order_id:str) -> list:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipping_addresses','get')

    def get_shipping_addresses_by_id(self, order_id:str, address_id:str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipping_addresses/{address_id}','get')

    @strict_types
    def update_shipping_addresses(self, order_id:str, address_id:str, data:ShippingAddressData) -> dict:
        return self.base.api._standard_call(f'{self.module}/{order_id}/shipping_addresses/{address_id}','put', data)

    def get_all_transactions(self, order_id:str) -> dict:
        return self.base3.api._standard_call(f'{self.module}/{order_id}/transactions', 'get')

    def get_all_refunds(self, **kwargs) -> dict:
        return self.base3.api._standard_call(f'{self.module}/payment_actions/refunds', 'get', **kwargs)

    def get_refund_by_id(self, refund_id:str) -> dict:
        return self.base3.api._standard_call(f'{self.module}/payment_actions/refunds/{refund_id}', 'get')

    def get_refunds_by_order(self, order_id:str) -> dict:
        return self.base3.api._standard_call(f'{self.module}/{order_id}/payment_actions/refunds', 'get')

    @strict_types
    def create_refund(self, order_id:str, data:RefundData) -> dict:
        return self.base3.api._standard_call(f'{self.module}/{order_id}/payment_actions/refunds', 'post', data)
