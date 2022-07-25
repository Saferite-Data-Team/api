from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import SOData, AddressData

@dataclass
class Estimates:
    token:str
    organization_id:str
    
    def __post_init__(self):
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module = 'estimates'
    
    def create(self, data:SOData, send:bool=None, ignore_auto_number_generation:bool=None):
        """Create an estimate for your customer.

        Args:
            data (SOData)
            send(bool)
            ignore_auto_number_generation(bool)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'post', data=data, send= send, ignore_auto_number_generation= ignore_auto_number_generation)
    
    def get_all(self, page:int=1,estimate_number:str= None, reference_number:str= None, customer_name:str=None, total:str=None, customer_id:str=None, item_id:str=None,status:str=None,\
         item_name:str=None, item_description:str=None, custom_field:str=None, expiry_date:str= None, date:str=None, filter_by:str=None, search_text:str=None, sort_column:str= None):
        """List all estimates with pagination.

        Args:
            page (int, optional): Defaults to 1.
            estimate_number(str):Search estimates by estimate number.
            reference_number(str):Search estimates by reference number.
            customer_name(str): Search estimates by customer name.
            total(str): arch estimates by estimate total..
            customer_id(str): Search estimates by customer id.
            item_id(str): ID of the item.
            status(str): Search estimates by status.Allowed Values "draft", "sent", "invoiced" , "accepted", "declined" and "expired".
            item_name(str): Search estimates by item name
            item_description(str):Search estimates by item description.
            custom_field(str):Search estimates by custom field.
            expiry_date(str):The date of expiration of the estimates.
            date(str):Search estimates by estimate date.Variants date_start, date_end, date_before and date_after.
            filter_by(str): Filter estimates by status.Allowed Values "Status.All", "Status.Sent", "Status.Draft", "Status.Invoiced", "Status.Accepted", "Status.Declined" and "Status.Expired".
            search_text(str): Search estimates by estimate number or reference or customer name.
            sort_column(str): Sort estimates. Allowed Values "customer_name", "estimate_number", "date", "total" and "created_time".

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'get', page=page, estim=estimate_number, refe=reference_number, customer_name=customer_name,tota=total, customer_id=customer_id,\
            item_id=item_id,status=status, item_name=item_name, item_description=item_description, custom_field=custom_field, expiry_date=expiry_date, date=date, filter_by=filter_by,search_text=search_text,\
                sort_column=sort_column)
    
    @strict_types
    def update(self, estimate_id: str, data:SOData,ignore_auto_number_generation:bool=None):
        """Update an existing estimate. To delete a line item just remove it from the line_items list.

        Args:
            estimate_id (str)
            data(SOData)
            ignore_auto_number_generation(bool)

        Returns:
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}', 'put', data=data,ignore_auto_number_generation= ignore_auto_number_generation)


    def get_by_id(self, estimate_id: str):
        """Get the details of an estimate.

        Args:
            estimate_id (str)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}', 'get')

    def delete(self, estimate_id:str):
        """Delete an existing estimate.

        Args:
            estimate_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}', 'delete')
        
    def mark_as_sent(self, estimate_id:str):
        """Mark a draft estimate as sent.

        Args:
            estimate_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/status/sent', 'post')

    def mark_as_accepted(self, estimate_id:str):
        """Mark a sent estimate as accepted if the customer has accepted it.

        Args:
            estimate_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/status/accepted', 'post')
        
    def mark_as_declined(self, estimate_id:str):
        """Mark a sent estimate as declined if the customer has rejected it.

        Args:
            estimate_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/status/declined', 'post')

    def submit_for_approval(self, estimate_id:str):
        """Submit an estimate for approval.

        Args:
            estimate_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/submit', 'post')

    def approve_estimate(self, estimate_id:str):
        """Approve an estimate.

        Args:
            estimate_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/approve', 'post')

    def send_email(self, estimate_id:str, data:dict, attachments:bytes=None):
        """Email an estimate to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.

        Args:
            estimate_id(str)
            data (dict):

            {
                "send_from_org_email_id": false,
                "to_mail_ids": [
                    "willsmith@bowmanfurniture.com"
                ],
                "cc_mail_ids": [
                    "peterparker@bowmanfurniture.com"
                ],
                "subject": "Statement of transactions with Zillium Inc",
                "body": "Dear Customer,   Thanks for your business enquiry.         The estimate EST-000002 is attached with this email.        We can get started if you send us your consent. For any assistance you can reach us via email or phone.         Looking forward to hearing back from you. Here's an overview of the estimate for your reference.        Estimate Overview:        Estimate  : EST-000002         Date : 03 Oct 2013        Amount : $36.47 Regards<br>\\nZillium Inc<br>\\n\"\""
            }
            attachments(bytes)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/email','post', data=data, attachments=attachments)

    def get_email_content(self, estimate_id:str):
        """Get the email content of an estimate.

        Args:
            estimate_id(str)

        Returns: 
            Response
            
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/email','get')

    def email_multiples(self, estimate_ids: str):
        """Send estimates to your customers by email. Maximum of 10 estimates can be sent at once.
        
        Args:
            estimate_ids(str): Comma separated estimate ids which are to be emailed.

        Returns: 
            Response
            
        """
        return self.base.api._standard_call(f'{self.module}/email','post', estimate_ids=estimate_ids)

    def bulk_export(self, estimate_ids:str):
        """Maximum of 25 estimates can be exported in a single pdf.

         Args:
            estimate_ids(str): Comma separated estimate ids which are to be emailed.

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/pdf','get', estimate_ids=estimate_ids)

    def bulk_print_estimates(self,estimate_ids: str):
        """Export estimates as pdf and print them. Maximum of 25 estimates can be printed.

        Args:
            estimate_ids(str): Comma separated estimate ids which are to be emailed.

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/print','get', estimate_ids=estimate_ids)
   
    @strict_types
    def update_billing_address(self, estimate_id:str, data:AddressData):
        """Updates the billing address for this estimate alone.

        Args:
            estimate_id(str)
            data(AddressData)
                

        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/address/billing','put', data=data)
   
    @strict_types
    def update_shipping_address(self, estimate_id:str, data:AddressData):
        """Updates the shipping address for an existing estimate alone.

        Args:
            estimate_id(str)
            data(AddressData)
                

        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/address/shipping','put', data=data)

    def get_all_templates(self):

        """Get all estimate pdf templates.

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/templates','get')

    def update_template(self, estimate_id:str, template_id:str):
        """Update the pdf template associated with the estimate.

        Args:
            estimate_id(str)
            template_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/templates/{template_id}', 'get')

    def add_comments( self, estimate_id:str, data:dict) :

        """Add a comment for an estimate

        Args:
            estimate_id(str)
            data(dict)

            {
                "description": "Estimate marked as sent",
                "show_comment_to_clients": true
                }

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{estimate_id}/comments','post',data=data) 

    def get_history_and_comments( self, estimate_id:str):
        """Get the complete history and comments of an estimate

        Args:
            estimate_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/comments','get')

    def update_comment(self, estimate_id:str, data:dict, comment_id:str):
        """Update an existing comment of an estimate.

        Args:
        estimate_id(str)
        comment_id(str)
        data(dict)
    
                {
                "description": "Estimate marked as sent",
                "show_comment_to_clients": true
                }

        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/comments/{comment_id}','put', data=data)
    
    def delete_comment(self, estimate_id:str, comment_id:str):
        """Delete an estimate comment.

        Args:
            estimate_id(str)
            comment_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{estimate_id}/comments/{comment_id}','delete')



         



