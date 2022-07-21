from dataclasses import dataclass, field, fields
from saferite.core import Data

@dataclass
class ItemData(Data):
    name: str
    rate: float
    description: str = None
    tax_percentage: str = None
    sku: str = None
    product_type: str = None
    is_taxable: bool = None
    tax_exemption_id: str = None
    account_id: str = None
    avatax_tax_code: str = None
    avatax_use_code: str = None
    item_type: str = None
    purchase_description: str = None
    purchase_rate: str = None
    purchase_account_id: str = None
    inventory_account_id: str = None
    vendor_id: str = None
    reorder_level: str = None
    initial_stock: str = None
    initial_stock_rate: str = None
    
    def __post_init__(self):
        super().__post_init__()
        
        PRODUCT_TYPES = {'goods', 'service', 'digital_service'}
        ITEM_TYPES = {"sales", "purchases", "sales_and_purchases", "inventory"}
        
        self.enum_validation("product_type", PRODUCT_TYPES)
        self.enum_validation("item_type", ITEM_TYPES)
       
        if self.is_taxable is not None and not self.is_taxable and self.tax_exemption_id is None:
            raise TypeError('tax_exemption_id is required when is_taxable is False')

@dataclass
class SOLineItems(Data):
    item_id: str
    rate: float
    quantity: int
    line_item_id: str = None
    item_order: str = None
    name: str = None
    description: str = None
    product_type: str = None
    warehouse_id: str = None #Replace with Miami Warehouse ID
    discount: str = None
    tax_id: str = None
    tags: list = None
    unit: str = None
    item_custom_fields: list = None #Replace with actual custom fields
    tax_exemption_id: str = None
    tax_exemption_code: str = None
    avatax_exempt_no: str = None
    avatax_use_code: str = None
    project_id: str = None
    data: list = field(default_factory=list, init=False)

    def __call__(
        self,
        item_id:str,
        rate:float,
        quantity: int,
        item_order: str = None,
        name: str = None,
        description: str = None,
        product_type: str = None,
        warehouse_id: str = None, #Replace with Miami Warehouse ID
        discount: str = None,
        tax_id: str = None,
        tags: list = None,
        unit: str = None,
        item_custom_fields: list = None, #Replace with actual custom fields
        tax_exemption_id: str = None,
        tax_exemption_code: str = None,
        avatax_exempt_no: str = None,
        avatax_use_code: str = None,
        project_id: str = None
    ):
        _data = {k:v for k, v in locals().items() if v is not None and k != "self"}
        for k, v in _data.items():
            _type = self.schema[k]
            if not isinstance(v, _type):
                raise ValueError(f'Expected {k} to be {_type}, 'f'got {type(v)}')
        self.data.append(_data)

    def __post_init__(self):
        super().__post_init__()
        _data = {k:v for k, v in self.__dict__.items() if v is not None and k != "data"}
        self.data.append(_data)
        
    @property
    def schema(self):
        return {field.name: field.type for field in fields(self) if field.name != 'data'}

    @property
    def reset_data(self):
        self.data = []

@dataclass
class SOData(Data):
    customer_id: str
    date: str
    line_items: SOLineItems
    _so_channel: str
    contact_persons: list = None
    shipment_date: str = None
    custom_fields: list = field(default_factory=list, init=False)
    salesperson_id: str = None
    merchant_id: str = None
    notes: str = None
    terms: str = None
    billing_address_id: str = None
    shipping_address_id: str = None
    crm_owner_id: str = None
    crm_custom_reference_id: str = None
    salesorder_number: str = None
    reference_number: str = None
    is_update_customer: bool = None
    discount: str = None
    exchange_rate: str = None
    salesperson_name: str = None
    notes_default: str = None
    terms_default: str = None
    tax_id: str = None
    tax_authority_id: str = None
    tax_exemption_id: str = None
    tax_authority_name: str = None
    tax_exemption_code: str = None
    shipping_charge: float = None
    adjustment: float = None
    delivery_method: str = None
    estimate_id: str = None
    is_discount_before_tax: bool = None
    discount_type: str = None
    adjustment_description: str = None
    pricebook_id: str = None
    template_id: str = None
    documents: list = None
    zcrm_potential_id: str = None
    zcrm_potential_name: str = None
    _dropship_po: str = None

    def __post_init__(self):
        super().__post_init__()
        
        SO_CHANNELS = {
            'Field Houston',
            'Field Miami',
            'Field Orlando',
            'Field Los Angeles',
            'Frontline',
            'Internet',
            'ISP Account',
            'Square',
            'MDF Vendors'
        }
        
        self.enum_validation("_so_channel", SO_CHANNELS)
        self.date_validation(['date', 'shipment_date'], '%Y-%m-%d')
        self.line_items = self.line_items.data
        custom_data = {k:v for k, v in self.__dict__.items() if k.startswith('_') and v is not None}

        custom_ids = {
            '_so_channel': '1729377000039969865',
            '_dropship_po': '1729377001216648872'
        }

        for field in custom_data:
            data = {
                'customfield_id': custom_ids[field],
                'value': custom_data[field]
            }
            self.custom_fields.append(data)
    
@dataclass
class AddressData(Data):
    """
    Args:
        address: str
        city: str
        state: str
        zip: str
        country: str
        street2:str = None
        phone: str = None
        fax: str = None
        attention: str = None
        is_one_off_address: bool = None
        is_update_customer: bool = None
        is_verified: bool = None

    Returns:
        Data
    """
    address: str
    city: str
    state: str
    zip: str
    country: str = 'U.S.A'
    street2:str = None
    phone: str = None
    fax: str = None
    attention: str = None
    is_one_off_address: bool = None
    is_update_customer: bool = None
    is_verified: bool = None

@dataclass
class ContactPersonData(Data):
    first_name: str
    last_name: str
    email:str
    phone:str
    mobile:str=None
    salutation: str = None
    designation: str = None
    department: str = None
    skype: str = None
    is_primary_contact: bool = None
    enable_portal: bool = None
    

@dataclass
class DefaultTemplates(Data):
    invoice_template_id: str = None
    estimate_template_id: str = None
    creditnote_template_id: str = None
    purchaseorder_template_id: str = None
    salesorder_template_id: str = None
    retainerinvoice_template_id: str = None
    paymentthankyou_template_id: str = None
    retainerinvoice_paymentthankyou_template_id: str = None
    invoice_email_template_id: str = None
    estimate_email_template_id: str = None
    creditnote_email_template_id: str = None
    purchaseorder_email_template_id: str = None
    salesorder_email_template_id: str = None
    retainerinvoice_email_template_id: str = None
    paymentthankyou_email_template_id: str = None
    retainerinvoice_paymentthankyou_email_template_id: str = None
  

@dataclass
class ContactData(Data):
    contact_name: str
    company_name: str
    billing_address: AddressData
    shipping_address: AddressData
    website:str = None
    language_code: str = None
    contact_type: str = None
    customer_sub_type: str = None
    credit_limit: float = None
    tags: list = None
    is_portal_enabled: bool = None
    currency_id: str = None
    payment_terms: int = None
    payment_terms_label: str = None
    notes: str = None
    contacts_persons: ContactPersonData = None
    default_templates: DefaultTemplates = None
    custom_fields: list = None
    opening_balance_amount: float = None
    exchange_rate: float = None
    owner_id: str = None
    tax_authority_name: str = None
    tax_exemption_id: str = None
    tax_exemption_code: str = None
    tax_authority_id: str = None
    tax_id: str = None
    is_taxable: bool = None
    facebook: str = None
    twitter: str = None
    track_1099: bool = None
    tax_id_type: str = None
    tax_id_value: str = None
    
    def __post_init__(self):
        super().__post_init__()
        self.billing_address = self.billing_address.json
        self.shipping_address = self.shipping_address.json
    
    
    
    