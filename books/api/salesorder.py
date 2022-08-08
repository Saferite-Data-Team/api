from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import SOData, AddressData

@dataclass
class SalesOrder:
    token:str
    organization_id:str
    
    def __post_init__(self):
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module = 'salesorders'
    
    
    def get_by_id(self, order_id: str):
        """Get the details of a sales order.

        Args:
            order_id (str)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{order_id}', 'get')
    
    @strict_types
    def create(self, data: SOData):
        """Create a sales order for your customer.

        Args:
            data (dict): customer_id is required

        Returns:
            Response
        """
        return self.base.api._standard_call(self.module, 'post', data=str(data.json))
    
    def get_all(self, page: int=1):
        return self.base.api._standard_call(self.module, 'get', page=page)
    
    @strict_types
    def update(self, order_id:str, data:SOData):
        return self.base.api._standard_call(f'{self.module}/{order_id}', 'put', data=str(data.json))
    
    def delete(self, order_id:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}', 'delete')
    
    def mark_as_void(self, order_id:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}/status/void', 'post')
    
    
    def send_email(self, order_id:str, data: dict):
        """Email a sales order to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.

        Args:
            order_id (str): _description_
            data (dict): {
                "from_address_id": "johnRoberts@safInstrument.com",
                "send_from_org_email_id": true,
                "to_mail_ids": [
                    "john@safInstruments.com"
                        ],
                "cc_mail_ids": [
                    "smith@safInstruments.com"
                ],
                "bcc_mail_ids": [
                    "mark@safInstruments.com"
                ],
                "subject": "Sales Order from Zillium Inc (Sales Order #: SO-00001)",
                "documents": "string",
                "invoice_id": 460000000028192,
                "body": "<br>Dear SAF Instruments Inc,&nbsp;<br><br>Thanks for your interest in our services. Please find our sales order attached with this mail.<br><br> An overview of the sales order is available below for your reference: &nbsp;<br><br> ----------------------------------------------------------------------------------------<br> <h2>Sales Order&nbsp;# :&nbsp;SO-00001</h2><br> ----------------------------------------------------------------------------------------<br> <b>&nbsp;Order Date &nbsp; &nbsp;&nbsp;&nbsp;: &nbsp;28 Jul 2014</b><br><b>&nbsp;Amount &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp;&nbsp;$12,400.00</b><br>----------------------------------------------------------------------------------------<br><br><span>Assuring you of our best services at all times.</span><br><br><br>Regards,<br><br>John<br>Zillium Inc<br><br><br>"
            }

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{order_id}/email', 'post', data=data)
    
    def email_content(self, order_id:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}/email', 'get')

    @strict_types
    def update_billing_address(self, order_id:str, data:AddressData):
        """Updates the billing address for the actual sales order.

        Args:
            order_id (str)
            data (dict):
            {
                "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
                "city": "Beijing",
                "state": "Beijing",
                "zip": "1000881",
                "country": "China",
                "phone": "(555) 555-1234",
                "fax": "+86-10-82637827",
                "attention": "string",
                "is_one_off_address": true,
                "is_update_customer": false,
                "is_verified": true
            }
        """
        return self.base.api._standard_call(f'{self.module}/{order_id}/address/billing', 'put', data=str(data.json))

    @strict_types
    def update_shipping_address(self, order_id:str, data:AddressData):
        """Updates the shipping address for the actual sales order.

        Args:
            order_id (str)
            data (dict):
            {
                "address": "B-1104, 11F, \nHorizon International Tower, \nNo. 6, ZhiChun Road, HaiDian District",
                "city": "Beijing",
                "state": "Beijing",
                "zip": "1000881",
                "country": "China",
                "phone": "(555) 555-1234",
                "fax": "+86-10-82637827",
                "attention": "string",
                "is_one_off_address": true,
                "is_update_customer": false,
                "is_verified": true
            }
        """
        return self.base.api._standard_call(f'{self.module}/{order_id}/address/shipping', 'put', data= str(data.json))

    def template_list(self):
        """Get all sales order templates ids
        """
        return self.base.api._standard_call(f'{self.module}/templates', 'get')
    
    def update_template(self, order_id:str, template_id:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}/templates/{template_id}', 'put')
    
    @strict_types
    def add_attachment(self, order_id:str, attachment:bytes, document_ids:str, can_send_in_email:bool):
        return self.base.api._standard_call(
            f'{self.module}/{order_id}/attachment',
            'post',
            attachment=attachment,
            document_ids=document_ids,
            can_send_in_email=can_send_in_email
            )
    
    @strict_types
    def update_attachment_preference(self, order_id:str, can_send_in_email:bool):
        return self.base.api._standard_call(f'{self.module}/{order_id}/attachment', 'put', can_send_in_email=can_send_in_email)
    
    def get_attachment(self, order_id:str):
        """Returns the file attached to the sales order.

        Args:
            order_id (str)

        Returns:
            File attached (bytes)
        """
        return self.base.api._standard_call(f'{self.module}/{order_id}/attachment', 'get')
    
    def delete_attachment(self, order_id:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}/attachment', 'delete')

    def add_comment(self, order_id:str, comment:str):
        data = {'description': comment}
        return self.base.api._standard_call(f'{self.module}/{order_id}/comments', 'post', data=str(data))
    
    def get_all_comments(self, order_id:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}/comments', 'get')

    def update_comment(self, order_id:str, comment_id:str, comment:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}/comments/{comment_id}', 'put', description=comment)
    
    def delete_comment(self, order_id:str, comment_id:str):
        return self.base.api._standard_call(f'{self.module}/{order_id}/comments/{comment_id}', 'delete')

    

    


    
