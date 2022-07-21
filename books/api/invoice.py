from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import SOData, AddressData

@dataclass
class Invoice:
    def post_init_(self) -> None:
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module = 'invoices'

def create (self, data:dict):
        """Create an invoice for your customer.

        Args:
            data (dict)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'post', data=data)


