from dataclasses import dataclass

from books.data import AddressData, ItemData, SOData
from saferite.core import ZohoBooksBase, strict_types


@dataclass
class Invoice:
    token:str
    organization_id:str

    def __post_init__(self) -> None:
        self.base = ZohoBooksBase(self.token, self.organization_id)
        self.module = 'invoices'

    @strict_types
    def create (self, data:dict, send:bool, ignore_auto_generation:bool=None):
        """Create an invoice for your customer.

        Args:
            data (dict)
            send(bool)
            ignore_auto_generation(bool)

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'post', json_data=data, send=send, ignore_auto_generation=ignore_auto_generation)
    
    def get_by_id(self, invoice_id:str):
        """Get the details of an invoice.

        Args:
            invoice_id (str)

        Returns:
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}', 'get')

    def get_all(self, page:int=1, invoice_number:str= None, reference_number:str= None, customer_name:str=None, total:str=None, customer_id:str=None, item_id:str=None,status:str=None,\
            item_name:str=None, item_description:str=None, custom_field:str=None, due_date:str= None, date:str=None, filter_by:str=None, search_text:str=None, sort_column:str= None, last_modified_time:str=None, balance:str = None, \
                email:str=None, recurring_invoice_id:str=None,**kwargs ):
        """List all invoices with pagination.

        Args:
            page (int): Defaults to 1.
            invoice_number (str): Search invoices by invoice number.
            reference_number (str): Search invoices by item description.
            customer_name (str):The name of the customer. Max-length [100]
            total (str):The total amount to be paid
            customer_id (str): ID of the customer the invoice has to be created.
            item_id (str): Search invoices by item id.
            status (str: Search invoices by invoice status.Allowed Values: "sent", "draft", "overdue", "paid", "void", "unpaid", "partially_paid" "and viewed".
            item_name(str):Search invoices by item name.
            item_description (str): Search invoices by item description.
            custom_field (str):Search invoices by custom fields
            due_date (str,): Search invoices by due date. Default date format is yyyy-mm-dd. 
            date (str,): Search invoices by invoice date. Default date format is yyyy-mm-dd.
            filter_by (str: Filter invoices by any status or payment expected date.Allowed Values: "Status.All", "Status.Sent", "Status.Draft", "Status.OverDue", "Status.Paid", "Status.Void", "Status.Unpaid", "Status.PartiallyPaid", "Status.Viewed" and "Date.PaymentExpectedDate".
            search_text (str): Search invoices by invoice number or purchase order or customer name. Max-length [100]
            sort_column (str): Sort invoices.Allowed Values: "customer_name", "invoice_number", "date", "due_date", "total", "balance" and "created_time".
            last_modified_time (str): Default date format is yyyy-mm-dd.
            balance (str): The unpaid amount
            email(str):ID of the recurring invoice from which the invoice is created.
            recurring_invoice_id (str):ID of the recurring invoice from which the invoice is created..

        Returns:
            Response
        """
        return self.base.api._standard_call(f'{self.module}', 'get', page=page, invoice_number=invoice_number, reference_number=reference_number, customer_name=customer_name, total=total,\
            customer_id=customer_id, item_id=item_id, status=status,item_name=item_name, item_description=item_description, custom_field=custom_field, due_date=due_date, datre=date, filter_by=filter_by,\
                search_text=search_text, sort_column=sort_column, last_modified_time=last_modified_time, balance=balance, email=email, recurring_invoice_id=recurring_invoice_id, ** kwargs)
    
    def get_all_complete(self, invoice_number:str= None, reference_number:str= None, customer_name:str=None, total:str=None, customer_id:str=None, item_id:str=None,status:str=None,\
            item_name:str=None, item_description:str=None, custom_field:str=None, due_date:str= None, date:str=None, filter_by:str=None, search_text:str=None, sort_column:str= None, last_modified_time:str=None, balance:str = None, \
                email:str=None, recurring_invoice_id:str=None,**kwargs ):
        """List all invoices.

        Args:
            invoice_number (str): Search invoices by invoice number.
            reference_number (str): Search invoices by item description.
            customer_name (str):The name of the customer. Max-length [100]
            total (str):The total amount to be paid
            customer_id (str): ID of the customer the invoice has to be created.
            item_id (str): Search invoices by item id.
            status (str: Search invoices by invoice status.Allowed Values: "sent", "draft", "overdue", "paid", "void", "unpaid", "partially_paid" "and viewed".
            item_name(str):Search invoices by item name.
            item_description (str): Search invoices by item description.
            custom_field (str):Search invoices by custom fields
            due_date (str,): Search invoices by due date. Default date format is yyyy-mm-dd. 
            date (str,): Search invoices by invoice date. Default date format is yyyy-mm-dd.
            filter_by (str: Filter invoices by any status or payment expected date.Allowed Values: "Status.All", "Status.Sent", "Status.Draft", "Status.OverDue", "Status.Paid", "Status.Void", "Status.Unpaid", "Status.PartiallyPaid", "Status.Viewed" and "Date.PaymentExpectedDate".
            search_text (str): Search invoices by invoice number or purchase order or customer name. Max-length [100]
            sort_column (str): Sort invoices.Allowed Values: "customer_name", "invoice_number", "date", "due_date", "total", "balance" and "created_time".
            last_modified_time (str): Default date format is yyyy-mm-dd.
            balance (str): The unpaid amount
            email(str):ID of the recurring invoice from which the invoice is created.
            recurring_invoice_id (str):ID of the recurring invoice from which the invoice is created..

        Returns:
            Response
        """
        more_pages =  True
        page = 1
        all_invoices = []
        while more_pages:
            # args = {k:v for k,v in locals().items() if k!='self'}
            # invoices = self.get_all( **args)
            # invoices = self.get_all(**kwargs) 
            invoices = self.get_all(page = page, invoice_number = invoice_number, reference_number=reference_number, customer_name=customer_name , total = total, customer_id = customer_id,item_id =  item_id,status = status,\
            item_name = item_name,item_description= item_description,custom_field= custom_field,due_state = due_date,date = date,filter_by= filter_by, search_text= search_text, sort_column=sort_column, last_modified_time= last_modified_time, balance= balance, \
            email=email, recurring_invoice_id= recurring_invoice_id, **kwargs)      
            all_invoices.extend(invoices['invoices'])
            more_pages = invoices['page_context']['has_more_page']
            page += 1
        return all_invoices



    def get_all_test(self, **kwargs ):
    
        return self.base.api._standard_call(f'{self.module}', 'get',**kwargs)
    
    def get_all_complete_test(self, **kwargs ):
        more_pages =  True
        page = 1
        all_invoices = []
        while more_pages:
            invoices = self.get_all_test(page = page , **kwargs)   
            all_invoices.extend(invoices['invoices'])
            more_pages = invoices['page_context']['has_more_page']
            page += 1
        return all_invoices



    @strict_types
    def update(self, invoice_id: str, data:SOData):
        """Update an existing invoice. To delete a line item just remove it from the line_items list.

        Args:
            invoice_id (str)
            data(SOData)

        Returns:
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}', 'put', data= str(data.json))
     
    def delete(self, invoice_id:str):
        """Delete an existing invoice. Invoices which have payment or credits note applied cannot be deleted.

        Args:
            invoice__id (str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}', 'delete')
        
    def mark_as_sent(self, invoice_id:str):
        """Mark a draft invoice as sent.

        Args:
            invoice_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/status/sent', 'post')

    def mark_as_draft(self, invoice_id:str):
        """Mark a voided invoice as draft.
        Args:
            invoice_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/status/draft', 'post')

    @strict_types
    def send_email(self, invoice_id:str, data:dict, attachments:bytes=None, send_customer_statement:bool=None, send_attachments:bool=None):
        """Email an invoice to the customer. Input json string is not mandatory. If input json string is empty, mail will be send with default mail content.
        Args:
            invoice_id(str)
            data(dict):

            {
                "send_from_org_email_id": false,
                "to_mail_ids": [
                     "willsmith@bowmanfurniture.com"
                ],
                "cc_mail_ids": [
                    "peterparker@bowmanfurniture.com"
            ],
            "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
            "body": "Dear Customer,         <br><br><br><br>Thanks for your business.         <br><br><br><br>The invoice INV-00001 is attached with this email. You can choose the easy way out and <a href= https://invoice.zoho.com/SecurePayment?CInvoiceID=b9800228e011ae86abe71227bdacb3c68e1af685f647dcaed747812e0b9314635e55ac6223925675b371fcbd2d5ae3dc  >pay online for this invoice.</a>         <br><br>Here's an overview of the invoice for your reference.         <br><br><br><br>Invoice Overview:         <br><br>Invoice  : INV-00001         <br><br>Date : 05 Aug 2013         <br><br>Amount : $541.82         <br><br><br><br>It was great working with you. Looking forward to working with you again.<br><br><br>\\nRegards<br>\\nZillium Inc<br>\\n\","

            }
            send_customer_statement(bool)
            attachments(bytes)
            send_attachments(bool)


        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/email', 'post', data= str(data.json), attachments = attachments,send_customer_statement=send_customer_statement,send_attachments=send_attachments)

    def email_multiples(self, invoices_ids:str, data:dict):
        """Send invoices to your customers by email. Maximum of 10 invoices can be sent at once.

        Args:
            invoices_ids(str)
            data:
            {
                "contacts": [
                    "string"
                ],
                "contact_id": 460000000026049
            }

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/email', 'post', data=data, invoices_ids=invoices_ids)

    def submit_for_approval(self, invoice_id:str):
        """Submit an invoice for approval.
        Args:
            invoice_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/submit', 'post')

    def approve_invoice(self, invoice_id:str):
        """Approve an invoice.

        Args:
           invoice_id(str)

        Returns: 
            Response

        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/approve', 'post')

    def get_email_content(self, invoice_id:str):
        """Get the email content of an invoice.

        Args:
            invoice_id(str)

        Returns: 
            Response
            
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/email','get')
    
    @strict_types
    def remind_customer( self, invoice_id:str, data:dict, send_customer_statement:bool=None, attachments:bytes=None):
        """Remind your customer about an unpaid invoice by email. Reminder will be sent, only for the invoices which are in open or overdue status.

        Args:
            invoice_id(str)
            data(dict):
            {
                "to_mail_ids": [
                      "willsmith@bowmanfurniture.com"
                ],
               "cc_mail_ids": [
                      "peterparker@bowmanfurniture.com"
                ],
                "subject": "Invoice from Zillium Inc (Invoice#: INV-00001)",
                "body": "<br>Dear Mr. Sujin,&nbsp;<br><br>You might have missed the payment date and the invoice is now overdue by&nbsp;1&nbsp;days.<br><br>----------------------------------------------------------------------------------------<br><h2>Invoice# : INV-000004 </h2>Dated : 23 Dec 2016<br>----------------------------------------------------------------------------------------<br><b>&nbsp;Due Date &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp;&nbsp;23 Dec 2016</b><br><b>&nbsp;Amount &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; : &nbsp;&nbsp;$139.65</b><br>----------------------------------------------------------------------------------------<br><br><span>Not to worry at all !&nbsp;</span>View your invoice and take the easy way out by making an&nbsp;<a href=\"https://books.zoho.com/portal/zilliuminc/index#/invoices/invoice/2000000007037 \">online payment</a>.<br><br>If you have already paid, please accept our apologies and kindly ignore this payment reminder.<br><br><br>Regards,<br><br>David Sujin<br>Zillium Inc<br><br><br>",
                 "send_from_org_email_id": false
            }
            send_customersend_customer_statement(bool) 
            attachments(bytes)
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/paymentreminder','post',data= str(data.json), send_customer_statement=send_customer_statement,attachments=attachments)

    def get_payment_reminder(self, invoice_id:str):
        """Get the mail content of the payment reminder.

        Args:
            invoice_id(str)
            
        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/paymentreminder','get')

    def bulk_invoice_reminder(self, invoice_ids:list):
        """Remind your customer about an unpaid invoices by email. Reminder mail will be send, only for the invoices is in open or overdue status. Maximum 10 invoices can be reminded at once.

         Args:
            invoice_ids(str): Array of invoice ids for which the reminder has to be sent.

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/paymentreminder','post', invoice_ids= invoice_ids)
           
    def bulk_export(self, invoice_ids:str):
        """Maximum of 25 invoices can be exported in a single pdf.

         Args:
            invoice_ids(str): Comma separated invoice ids which are to be emailed.

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/pdf','get', invoice_ids=invoice_ids)

    def bulk_print_invoices(self,invoice_ids: str):
        """Export invoices as pdf and print them. Maximum of 25 invoices can be printed.

        Args:
            invoice_ids(str): Comma separated estimate ids which are to be emailed.

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/print','get', invoice_ids=invoice_ids)

    def disable_payment_reminder(self,invoice_id:str):
        """Disable automated payment reminders for an invoice.
        Args:
            invoice_id(str) 


        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/paymentreminder','post')
    
    def enable_payment_reminder(self,invoice_id:str):
        """Enable automated payment reminders for an invoice.
        Args:
            invoice_id(str) 

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/paymentreminder','post')
    
    def write_off_invoice(self,invoice_id:str):
        """Write off the invoice balance amount of an invoice.
        Args:
            invoice_id(str) 

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/writeoff','post')
       
    def cancel_write_off(self,invoice_id:str):
        """Cancel the write off amount of an invoice.
        Args:
            invoice_id(str) 

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/writeoff','post')
    
    @strict_types
    def update_billing_address(self, invoice_id:str, data:AddressData):
        """Updates the billing address for this invoice alone.

        Args:
            invoice_id(str)
            data(AddressData)
                

        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/address/billing','put', data=data)

    @strict_types
    def update_shipping_address(self, invoice_id:str, data:AddressData):
        """Updates the shipping address for this invoice alone.

        Args:
           invoice_id(str)
           data(AddressData)
                

        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/address/shipping','put', data=str(data.json))

    def get_all_templates(self):

        """Get all invoice pdf templates.

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/templates','get')

    def update_template(self, invoice_id:str, template_id:str):
        """Update the pdf template associated with the invoice.

        Args:
           invoice_id(str)
           template_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/templates/{template_id}','put')

    def get_invoice_payments(self,invoice_id:str):
        """Get the list of payments made for an invoice.

        Args:
           invoice_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/payments','get')

    def get_credits_applied(self,invoice_id:str):
        """Get the list of credits applied for an invoice.

        Args:
           invoice_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/creditsapplied','get')

    def apply_credits(self, invoice_id:str, data:dict):
        """Apply the customer credits either from credit notes or excess customer payments to an invoice. Multiple credits can be applied at once.

        Args:
           invoice_id(str)
           data(dict):
           {
                "invoice_payments": [
                {
                     "payment_id": 982000000567190,
                    "amount_applied": 12.2
                }
            ],
            "apply_creditnotes": [
                {
                    "creditnote_id": 982000000567134,
                    "amount_applied": 12.2
                }
             ]
           }


        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/credits','post', data=data)
        
    def delete_payment(self, invoice_id:str, invoice_payment_id:str):
        """Delete a payment made to an invoice.

        Args:
            invoice_id(str)
            invoice_payment_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/payments/{invoice_payment_id}','delete')
    
    def delete_applied_credit(self, invoice_id:str, creditnotes_invoice_id:str):
        """Delete a particular credit applied to an invoice..

        Args:
            invoice_id(str)
            creditnotes_invoice_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/creditsapplied/{creditnotes_invoice_id}','delete')

    @strict_types   
    def add_attachment( self, invoice_id:str, can_send_in_email:bool=None, attachment:bytes=None) :

        """Attach a file to an invoice.

        Args:
            invoice_id(str)
            can_send_in_email(bool)
            attachment(bytes) 
            

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{invoice_id}/attachment','post', can_send_in_email=can_send_in_email, attachment=attachment)

    def update_attachment_preference(self,invoice_id:str, can_send_in_email:bool):

        """Set whether you want to send the attached file while emailing the invoice.

        Args:
            invoice_id(str)
            can_send_in_mail(bool)


        Returns: 
            Response
        """
        
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/attachment','put',can_send_in_email=can_send_in_email)

    @strict_types
    def get_invoice_attachment(self, invoice_id:str, preview:bytes=None):
        """Returns the file attached to the invoice.

        Args:
            invoice_id(str)
            preview(bytes):Get the thumbnail of the attachment.

        Returns: 
            Response
        """
        
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/attachment','get',preview=preview)

    def delete_attachment(self, invoice_id:str):
        """Delete the file attached to the invoice.

        Args:
            invoice_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/attachment','delete')

    def delete_expense_receipt(self, expense_id:str):
        """Delete the expense receipts attached to an invoice which is raised from an expense.

        Args:
            expense_id(str)
    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/expenses/{expense_id}/receipt','delete')
        
    def add_comments( self, invoice_id:str, description:str, payment_expected_date:str, show_comments_to_clients:bool=None):

        """Add a comment for an invoice.

        Args:
            invoice_id(str)
            description(str)
            payment_expected_date(str): Format [yyyy-mm-dd]status.
            show_comments_to_clients(bool): Boolean to check if the comment to be shown to the clients
           

        Returns: 
            Response
        """

        return self.base.api._standard_call(f'{self.module}/{invoice_id}/comments','post',description= description,payment_expected_date=payment_expected_date,\
             show_comments_to_clients=show_comments_to_clients) 

    def get_history_and_comments( self, invoice_id:str):
        """Get the complete history and comments of an invoice.

        Args:
            invoice_id(str)

        Returns: 
            Response
        
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/comments','get')

    def update_comment(self, invoice_id:str, comment_id:str, description:str, show_comments_to_clients:bool=None):
        """Update an existing comment of an invoice.

        Args:
        invoice_id(str)
        comment_id(str)
        description(str)
        show_comments_to_clients(bool)
        

        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/comments/{comment_id}','put', description=description,\
            show_comments_to_clients=show_comments_to_clients)
    
    def delete_comment(self, invoice_id:str, comment_id:str, data:dict):
        """Delete an invoice comment.

        Args:
            invoice_id(str)
            comment_id(str)
            data(dict):
            {
                "description": "Estimate created",
                "show_comment_to_clients": " "
            }

    
        Returns: 
            Response
        """
        return self.base.api._standard_call(f'{self.module}/{invoice_id}/comments/{comment_id}','put', data= data)



    

    


