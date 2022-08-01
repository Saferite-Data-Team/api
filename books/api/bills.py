from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import BillsData



@dataclass
class Bills:
    token:str
    organization_id:str
    
    def __post_init__(self):
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module = 'bills'
    





   