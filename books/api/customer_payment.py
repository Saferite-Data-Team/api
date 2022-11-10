from dataclasses import dataclass
from books.data import PaymentData

from saferite.core import ZohoBooksBase, strict_types

@dataclass
class Payment:
    token:str
    organization_id:str
    
    def __post_init__(self) -> None:
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module = "customerpayments"
        
    @strict_types
    def create(self, data:PaymentData):
        """Create a payment for your invoices
        Args:
            data (dict)
        Returns
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'post', json_data=data.json)





