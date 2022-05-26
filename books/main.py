from books.api import items, salesorder, contacts
from datetime import datetime

class Books:
    def __init__(self, token:str, organization_id:str):
        self.items = items.Items(token, organization_id)
        self.salesorder = salesorder.SalesOrder(token, organization_id)
        self.contacts = contacts.Contacts(token, organization_id)

    def __repr__(self):
        now = datetime.now()
        expiration = 60 - now.minute
        return f'Zoho Books intance in 0x{id(self)}. Token will expire in {expiration} minutes'
