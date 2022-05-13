from dataclasses import dataclass
from saferite.core import ZohoBooksBase, ZohoData

ITEM_SCHEMA = {
    "name": "ItemData",
    "type": "object",
    "properties": {
        "name": { "type": "string" },
        "rate": { "type": "number" },
        "description": { "type": "string" },
        "tax_percentage": {"type": "string"},
        "sku": { "type": "string" },
        "product_type": {
            "type": "string",
            "enum": ["goods", "service", "digital_service"]
            },
        "is_taxable": {"type": "boolean"},
        "tax_exemption_id": {"type": "string"},
        "account_id": {"type": "string"},
        "avatax_tax_code": {"type": "string"},
        "avatax_use_code": {"type": "string"},
        "item_type": {
            "type": "string",
            "enum": ["sales", "purchases", "sales_and_purchases", "inventory"]
            },
        "purchase_description": {"type": "string"},
        "purchase_rate": {"type": "string"},
        "purchase_account_id": {"type": "string"},
        "inventory_account_id": {"type": "string"},
        "vendor_id": {"type": "string"},
        "reorder_level": {"type": "string"},
        "initial_stock": {"type": "string"},
        "initial_stock_rate": {"type": "string"}
        },
    "additionalProperties": False,
    "if": {
        "properties": {"is_taxable": {"const": True}}
    },
    "then": {
        "required": ["name", "rate"]
    },
    "else": {
        "required": ["name", "rate", "tax_exemption_id"]
    }
        }

@dataclass
class ItemData(ZohoData):
    name: str
    rate: float
    description: str = None
    tax_percentage: str = None
    sku: str = None
    product_type: str = None
    is_taxable: bool = None
    tax_exemption_id: str = None
    account_id: str = None
    avatax_tax_code: str = None
    avatax_use_code: str = None
    item_type: str = None
    purchase_description: str = None
    purchase_rate: str = None
    purchase_account_id: str = None
    inventory_account_id: str = None
    vendor_id: str = None
    reorder_level: str = None
    initial_stock: str = None
    initial_stock_rate: str = None

    @property
    def schema(self):
        return ITEM_SCHEMA

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
    
    def delete(self, item_id:str) -> dict:
        """Delete the selected item.
        Items that are part of transaction cannot be deleted.

        Args:
            item_id (str): item_id of the item to be deleted.

        Returns:
            dict: Response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'DELETE')

    def mark_as_active(self, item_id:str) -> dict:
        """Mark an inactive item as active.

        Args:
            item_id (str): item_id of the item to be activated.

        Returns:
            dict: API response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}/activate', 'POST')
    
    def mark_as_inactive(self, item_id: str) -> dict:
        """Mark an active item as inactive.

        Args:
            item_id (str): item_id of the item to be activated.

        Returns:
            dict: API response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}/activate', 'POST')

    def create(self, data: ItemData) -> dict:
        """
        Creates a new item in Zoho Books.
        Call example_data method to build the JSON.
        """
        return self.base.api._standard_call(self.module, 'POST', data=data)
    
    def update(self, item_id:str, data:dict) -> dict:
        """Update the details of an item

        Args:
            item_id (str): Item id to be updated
            data (dict): Data in JSON format.

        Returns:
            Response: dict
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'PUT', data=data)