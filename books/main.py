from books.api import items, salesorder, contacts, estimates, invoice, purchase_order, credits_notes, taxes
from datetime import datetime
import requests

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

    @classmethod
    def refresh_token(cls, token:str, client_id:str, client_secret:str):
        redirect_uri = 'http://www.zoho.com/books'
        url = f'https://accounts.zoho.com/oauth/v2/token?refresh_token={token}&redirect_uri={redirect_uri}&client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token'
        request = requests.post(url).json()
        cls.token_creation_time = datetime.now()
        return request['access_token']
    
    @classmethod
    @property
    def token_status(cls):
        now = datetime.now()
        delta = now - cls.token_creation_time
        expiration = 60 - int(delta.seconds / 60)
        if expiration > 0:
            cls.is_token_expired = False
            return f'Token will expired in {expiration} minutes'
        cls.is_token_expired = True
        return 'Token has expired'

    def __repr__(self):
        now = datetime.now()
        expiration = 60 - now.minute
        return f'Zoho Books intance in 0x{id(self)}. Token will expire in {expiration} minutes'
