from dataclasses import dataclass
from apis import ZohoBooksBase
import json
from datetime import datetime

@dataclass
class Items:
    base: ZohoBooksBase = ZohoBooksBase()
    module: str = 'items'

    def list(self) -> dict:
        """Get the list of all active items with pagination."""
        #[TODO] add pagination in the standard call
        return self.base.api._standard_call(self.module, 'GET')

    def get_by_id(self, item_id: str) -> dict:
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'GET')
    
    def create(self, data: json):
        """
        Creates a new item in Zoho Books.
        Use example_data to build the JSON.
        """
        return self.base.api._standard_call(self.module, 'POST', data=data)
    
    def example_data(self) -> dict:
        data = {
            "name": "Hard Drive",
            "rate": 120,
            "description": "500GB",
            "tax_percentage": "70%",
            "sku": "s12345",
            "product_type": "goods",
            "hsn_or_sac": "string",
            "is_taxable": True,
            "tax_exemption_id": "string",
            "account_id": " ",
            "avatax_tax_code": 982000000037049,
            "avatax_use_code": 982000000037049,
            "item_type": " ",
            "purchase_description": " ",
            "purchase_rate": " ",
            "purchase_account_id": " ",
            "inventory_account_id": " ",
            "vendor_id": " ",                      
            "reorder_level": " ",
            "initial_stock": " ",
            "initial_stock_rate": " ",
            "item_tax_preferences": [
                {
                    "tax_id": 982000000037049,
                    "tax_specification": "intra"
                    }
                    ]
                    }
        return data

class Books:
    items: Items = Items()

    def __repr__(self):
        now = datetime.now()
        expiration = 60 - now.minute
        return f'Zoho Books intance in 0x{id(self)}. Token will expire in {expiration} minutes'


