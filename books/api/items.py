from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import ItemData

@dataclass
class Items:
    token:str
    organization_id:str

    def __post_init__(self):
        self.module= 'items'
        self.base = ZohoBooksBase(self.token, self.organization_id)

    def get_all(self, page: int = 1) -> dict:
        """Get the list of all active items with pagination."""
        return self.base.api._standard_call(self.module, 'get', page=page)

    def get_by_id(self, item_id: str) -> dict:
        """Get details of an existing item.

        Args:
            item_id (str): Item id of the item

        Returns:
            dict: Response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'get')
    
    def delete(self, item_id:str) -> dict:
        """Delete the selected item.
        Items that are part of transaction cannot be deleted.

        Args:
            item_id (str): item_id of the item to be deleted.

        Returns:
            dict: Response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'delete')

    def mark_as_active(self, item_id:str) -> dict:
        """Mark an inactive item as active.

        Args:
            item_id (str): item_id of the item to be activated.

        Returns:
            dict: API response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}/activate', 'post')
    
    def mark_as_inactive(self, item_id: str) -> dict:
        """Mark an active item as inactive.

        Args:
            item_id (str): item_id of the item to be activated.

        Returns:
            dict: API response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}/activate', 'post')

    @strict_types
    def create(self, data: ItemData) -> dict:
        """
        Creates a new item in Zoho Books.
        Call example_data method to build the JSON.
        """
        return self.base.api._standard_call(self.module, 'post', data=data)
    
    @strict_types
    def update(self, item_id:str, json:dict) -> dict:
        """Update the details of an item

        Args:
            item_id (str): Item id to be updated
            data (dict): Data in JSON format.

        Returns:
            dict: Response
        """
        return self.base.api._standard_call(f'{self.module}/{item_id}', 'put', json=json)