from dataclasses import dataclass, field
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
            raise TypeError(
                'tax_exemption_id is required when is_taxable is False')


@dataclass
class SOLineItems(Data):
    __data: list = field(default_factory=list, init=False)

    def __call__(
        self,
        item_id: str,
        rate: float,
        quantity: int,
        bcy_rate: float = None,
        line_item_id: str = None,
        item_order: str = None,
        name: str = None,
        description: str = None,
        product_type: str = None,
        warehouse_id: str = None,
        discount: str = None,
        discount_amount: float = None,
        tax_id: str = None,
        tags: list = None,
        unit: str = None,
        item_custom_fields: list = None,
        tax_name: str = None,
        tax_type: str = None,
        tax_percentage: str = None,
        tax_treatment_code: str = None,
        header_name: str = None,
        tax_exemption_id: str = None,
        tax_exemption_code: str = None,
        avatax_exempt_no: str = None,
        avatax_use_code: str = None,
        project_id: str = None,
        project_name: str = None,
        expense_id: str = None,
        expense_receipt_name: str = None,
        time_entry_ids: list = None,
        custom_body: str = None,
        custom_subject: str = None,
        notes: str = None,
        terms: str = None,
        shipping_charge: str = None,
        adjustment: float = None,
        adjustment_description: str = None,
        purchaseorder_item_id: str = None,
        sku: str = None,
        account_id: str = None,
        account_name: str = None,
        item_total: int = None,
        item_total_inclusive_of_tax: float = None,
        is_billable: bool = None,
        customer_id: str = None,
        customer_name: str = None,
        invoice_id: str = None,
        invoice_number: str = None,
        salesorder_item_id: str = None
    ):

        _data_ = {k: v for k, v in locals().items()
                  if v is not None and k != "self"}
        self.__data.append(_data_)

    @staticmethod
    def fields():
        field_list = [
            'item_id',
            'rate',
            'quantity',
            'item_order',
            'name',
            'description',
            'product_type',
            'warehouse_id',
            'discount',
            'tax_id',
            'tags',
            'unit',
            'item_custom_fields',
            'tax_exemption_id',
            'tax_exemption_code',
            'avatax_exempt_no',
            'avatax_use_code',
            'project_id'
        ]
        return field_list

    @property
    def required_fields(self):
        field_list = [
            'item_id',
            'rate',
            'quantity'
        ]
        return field_list

    @property
    def data(self):
        if self.__data == []:
            raise ValueError(
                'No data has been passed to the SOLineItems class')
        return self.__data

    @property
    def reset_data(self):
        self.data = []


@dataclass
class TaxData(Data):
    tax_name: str
    tax_percentage: str
    tax_type: str = None
    tax_authority_name: str = None
    tax_authority_id: str = None
    country_code: str = None
    is_valued_added: bool = None
    update_recurring_invoice: bool = None
    update_recurring_expense: bool = None
    update_draft_invoice: bool = None
    update_recurring_bills: bool = None
    update_draft_so: bool = None
    update_subscription: bool = None
    update_project: bool = None
    is_editable: bool = None

    def __post_init__(self):
        super().__post_init__()

        TAX_TYPE = {
            'tax',
            'compound_tax'
        }

        self.enum_validation("tax_type", TAX_TYPE)


@dataclass
@dataclass
class SOData(Data):
    """Data model for SO, Invoices, Estimates, CreditNotes and PurchaseOrders

    Args:
    _transaction_type: str (required). Allowed Values: 'SO-', 'INV', 'SQ-'.
    customer_id: str (required)
    date: str (required)
    line_items: SOLineItems (required)
    _so_channel: str (required)
    reason: str (required for update call)
    contact_persons: list
    shipment_date: str (only SO)
    custom_fields: list = { 
            'customfield_id' : 0,
            'value': 'string'
    }
    salesperson_id: str
    salesperson_name: str 
    merchant_id: str (only SO)
    notes: str 
    terms: str
    billing_address_id: str
    shipping_address_id: str
    crm_owner_id: str (only SO)
    crm_custom_reference_id: str  (only SO)
    salesorder_number: str (only SO)
    reference_number: str 
    is_update_customer: bool  (only SO)
    discount: str
    exchange_rate: str 
    notes_default: str (only SO)
    terms_default: str (only SO)
    tax_id: str
    tax_authority_id: str 
    tax_exemption_id: str 
    tax_authority_name: str
    tax_exemption_code: str 
    shipping_charge: float
    adjustment: float 
    delivery_method: str (only SO)
    estimate_id: str 
    discount_type: str
    adjustment_description: str 
    pricebook_id: str (only SO)
    template_id: str 
    documents: list 
    zcrm_potential_id: str   (only SO)
    zcrm_potential_name: str  (only SO)
    _dropship_po: str
    _isp_sales_rep: str
    _eye4fraud: st
    _shipping_address_id : str
    _internal_notes : str 
    _payment_terms : str
    _address_validation : str
    invoice_number: str  (only invoice)
    due_date: str   (only invoice)
    is_discount_before_tax: bool 
    recurring_invoice_id: str  (only invoice)
    invoice_estimate_id: str (only invoice)
    allow_partial_payments: str (only invoice)
    estimate_number:str (only estimate)
    expiry_date: str (only estimates)
    reason: str 
    payment_options: dict   (only invoice) ='payment_options': {'payment_gateways': [{'configured': True,
            'can_show_billing_address': False,
            'is_bank_account_applicable': False,
            'can_pay_using_new_card': True,
            'gateway_name': 'braintree'}]},

    tags: list (only invoice)=[
                {
                    "is_tag_mandatory": false,
                    "tag_id": 982000000009070,
                    "tag_name": "Location",
                    "tag_option_id": 982000000002670,
                    "tag_option_name": "USA"
                }
            ],
    is_draft: bool  (only CreditNotes)
    credit_note_number: str (only CreditNotes)
    delivery_date: str (only purchaseOrder)
    vendor_id: str  (only purchaseOrder)
    purchaseorder_number: str   (only purchaseOrder)
    ship_via: str (only purchaseOrder)
    delivery_org_address_id: str   (only purchaseOrder)
        """
    _transaction_type: str
    customer_id: str
    date: str
    line_items: SOLineItems
    _so_channel: str
    custom_fields: list = field(default_factory=list, init=False)
    contact_persons: list = None
    shipment_date: str = None
    salesperson_id: str = None
    salesperson_name: str = None
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
    discount_type: str = None
    adjustment_description: str = None
    pricebook_id: str = None
    template_id: str = None
    documents: list = None
    zcrm_potential_id: str = None
    zcrm_potential_name: str = None
    _dropship_po: str = None
    _isp_sales_rep: str = None
    _eye4fraud: str = None
    _internal_notes: str = None
    _shipping_address_id: str = None
    _payment_terms: str = None
    _address_validation: str = None
    invoice_number: str = None
    due_date: str = None
    is_discount_before_tax: bool = None
    recurring_invoice_id: str = None
    invoice_estimate_id: str = None
    allow_partial_payments: bool = None
    estimate_number: str = None
    expiry_date: str = None
    reason: str = None
    payment_options: dict = None
    tags: list = None
    is_draft: bool = None
    credit_note_number: str = None
    delivery_date: str = None
    vendor_id: str = None
    purchaseorder_number: str = None
    ship_via: str = None
    delivery_org_address_id: str = None
    last_modified_time: str = None
    order_status: str = None

    def __post_init__(self):
        super().__post_init__()
        SO_CHANNELS = {
            'Field Houston',
            'Field Miami',
            'Field Orlando',
            'Field Los Angeles',
            'Frontline',
            'ISP Outbound Sales',
            'ISP Order Entry',
            'Vendors',
            'MDF Vendors',
            'Amazon ISP',
            'BC ISP',
            'BC SS',
            'eBay',
            '3M',
            'Project N95',
            'Internet'
        }
        TRANSACTION_TYPE = {
            'SO-',
            'INV',
            'SQ-'
        }
        DISCOUNT_TYPE = {
            'entity level',
            'item_level'
        }
        self.enum_validation("_so_channel", SO_CHANNELS)
        self.enum_validation("_transaction_type", TRANSACTION_TYPE)
        self.enum_validation("discount_type", DISCOUNT_TYPE)
        self.date_validation(
            ['date', 'shipment_date', 'expiry_date', 'delivery_date', 'due_date'], '%Y-%m-%d')
        self.line_items = self.line_items.data
        custom_data = {k: v for k, v in self.__dict__.items() if k.startswith(
            '_') and v is not None and k != '_transaction_type'}
        custom_ids = {
            'SO-': {
                '_so_channel': '1729377000039969865',
                '_dropship_po': '1729377001216648872',
                '_eye4fraud': '1729377001316393739',
                '_shipping_address_id': '1729377001314352847',
                '_internal_notes': '1729377001348214644',
                '_isp_sales_rep': '1729377000918761390',
                '_address_validation': '1729377001364999109'

            },
            'INV': {
                '_so_channel': '1729377000880233358',
                '_dropship_po': '1729377001216648914',
                '_isp_sales_rep':  '1729377000039969883',
                '_address_validation': '1729377001364999049'


            },
            'SQ-': {
                '_so_channel': '1729377001340068453',
                '_address_validation': '1729377001358036674',
                '_payment_terms': '1729377000039606098',

            }
        }

        for field in custom_data:
            data = {
                'customfield_id': custom_ids[self.__dict__['_transaction_type']][field],
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
    street2: str = None
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
    email: str
    phone: str
    mobile: str = None
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
    website: str = None
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


@dataclass
class BillsData(Data):
    """
    purchaseorder_ids: [
        460000000068231,
        460000000068233
    ]
    documents(list)= [
        {
            "document_id": 0,
            "file_name": "string"
        }
    ]
    custom_fields(list) = [
        {

            "custom_field_id": 0,
            "index": 0,
            "value": "string",
            "label": "string"

        }
    ]
     "purchaseorders"(list): [
        {
            "purchaseorder_id": "460000000068231",
            "purchaseorder_number": "PO-0001",
            "purchaseorder_date": "19 Jan 2017",
            "purchaseorder_status": "billed"
        }
    ]
    taxes(list) =  [
        {
            "tax_name": "VAT (12.5%)",
            "tax_amount": 1.25
        }
    ]
    payments(list) = [
        {
            "payment_id": "460000000042059",
            "bill_id": "460000000098765",
            "bill_payment_id": "460000000042061",
            "payment_mode": "Cash",
            "payment_number": "string",
            "description": "string",
            "date": "2013-09-11",
            "reference_number": "4321133",
            "exchange_rate": 1.23,
            "amount": 31.25,
            "paid_through_account_id": "460000000000358",
            "paid_through_account_name": "Undeposited Funds",
            "is_single_bill_payment": true,
            "is_paid_via_print_check": false,
            "check_details": [
                {
                    "check_status": "string",
                    "check_number": "string"
                }
            ],
            "is_ach_payment": false,
            "ach_payment_status": "string",
            "ach_gw_transaction_id": "string",
            "filed_in_vat_return_id": "string",
            "filed_in_vat_return_name": "string",
            "filed_in_vat_return_type": "string"
        }
    ]
    vendor_credits(list) = [
        {
            "vendor_credit_id": "4600000053221",
            "vendor_credit_bill_id": "4600000211221",
            "vendor_credit_number": "DN-001",
            "date": "27 Dec 2016",
            "amount": 10
        }
    ]




    """
    bill_id: str
    purchaseorder_ids: list
    vendor_id: str
    vendor_name: str = None
    pricebook_id: str = None
    pricebook_name: str = None
    unused_credits_payable_amount: int = None
    status: str = None
    bill_number: str = None
    date: str = None
    due_date: str = None
    payment_terms: str = None
    payment_terms_label: str = None
    payment_expected_date: str = None
    reference_number: str = None
    recurring_bill_id: str = None
    due_by_days: int = None
    currency_id: str = None
    currency_code: str = None
    currency_simbol: str = None
    documents: list = None
    price_precision: int = None
    exchange_rate: float = None
    adjustment: float = None
    adjustment_description: str = None
    custom_fields: list = None
    is_item_level_taxcalc: bool = None
    line_items: SOLineItems = None
    sub_total: int = None
    tax_total: int = None
    total: int = None
    payment_made: int = None
    vendor_credits_applied: int = None
    is_line_item_invoice: bool = None
    purchaseorder: list = None
    taxes: list = None
    balance: int = None
    billing_address: AddressData = None
    paymnets: list = None
    vendor_credits: list = None
    created_time: str = None
    created_by_id: str = None
    last_modified_time: str = None
    reference_id: str = None
    notes: str = None
    attachment_name: str = None
    open_purchaseorder_count: int = None

    def __post_init__(self):
        super().__post_init__()

        self.date_validation(
            ['date', 'due_date', 'payment_expected_date', 'created_time'], '%Y-%m-%d')


@dataclass
class PaymentData(Data):
    __data: list = field(default_factory=list, init=False)

    def __call__(
        self,
        customer_id: str,
        payment_mode: str,
        amount: float,
        date: str,
        invoices: list,
        invoice_id:str,
        amount_applied:float,
        reference_number: str = None,
        description: str = None,
        exchange_rate: float = None,
        bank_charges:float = None,
        custom_fields:list = None,
        tax_amount_withheld:float = None,
        account_id:str = None
        ):
        _data_ = {k:v for k, v in locals().items() if v is not None and k != 'self'}
        self.__data.append(_data_)
    
    @staticmethod
    def fields():
        field_list = [
        'customer_id',
        'payment_mode',
        'amount',
        'date',
        'invoices',
        'invoice_id',
        'amount_applied',
        'reference_number',
        'description',
        'exchange_rate',
        'bank_charges',
        'custom_fields',
        'tax_amount_withheld',
        'account_id'
        ]
    
    @property
    def data(self):
        if self.__data == []:
            raise ValueError("No data has been passed to the PaymentData")
        return self.__data
    
    @property
    def reset_data(self):
        self.data = []
        