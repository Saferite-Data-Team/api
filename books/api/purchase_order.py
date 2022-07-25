from dataclasses import dataclass

from requests import FileModeWarning
from saferite.core import ZohoBooksBase, strict_types
from books.data import SOData, AddressData

@dataclass
class PurchaseOrder:
    token:str
    organization_id:str
    
    def __post_init__(self):
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module = 'purchaseorders'
    
    def create(self, data:SOData, attachment:bytes=None, ignore_auto_number_generation:bool=None):
        """Create a purchase order for your vendor.

        Args:
            data (SOData)
            ignore_auto_number_generation(bool)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'post', data=data, ignore_auto_number_generation= ignore_auto_number_generation)
    
    def get_all(self,purchaseorder_number:str= None, reference_number:str= None, total:str=None, item_id:str=None,status:str=None,vendor_name:str=None,last_modified_time:str=None,\
        item_description:str=None, custom_field:str=None, expiry_date:str= None, search_text:str=None, filter_by:str=None, sort_column:str= None):
        """List all purchase orders.

        Args:
            purchaseorder_number(str):Search purchase order by purchase order number. Variants: purchaseorder_number.startswith and purchaseorder_number.contains
            reference_number(str)Search purchase order by reference number.
            customer_name(str): Search estimates by customer name.Variants customer_name_startswith and customer_name_contains
            total(str): Search purchase order by purchase order total.
            item_id(str): Search purchase order by item id.
            status(str): Search purchase order by purchase order status. Allowed Values: "draft", "open", "billed" and "cancelled".
            item_description(str):Search purchase order by purchase order item description.
            vendor_name(str): Search purchase order by vendor name. 
            last_modified_time(str): Search purchase order by last modified time.
            custom_field(str):Search purchase order by purchase order’s custom field. 
            expiry_date(str):The date of expiration of the estimates
            filter_by(str):Filter purchase order by any status. Allowed Values: "Status.All", "Status.Draft", "Status.Open", "Status.Billed" and "Status.Cancelled".
            search_text(str):Search purchase order by purchase order number or reference number or vendor name.
            sort_column(str):Sort purchase orders. Allowed Values: "vendor_name", "purchaseorder_number"," date", "delivery_date", "total" and "created_time".

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'get', estim=purchaseorder_number, refe=reference_number ,tota=total, item_id=item_id,\
            status=status,vendor_name=vendor_name, item_description=item_description, custom_field=custom_field, expiry_date=expiry_date, filter_by=filter_by, search_text=search_text,\
                sort_column=sort_column)
    
    @strict_types
    def update(self, purchaseorder_id: str, data:SOData, ignore_auto_number_generation:bool=None):
        """Update an existing purchase order.
        Args:
            purchaseorder_id (str)
            data(SOData)
            ignore_auto_number_generation(bool)

        Returns:
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}', 'put', data=data, ignore_auto_number_generation=ignore_auto_number_generation)

    def get_by_id(self, purchaseorder_id: str, print:bool=None, accept:str=None):
        """Get the details of a purchase order.
        Args:
            purchaseorder_id (str) 
            print (bool): Print the exported pdf
            accept (str:Get the details of a particular purchase order in formats such as json/ pdf/ html. Default format is json. Allowed Values: json, pdf and html.

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}', 'get', print=print, accept=accept)

    def delete(self, purchaseorder_id:str):
        """Delete an existing purchase order.

        Args:
            purchaseorder_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}', 'delete')
        
    def mark_as_open(self, purchaseorder_id:str):
        """Mark a draft purchase order as open.

        Args:
            purchaseorder_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/status/open', 'post')

    def mark_as_billed(self, purchaseorder_id:str):
        """Mark a purchase order as billed.

        Args:
            purchaseorder_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/status/billed', 'post')
    
    def cancel( self, purchaseorder_id:str):
        """Mark a purchase order as cancelled.
        
        Args:
            purchaseorder_id (str): 
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/cancelled', 'post')

    def submit_for_approval(self, purchaseorder_id:str):
        """SSubmit a purchase order for approval.

        Args:
            purchaseorder_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/submit', 'post')

    def approve(self, purchaseorder_id:str):
        """Mark a purchase order as cancelled.

        Args:
            purchaseorder_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/approve', 'post')

    def send_email(self, purchaseorder_id:str, data:dict, attachments:bytes=None, send_attachment:bool=None, file_name:str=None):
        """Email a purchase order to the vendor.

        Args:
            purchaseorder_id(str)
            data (dict):{
                "send_from_org_email_id": true,
                "from_address_id": "460000008392548",
                "to_mail_ids": [
                    "willsmith@bowmanfurniture.com"
                ],
                "cc_mail_ids": [
                    "peterparker@bowmanfurniture.com"
                ],
                "bcc_mail_ids": [
                    "mark@safInstruments.com"
                ],
                "subject": "Purchase Order from Zillium Inc (PO #: PO-00001)",
                "body": "Dear Bowman and Co, <br><br>The purchase order (PO-00001) is attached with this email. <br><br>An overview of the purchase order is available below: <br>Purchase Order # : PO-00001 <br>Date : 10 Feb 2014 <br>Amount : $112.00(in USD) <br><br>Please go through it and confirm the order. We look forward to working with you again<br><br><br><br>Regards<br><br>Zillium Inc<br><br>",
                "mail_documents": [
                    {
                        "document_id": 0,
                        "file_name": "string"
                    }
                ]
            }           
            attachments(bytes)
            send_ttachment(bool):Send the purchase order attachment a with the email.
            file_name(str)


        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/email','post', data=data, attachments=attachments, send_attachment=send_attachment, file_name=file_name)

    def get_email_content(self, purchaseorder_id:str, email_template_id):
        """Get the email content of a purchase order.

        Args:
            purchaseorder_id(str)
            email_template_id(str) :Get the email content based on a specific email template.

        Returns: 
            Response
            
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/email','get')
 
    @strict_types
    def update_billing_address(self, purchaseorder_id:str, data:AddressData):
        """Updates the billing address for this purchase order alone.

        Args:
            purchaseorder_id(str)
            data(AddressData)
                

        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/address/billing','put', data=data)

    def get_all_templates(self):

        """Get all purchase order pdf templates.

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/templates','get')

    def update_template(self, purchaseorder_id:str, template_id:str):
        """Update the pdf template associated with the purchase order.

        Args:
            purchaseorder_id(str)
            template_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/templates/{template_id}', 'get')

    def add_attachment( self, purchaseorder_id:str, attchment:bytes=None) :

        """Attach a file to a purchase order.

        Args:
           purchaseorder_id(str)
            attchment(bytes) 
            

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/attachment','post', attchment=attchment)
   
    def update_attachment_preference(self,purchaseorder_id:str, can_send_in_email:bool):

        """Set whether you want to send the attached file while emailing the purchase order.

        Args:
            purchaseorder_id(str)
            can_send_in_mail(bool)


        Returns: 
            Response
        """
        
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/attachment','put',can_send_in_email=can_send_in_email)
    
    def get_purchaseorder_attachment(self, purchaseorder_id:str, preview:bytes=None):
        """Returns the file attached to the purchase order.

        Args:
            purchaseorder_id(str)
            preview(bytes):Get the thumbnail of the attachment.

        Returns: 
            Response
        """
        
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/attachment','get',preview=preview)

    def delete_attachment(self, purchaseorder_id:str):
        """Delete the file attached to the purchase order.

        Args:
            invoice_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/attachment','delete')

    def add_comments( self, purchaseorder_id:str, data:dict) :

        """Add a comment for a purchase order.

        Args:
            purchaseorder_id(str)
            data(dict): {
                "description": "string",
                "expected_delivery_date": "string"
            }

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/comments','post',data=data) 

    def get_history_and_comments( self, purchaseorder_id:str):
        """Get the complete history and comments of purchase order.

        Args:
            purchaseorder_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/comments','get')

    def update_comment(self, purchaseorder_id:str, data:dict, comment_id:str):
        """Update an existing comment of a purchase order.

        Args:
        purchaseorder_id(str)
        comment_id(str)
        data(dict):{
            "description": "string",
            "expected_delivery_date": "string"
        }
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/comments/{comment_id}','put', data=data)
    
    def delete_comment(self, purchaseorder_id:str, comment_id:str):
        """Delete a purchase order comment.

        Args:
            purchaseorder_id(str)
            comment_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{purchaseorder_id}/comments/{comment_id}','delete')



         



