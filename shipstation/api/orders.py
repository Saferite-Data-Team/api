from saferite.core import ShipstationBase


class Orders(ShipstationBase):
    def __init__(self, username: str, password: str):
        self.base = ShipstationBase(username, password)
        self.module = 'orders'
        
    def while_(self,**kwargs):
            page = 1
            pages = 1
            data_full = []
            while page <= pages:
                data = self.get_by_all(page=page,**kwargs)
                data_full+=data['orders']
                page += 1
                pages = data['pages']
            return data_full   
         
    def get_by_all(self, page: int = 1, **kwargs):
        """List all orders with pagination.
        Args:
            page (int): Defaults to 1.
        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'get', page=page, **kwargs)

    def create(self, data: dict) -> dict:
        return self.base.api._standard_call(f'{self.module}/createorder', 'post', data)
