from dataclasses import dataclass
from saferite.core import ZohoBooksBase, strict_types
from books.data import SOData


@dataclass
class CreditsNotes:
    token:str
    organization_id:str

    def __post_init__(self):
        self.base = ZohoBooksBase(self.token,self.organization_id)
        self.module: str = "creditnotes"

    @strict_types
    def create(self,data, invoice_id:str=None, ignore_auto_number_generation:bool=None):
        """Create a Credit

        Args:
            data (_type_): _description_
            invoice_id (str): Invoice ID of the required invoice.
            ignore_auto_number_generation (bool): Set to true if you need to provide your own credit note number.
        """
        return self.base.api._standard_call(f'{self.module}', 'post', data=data, ignore_auto_number_generation=ignore_auto_number_generation,\
            invoice_id=invoice_id ) 
            
    def get_all(self, creditnote_number:str=None, date:str=None, status:str=None, total:str=None, reference_numnber:str=None, customer_name:str=None, item_name:str=None,\
        customer_id:str=None,item_drescription:str=None, item_id:str=None, line_item_id:str=None, tax_id:str=None, filter_by:str=None, search_text:str=None, sort_column:str=None):
        """_summary_

        Args:
            creditnote_number (str): Unique number generated (starts with CN) which will be displayed in the interface and credit notes. Max-Length [100].
            date (str):The date on which credit note is raised. Format [yyyy-mm-dd]status
            status (str: Status of the credit note. This can be "open", "closed" or "void".
            total (str): Total credits raised in this credit note.
            reference_numnber (str): Reference number generated for the payment. A string of your choice can also be used as the reference number. Max-Length [100]
            customer_name (str): Name of the customer to whom the credit note is raised. Max-Length [100]
            item_name (str): Search credit notes by item name.Max_lenght [100]
            customer_id(str):Customer ID of the customer for whom the credit note is raised.
            item_drescription (str):description for the item. Max-length [100]
            item_id (str):Unique string generated for the item to which a refund is to be made.
            line_item_id (str):Search credit notes by credit note line item id.
            tax_id (str): Unique to denote the tax associate to the creditnote
            filter_by (str): Filter credit notes by statuses. Allowed values "Status.All", "Status.Open", "Status.Draft", "Status.Closed", "Status.Void".
            search_text (str): Search credit notes by credit note number or customer name or credit note reference number. Max-length [100]
            sort_column (str): Sort credit notes by following columns customer_name, creditnote_number, balance, total, date and created_time. Allowed Values "customer_name","creditnote_number", "balance total", "date and created_time"
        """
        return self.base.api._standard_call(f'{self.module}','get',creditnote_number=creditnote_number, date=date, status=status, total=total, reference_numnber=reference_numnber, customer_name=customer_name,\
         item_name=item_name, customer_id=customer_id, item_drescription=item_drescription, item_id=item_id, line_item_id=line_item_id, tax_id=tax_id, filter_by=filter_by,search_text=search_text,sort_column=sort_column)

    @strict_types
    def update(self, creditnote_id:str, data:SOData,ignore_auto_number_generation:bool=None):
        """Update a Credit Note 

        Args:
            ignore_auto_number_generation (bool): Set to true if you need to provide your own credit note number.
        
        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}', 'put', data=data, ignore_auto_number_generation= ignore_auto_number_generation)

    def get_by_id(self, creditnote_id:str, print:bool=None, accept:str=None):
        """Get details of an existing creditnote.

        Args:
        creditnote_id(str)
            print (bool): Export credit note pdf with default print option. 
            accept (): You can get credit note details as json/pdf/html. Default format is html. 
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}', 'get', print=print, accept=accept)

    def delete(self,creditnote_id:str=None):
        """Delete an existing credit note.

        Args:
            seld (_type_)
            credit (_type_)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}', 'delete')

    def send_email(self, data:dict, customer_id=None, attchments=None, creditnote_id:str=None):
        """Email a credit note.

        Args:
            data (dict): {
                "to_mail_ids": [
                    "benjamin.george@bowmanfurniture.com",
                    "paul@bowmanfurniture.com"
                ],
                "cc_mail_ids": [
                    "accounts@bowmanfurniture.com"
                ],
                "subject": "Credit note for subscription.",
                "body": "Please find attached the credit note for your subscription."
            }
            customer_id (_type_)
            attchments (_type_)
            creditnote_id(str)
        """

        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/email', 'post', customer_id=customer_id, attchments=attchments)

    def get_email_content(self, creditnote_id:str, email_templated_id=None):
        """Get email content of a credit note.

        Args:
            email_templated_id (_type_): Get the email content based on a specific email template. If this param is not inputted, then the content will 
                be based on the email template associated with the customer. If no template is associated with the customer, then default template will be used.
            creditnote_id(str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/email', 'get', email_templated_id=email_templated_id)

    def mark_as_void(self, creditnote_id:str):
        """Mark the credit note as Void.

        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/status/void', 'post')
    
    def convert_to_draft(self, creditnote_id:str):
        """Convert a voided credit note to Draft.

        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/status/draft', 'post')
            
    def convert_to_open(self, creditnote_id:str):
        """Convert a credit note in Draft status to Open.

        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/status/open', 'post')

    def submit_for_approval(self, creditnote_id:str):
        """Submit an estimate for approval.
        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/submit', 'post')

    def approve(self, creditnote_id:str):
        """Approve a credit note.

        Args:
            creditnote_id (str): _description_
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/approve', 'post')

    def get_email_history(self,creditnote_id:str):
        """Get email history of a credit note.

        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/emailhistory', 'get')

    @strict_types
    def update_billing_address(self,creditnote_id:str, data:dict):
        """Updates the billing address for an existing credit note alone.

        Args:
            creditnote_id:str
            data (dict): {
                "address": "4900 Hopyard Rd, Suite 310",
                "city": "Pleasanton",
                "state": "CA",
                "zip": 94588,
                "country": "USA",
                "fax": "+1-925-924-9600"
            }
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/address/billing','put', data=data)

    @strict_types
    def update_shipping_address(self, creditnote_id:str, data:dict):
        """Updates the shipping address for an existing credit note alone.

        Args:
            creditnote_id (str)
            data (dict):{
                "address": "Suite 125, McMillan Avenue",
                "city": "San Francisco",
                "state": "CA",
                "zip": 94134,
                "country": "USA",
                "fax": "+1-925-924-9600"
            }
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/address/shipping','put', data=data)

    def get_all_templates(self):
        """Get all credit note pdf templates.

        """
        return self.base.api._standard_call(f'{self.module}/templates','get')

    def update_template(self, creditnote_id:str, template_id:str):
        """Update the pdf template associated with the credit note.

        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/templates/{template_id}','put')

    def apply_to_an_invoice(self,creditnote_id:str, data:dict):
        """Apply credit note to existing invoices.

        Args:
            creditnote_id (str)
            data (dict) = {
                "invoices": [
                    {
                        "invoice_id": "90300000079426",
                        "amount_applied": 41.82
                    }
                ],
                "invoice_id": "90300000079426",
                "amount_applied": 41.82
            }
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/invoices','post')

    def get_invoices_credited(self,creditnote_id:str):
        """List invoices to which the credit note is applied.

        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/invoices','post')

    def delete_invoices_credited(self, creditnote_id:str, creditnote_invoice_id:str) :
        """Delete the credits applied to an invoice.

        Args:
            creditnote_id (str)
            creditnote_invoice_id(str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/invoices{creditnote_invoice_id}','delete')

    def add_comments( self, creditnote_id:str, data:dict) :

        """Add a comment to an existing credit note.

        Args:
            creditnote_id(str)
            data(dict) = {
                "description": "Credits applied to invoice INV-00004"
            }
        
        """

        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/comments','post',data=data) 

    def get_history_and_comments( self, creditnote_id:str):
        """Get history and comments of a credit note.

        Args:
            creditnote_id(str)

        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/comments','get')
    
    def delete_comment(self, creditnote_id:str, comment_id:str):
        """Delete a credit note comment.

        Args:
            creditnote_id(str)
            comment_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/comments/{comment_id}','delete')

    def get_all_note_refunds(self, customer_id:str, sort_column:str=None):
        """List all refunds with pagination.

        Args:
            customer_id (str)
        sort_column (str)=
            "refund_mode" or "reference_number"or "date" or "creditnote_number" or "customer_name" or "amount_bcy and amount_fcy"
        """
        return self.base.api._standard_call(f'{self.module}/refunds','get',customer_id= customer_id, sort_column=sort_column)

    def refund_credinote(self, creditnote_id:str, data:dict):
        """Refund credit note amount.

        Args:
            creditnote_id (str)
            data (dict) = {
                "date": "2016-06-05",
                "refund_mode": "cash",
                "reference_number": "INV-384",
                "amount": 450,
                "exchange_rate": "5.5",
                "from_account_id": " ",
                "description": "prorated amount for items"
            }
                    """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/refunds','post')

    def get_all_refunds_of_existing_creditnote(self, creditnote_id:str):
        """List all refunds of an existing credit note.

        Args:
            creditnote_id (str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/refunds','get')

    def update_creditnote_refund( self, creditnote_id:str, data:dict,creditnote_refund_id:str):
        """Update the refunded transaction.

        Args:
            creditnote_id (str)
            data (dict) = {
                "date": "2016-06-05",
                "refund_mode": "cash",
                "reference_number": "INV-384",
                "amount": 450,
                "exchange_rate": "5.5",
                "from_account_id": " ",
                "description": "prorated amount for items"
            }
            creditnote_refund_id(str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/refunds/{creditnote_refund_id}','put')

    def get_creditnote_refund( self, creditnote_id:str, creditnote_refund_id:str):
        """Get refund of a particular credit note.

        Args:
            creditnote_id (str)
            creditnote_refund_id(str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/refunds/{creditnote_refund_id}','get')

    def delete_creditnote_refund( self, creditnote_id:str, creditnote_refund_id:str):
        """Delete a credit note refund.
        Args:
            creditnote_id (str)
            creditnote_refund_id(str)
        """
        return self.base.api._standard_call(f'{self.module}/{creditnote_id}/refunds/{creditnote_refund_id}','delete')





       






        











       