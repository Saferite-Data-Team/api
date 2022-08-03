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
    

    def create(self, data:BillsData, attachment:bytes):
        """Create a bill received from your vendor.

        Args:
            attachments(bytes)
            data(BillsData)
        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'post', data=data.json, attachment= attachment)

    
    def get_all(self, page:int=1,bill_number:str= None, reference_number:str= None, vendor_name:str=None, total:str=None, vendor_id:str=None, item_id:str=None,status:str=None,\
         purchase_order_id:str=None, description:str=None,recurring_bill_id:str=None, last_modified_time:str= None, date:str=None, filter_by:str=None, search_text:str=None, sort_column:str= None):
        """List all bills with pagination.

        Args:
            page (int, optional): Defaults to 1.
            bill_number(str): Search bills by bill number. 
            reference_number(str): Search bills by reference_number 
            vendor_name(str): Search bills by vendor name.
            total(str): Search bills by bill total
            vendor_id(str): Search bills by Vendor ID
            recurring_bill_id(str): Search bills by Recurring Bill ID
            item_id(str): Search bills by Item ID
            status(str): Search bills by bill status. 
            purchase_order_id(str): Search bills by Purchase Order ID
            description(str):Search bills by description. 
            search_text(str): Search bills by bill number or reference number or vendor name.
            last_modified_time(str): Search bills by Purchase Order ID
            date(str): Search bills by bill date. 
            filter_by(str): Filter bills by any status.Allowed Values: "Status.All", "Status.PartiallyPaid", "Status.Paid", "Status.Overdue", "Status.Void" and "Status.Open".
            sort_column(str): Sort bills. Allowed Values: "vendor_name", "bill_number", "date", "due_date", "total", "balance" and "created_time".

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'get', page=page, bill_number=bill_number, reference=reference_number, vendor_name=vendor_name,total=total, vendor_id=vendor_id,\
            item_id=item_id, status=status, purchase_order_id=purchase_order_id, description=description, recurring_bill_id=recurring_bill_id, last_modified_time=last_modified_time, date=date, filter_by=filter_by,search_text=search_text,\
                sort_column=sort_column)

    @strict_types
    def update(self, bill_id: str, data:BillsData, attachment:bytes=None):
        """Update a bill. To delete a line item just remove it from the line_items list.

        Args:
            bill_id (str)
            data(SOData)
            attachment(bytes): File to attach. Allowed Extensions: gif, png, jpeg, jpg, bmp and pdf.

        Returns:
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}', 'put', data=str(data.json), attachment=attachment)

    def get_by_id(self, bill_id: str):
        """Get the details of a bill.

        Args:
            bill_id (str)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}', 'get')

    def delete(self, bill_id:str):
        """Delete an existing bill. Bills which have payments applied cannot be deleted.

        Args:
           bill_id(str)

        Returns: 
            Response

        """
        bill =  self.get_by_id(bill_id)
        # if len(bill['bill']['payments']):   #chechk it out if will be for len(payments) or another property
        #     raise Exception("Bills which have payments applied cannot be deleted.")

        return self.base.api._standard_call(f'{self.module}/{bill_id}', 'delete')
   
    def mark_as_void(self, bill_id:str):
        """Mark a bill status as Void.

        Args:
            bill_id (str)
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/status/void', 'post')

    def mark_as_open(self, bill_id:str):
        """Mark a void bill as open.

        Args:
            bill_id (str)
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/status/open', 'post')


    def submit_for_approval(self, bill_id:str):
        """Submit a bill for approval.
        Args:
            bill_id (str)
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/submit', 'post')

    def approve(self, bill_id:str):
        """Approve a bill.

        Args:
            bill_id (str): _description_
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/approve', 'post')


    @strict_types
    def update_billing_address(self,bill_id:str, data:dict):
        """Updates the billing address for this bill

        Args:
            bill_id:str
            data (dict): {
                "address": "4900 Hopyard Rd, Suite 310",
                "city": "Pleasanton",
                "state": "CA",
                "zip": 94588,
                "country": "USA",
                "fax": "+1-925-924-9600"
                "attention": "string",
               "is_update_customer": false
            }
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/address/billing','put', data=data)

    def get_all_payments(self, bill_id:str):
        """Get the list of payments made for a bill.

        Args:
            bill_id (str)
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/payments', 'get')

    def apply_credits(self, bill_id:str, data:dict):
        """Apply the vendor credits from excess vendor payments to a bill. Multiple credits can be applied at once.

        Args:
            bill_id (str)
            data (dict) = {
                "bill_payments": [
                    {
                        "payment_id": "460000000042059",
                        "amount_applied": 31.25
                    }
                ],
                "apply_vendor_credits": [
                    {
                        "vendor_credit_id": "4600000053221",
                        "amount_applied": 31.25
                    }
                ]
            }

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/credits','post', data =data)

    def delete_payment(self, bill_id:str, bill_payment_id:str):
        """Delete a payment made to a bill.

        Args:
            bill_id (str)
            bill_payment_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call('{self.module}/{bill_id}/payments/{bill_payment_id}','delete')

    def add_attachment( self, bill_id:str, attachment:bytes=None) :

        """Attach a file to a bill

        Args:
            bill_id(str)
            attchment(bytes) 
            

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{bill_id}/attachment','post', attachment=attachment)

    def get_bill_attachment(self, bill_id:str):
        """Returns the file attached to the bill.

        Args:
            bill_id (str)
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/attachment','get')

    def delete_attachment(self, bill_id:str):
        """Delete the file attached to a bill.

        Args:
            bill_id (str)
        
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/attachment','delete')

    def add_comments( self, bill_id:str, data:dict) :
        """Add a comment for a bill.

        Args:
            bill_id(str)
            data(dict): {
                "description": "string",
            }

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{bill_id}/comments','post', data=data) 

    def get_history_and_comments( self, bill_id:str):
        """Get the complete history and comments of a bill.

        Args:
            bill_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{bill_id}/comments','get')

    
    def delete_comments( self, bill_id:str, comment_id:str) :
        """Delete a comment for a bill.

        Args:
            bill_id(str)
            comment_id(str)
           
        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{bill_id}/comments/{comment_id}','delete') 