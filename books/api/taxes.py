from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import TaxData


@dataclass
class Taxes:
    token:str
    organization_id: str

    def __post_init__(self):
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module  = "settings"
    @strict_types
    def create( self, data:TaxData):
        """Create a tax which can be associated with an item.

        Args:
            data (TaxData)
        """
        return self.base.api._standard_call(f'{self.module}/taxes', 'post', data=data)

    def get_all(self, page=1):
        """List of simple and compound taxes with pagination.

        Args:
            page (int): Defaults to 1.
        """
        return self.base.api._standard_call(f'{self.module}/taxes', 'get', page=page)

    @strict_types
    def update (self, tax_id:str, data:TaxData):
        """Update the details of a simple or compound tax.

        Args:
            data (TaxData)
            tax_id(str)
        """
        return self.base.api._standard_call(f'{self.module}/taxes{tax_id}', 'put', data=data)

    def get_by_id(self, tax_id:str):
        """Get the details of a simple or compound tax.

        Args:
            tax_id (str)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}/taxes/{tax_id}', 'get')
    
    def delete(self, tax_id:str):
        """Delete a simple or compound tax.

        Args:
            tax_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/taxes/{tax_id}', 'delete')

    @strict_types
    def update_tax_group(self, tax_group_id:str, data:dict):
        """Update the details of the tax group.

        Args:
            tax_group_id (str): _description_
            data (dict): {
                tax_group_name(str): Name of the tax group to be created.   
                taxes(str): Comma Seperated list of tax IDs that are to be associated to the tax group.
            }
        """
        return self.base.api._standard_call(f'{self.module}/taxgroups/{tax_group_id}','put', data=data)

    def get_a_tax_group(self, tax_group_id:str):
        """Get the details of a tax group.

        Args:
            tax_group_id (str): 
        """
        return self.base.api._standard_call(f'{self.module}/taxgroups/{tax_group_id}','get')

    @strict_types
    def create_tax_group(self, data:dict):
        """Create a tax group associating multiple taxes.

        Args:
             data (dict): {
                tax_group_name(str): Name of the tax group to be created.   
                taxes(str): Comma Seperated list of tax IDs that are to be associated to the tax group.
            }
        """
        return self.base.api._standard_call(f'{self.module}/taxgroups/', 'post', data=data)
    
    def delete_tax_group(self, tax_group_id:str):
        """Delete a tax group. Tax group that is associated to transactions cannot be deleted.

        Args:
            tax_group_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/taxgroups/:{tax_group_id}', 'delete')

    @strict_types
    def create_tax_authority(self, data:dict):
        """Create a tax authority.

        Args:
            data (dict): {
                "tax_authority_name": "Illinois Department of Revenue",
                "description": "The New York State Department of  Taxation and Finance",
            }

        """
        return self.base.api._standard_call(f'{self.module}/taxauthorities', 'post', data=data)
    
    def get_all_tax_authorities(self):
        """List of tax authorities.
        """ 
        return self.base.api._standard_call(f'{self.module}/taxauthorities', 'get')

    @strict_types
    def update_tax_authority(self, tax_authority_id:str, data:dict):
        """Update the details of a tax authority.

        Args:
            tax_authority_id (str)
            data (dict) ={
                "tax_authority_name": "Illinois Department of Revenue",
                "description": "The New York State Department of  Taxation and Finance",
            }
        """
        return self.base.api._standard_call(f'{self.module}/taxauthorities/{tax_authority_id}', 'put', data=data)
    
    def get_tax_authority(self, tax_authority_id:str):
        """Get the details of a tax authority.

        Args:
            tax_authority_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/taxauthorities/{tax_authority_id}', 'get')

    def delete_tax_authority(self, tax_authority_id:str):
        """Delete a tax authority.

        Args:
            tax_authority_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/taxauthorities/{tax_authority_id}', 'delete')

    @strict_types
    def create_tax_exemptio(self, data:dict):
        """Create a tax exemption.

        Args:
            data (dict): {
                description(str)
                type(str): Type of the tax exemption. Allowed Values "customer" or "item".
            }

        """
        return self.base.api._standard_call(f'{self.module}/taxexemptions', 'post', data=data)
    
    def get_all_tax_exemption(self):
        """List of tax exemptions.
        """ 
        return self.base.api._standard_call(f'{self.module}/taxexemptions', 'get')
    
    @strict_types
    def update_tax_exemption(self, tax_exemption_id:str, data:dict):
        """Update the details of a tax exemption.

        Args:
            tax_exemption_id (str)
            data (dict): {
                description(str)
                type(str): Type of the tax exemption. Allowed Values "customer" or "item".
            }
        """
        return self.base.api._standard_call(f'{self.module}/taxexemptions/{tax_exemption_id}', 'put', data=data)
   
    def get_tax_exemption(self, tax_exemption_id:str):
        """Get the details of a tax exemption..

        Args:
            tax_exemption_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/taxexemptions/{tax_exemption_id}', 'get')

    def delete_tax_authority(self, tax_exemption_id:str):
        """Delete a tax exemption.

        Args:
            tax_exemption_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/taxexemptions/{tax_exemption_id}', 'delete')
