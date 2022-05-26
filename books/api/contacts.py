from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import AddressData, ContactData

@dataclass
class Contacts:
    token:str
    organization_id:str
    
    def __post_init__(self):
        self.module = 'contacts'
        self.base = ZohoBooksBase(self.token, self.organization_id)
    
    @strict_types
    def create(self, data:ContactData):
        if not isinstance(data, ContactData):
            raise TypeError(f'Expected data to be ContactData, got {type(data)}')
        return self.base.api._standard_call(self.module, 'post', data=str(data.json))
    
    def list(self, page:int = 1):
        return self.base.api._standard_call(self.module, 'get', page=page)
    
    @strict_types
    def update(self, data:ContactData):
        return self.base.api._standard_call(self.module, 'put', data=str(data.json))
    
    def get_by_id(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}', 'get')
    
    def delete(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}', 'delete')
    
    def mark_as_active(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/active', 'post')
    
    def mark_as_inactive(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/inactive', 'post')
    
    @strict_types
    def enable_portal(self, contact_id:str, contact_persons:list):
        data = {'contact_persons': [{'contact_person_id': person} for person in contact_persons]}
        return self.base.api._standard_call(f'{self.module}/{contact_id}/portal/enable', 'post', data=data)
    
    def enable_payment_reminders(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/paymentreminder/enable', 'post')
    
    def disable_payment_reminders(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/paymentreminder/disable', 'post')
    
    @strict_types
    def email_statement(self, contact_id:str, email:dict, **kwargs):
        """Email statement to the contact. If JSONString is not inputted, mail will be sent with the default mail content.

        Args:
            contact_id (str)
            email (dict):
            
            {
                "send_from_org_email_id": true,
                "to_mail_ids": ["willsmith@bowmanfurniture.com"],
                "cc_mail_ids": ["peterparker@bowmanfurniture.com"],
                "subject": "Statement of transactions with Zillium Inc",
                "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc"
                }
        
        Query Parameters:
            start_date: 'yyyy-mm-dd'
            end_date: 'yyyy-mm-dd'
            multipart_or_formdata: Files to be attached along with the statement.
                
        """
        return self.base.api._standard_call(f'{self.module}/{contact_id}/statements/email', 'post', data=email **kwargs)
    
    def get_statement_mail_content(self, contact_id:str, **kwargs):
        """Get the statement mail content.

        Args:
            contact_id (str):
        
        Query Parameters:
            start_date: 'yyyy-mm-dd'
            end_date: 'yyyy-mm-dd'
        """
        return self.base.api._standard_call(f'{self.module}/{contact_id}/statements/email', 'get', **kwargs)

    @strict_types
    def email_contact(self, contact_id:str, email:dict, **kwargs):
        """Send email to contact.

        Args:
            contact_id (str)
            email (dict): {
                "to_mail_ids": ["willsmith@bowmanfurniture.com"],
                "subject": "Welcome to Zillium Inc .",
                "body": "Dear Customer,     <br/>We have attached with this email a list of all your transactions with us for the period 01 Sep 2013 to 30 Sep 2013. You can write to us or call us if you need any assistance or clarifications.     <br/>Thanks for your business.<br/>Regards<br/>Zillium Inc",
                "attachments": "string"
                }
        Query Parameters:
            send_customer_statement (bool?)
        
        """
        return self.base.api._standard_call(f'{self.module}/{contact_id}/email', 'post', data=email, **kwargs)
    
    def list_comments(self, contact_id:str):
        """List recent activities of a contact.

        Args:
            contact_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{contact_id}/comments', 'get')
    
    @strict_types
    def add_additional_address(self, contact_id:str, data:AddressData):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/address', 'post', data=str(data.json))
    
    def get_contact_addresses(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/address', 'get')
    
    @strict_types
    def edit_additional_address(self, contact_id:str, data:AddressData):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/address', 'put', data=str(data.json))
    
    def delete_additional_address(self, contact_id:str, address_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/address/{address_id}', 'delete')
    
    def list_refunds(self, contact_id:str):
        return self.base.api._standard_call(f'{self.module}/{contact_id}/refunds', 'get')
    
    def track_1099(self, contact_id:str):
        self.base.api._standard_call(f'{self.module}/{contact_id}/track1099', 'post')
    
    def untrack_1099(self, contact_id:str):
        self.base.api._standard_call(f'{self.module}/{contact_id}/untrack1099', 'post')
    
    