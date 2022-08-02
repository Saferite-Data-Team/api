from books.api import items, salesorder, contacts, estimates, invoice, purchase_order, credits_notes, taxes
from datetime import datetime

class Books:
    def __init__(self, token:str, organization_id:str):
        self.items = items.Items(token, organization_id)
        self.salesorder = salesorder.SalesOrder(token, organization_id)
        self.contacts = contacts.Contacts(token, organization_id)
        self.estimates = estimates.Estimates(token, organization_id)
        self.invoices = invoice.Invoice(token, organization_id)
        self.credits_notes = credits_notes.CreditsNotes(token, organization_id)
        self.purchase_order = purchase_order.PurchaseOrder(token, organization_id)
        self.taxes = taxes.Taxes(token, organization_id)


    def __repr__(self):
        now = datetime.now()
        expiration = 60 - now.minute
        return f'Zoho Books intance in 0x{id(self)}. Token will expire in {expiration} minutes'
