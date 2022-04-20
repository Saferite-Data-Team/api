from dataclasses import dataclass
from saferite.core import ZohoBooksBase

@dataclass
class Items:

    def __init__(self, token:str, organization_id:str):
        self.module: str = 'items'
        self.base: ZohoBooksBase = ZohoBooksBase(token, organization_id)

    def list(self, page: int = 1) -> dict:
        """Get the list of all active items with pagination."""
        return self.base.api._standard_call(self.module, 'GET', page=page)

    def get_by_id(self, item_id: str) -> dict:
        """Get details of an existing item.

        Args:
            item_id (str): Item id of the item

        Returns:
            dict: Response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'GET')
    
    def delete(self, item_id:str):
        """Delete the selected item.
        Items that are part of transaction cannot be deleted.

        Args:
            item_id (str): item_id of the item to be deleted.

        Returns:
            dict: Response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'DELETE')

    def mark_as_active(self, item_id:str):
        """Mark an inactive item as active.

        Args:
            item_id (str): item_id of the item to be activated.

        Returns:
            dict: API response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}/activate', 'POST')
    
    def mark_as_inactive(self, item_id:str):
        """Mark an active item as inactive.

        Args:
            item_id (str): item_id of the item to be activated.

        Returns:
            dict: API response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}/activate', 'POST')

    def create(self, data: dict):
        """
        Creates a new item in Zoho Books.
        Call example_data method to build the JSON.
        """
        return self.base.api._standard_call(self.module, 'POST', data=data)
    
    def update(self, item_id:str, data:dict):
        """Update the details of an item

        Args:
            item_id (str): Item id to be updated
            data (dict): Data in JSON format.

        Returns:
            Response: dict
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'PUT', data=data)
    

    def example_data(self) -> dict:
        """Example item data JSON. Use it as reference for item creation or update.

        Returns:
            dict
        """
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