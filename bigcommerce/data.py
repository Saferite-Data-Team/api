from dataclasses import dataclass
from saferite.core import Data

@dataclass
class AddressData(Data):
    customer_id: int
    first_name: str
    last_name: str
    city: str
    country_code: str
    address1: str
    address2: str = None
    company: str = None
    state_or_province: str = None
    postal_code: str = None
    phone: str = None
    address_type: str = None
    form_fields: list = None

@dataclass
class BrandData(Data):
    name: str
    page_title: str = None
    meta_keywords: list = None
    meta_description: str = None
    search_keywords: str = None
    image_url: str = None
    custom_url: dict = None

@dataclass
class CartData(Data):
    customer_id: int
    line_items: list
    custom_items: list = None
    gift_certificates: list = None
    channel_id: int = None
    currency: dict = None
    locale: str = None

@dataclass
class CategoryData(Data):
    parent_id: int
    name: str
    description: str = None
    views: int = None
    sort_order: int = None
    page_title: str = None
    search_keywords: str = None
    meta_keywords: list = None
    meta_description: str = None
    layout_file: str = None
    is_visible: bool = None
    default_product_sort: str = None
    img_url: str = None
    custom_url: dict = None

    def __post_init__(self):
        super().__post_init__()

        DEFAULT_PRODUCT_SORT_TYPES = {
            'use_store_settings', 'featured', 'newest',
            'best_selling', 'alpha_asc', 'alpha_desc',
            'avg_customer_review', 'price_asc', 'price_desc'
        }

        self.enum_validation('default_product_sort', DEFAULT_PRODUCT_SORT_TYPES)

@dataclass
class CustomerData(Data):
    first_name: str
    last_name: str
    email: str
    company: str = None
    phone: str = None
    notes: str = None
    tax_exempt_category: str = None
    customer_group_id: int = None
    addresses: list = None
    attributes: list =  None
    authentication: dict = None
    accepts_product_review_abandoned_cart_emails: bool = None
    store_credit_amounts: list = None
    origin_channel_id: int = None
    channel_ids: list = None
    form_fields: list = None
    id: int = None

    def __post_init__(self):
        super().__post_init__()

@dataclass
class OrderData(Data):
    products: list
    billing_address: dict
    shiping_addresses: list = None
    base_handling_cost: str = None
    base_shipping_cost: str = None
    base_wrapping_cost: str = None
    channel_id: int = None
    customer_id: int = None
    customer_message: str = None
    date_created: str = None
    default_currency_code: str = None
    discount_amount: str = None
    ebay_order_id: str = None
    external_id: str = None
    external_merchant_id: str = None
    external_source: str = None
    geoip_country: str = None
    geoip_country_iso2: str = None
    handling_cost_ex_tax: str = None
    handling_cost_inc_tax: str = None
    ip_address: str = None
    ip_address_v6: str = None
    is_deleted: bool = None
    items_shipped: int = None
    items_total: int = None
    orders_is_digital: bool = None
    payment_method: str = None
    payment_provider_id: str = None
    refunded_amount: str = None
    shipping_cost_ex_tax: str = None
    shipping_cost_inc_tax: str = None
    staff_notes: str = None
    status_id: int = None
    subtotal_ex_tax: str = None
    subtotal_inc_tax: str = None
    tax_provider_id: str = None
    customer_locale: str = None
    total_ex_tax: str = None
    total_inc_tax: str = None
    wrapping_cost_ex_tax: str = None
    wrapping_cost_inc_tax: str = None

    def __post_init__(self):
        super().__post_init__()

        PAYMENT_METHOD_TYPES = {'Credit Card', 'Cash', 'Test Payment Gateway', 'Manual'}
        TAX_PROVIDER_TYPES = {'BasicTaxProvider', 'AvaTaxProvider'}

        self.enum_validation('payment_method', PAYMENT_METHOD_TYPES)
        self.enum_validation('tax_provider_id', TAX_PROVIDER_TYPES)

@dataclass
class ShipmentData(Data):
    order_address_id: int
    items: list
    tracking_number: str = None
    shipping_method: str = None
    shipping_provider: str = None
    tracking_carrier: str = None
    comments: str = None

    def __post_init__(self):
        super().__post_init__()

@dataclass
class ShippingAddressData(Data):
    first_name: str = None
    last_name: str = None
    company: str = None
    street_1: str = None
    street_2: str = None
    city: str = None
    state: str = None
    zip: str = None
    country: str = None
    country_iso_2: str = None
    phone: str = None
    email: str = None
    shipping_method: str = None


@dataclass
class RefundData(Data):
    items: list
    payments: list
    reason: str
    merchant_calculated_override: dict



@dataclass
class ProductData(Data):
    name: str
    type: str
    weight: float
    price: float
    sku: str = None
    description: str = None
    width: float = None
    depth: float = None
    height: float = None
    cost_price: float = None
    retail_price: float = None
    sale_price: float = None
    map_price: int = None
    tax_class_id: int = None
    product_tax_code: str = None
    categories: list = None
    brand_id: int = None
    inventory_level: int = None
    inventory_warning_level: int = None
    inventory_traking: str = None
    fixed_cost_shipping_price: float = None
    is_free_shipping: bool = None
    is_visible: bool = None
    is_featured: bool = None
    related_products: list = None
    warranty: str = None
    bin_picking_number: str = None
    layout_file: str = None
    upc: str = None
    search_keywords: str = None
    availability: str = None
    availability_description: str = None
    gift_wrapping_options_type: str = None
    gift_wrapping_options_list: list = None
    sort_order: int = None
    condition: str = None
    is_condition_shown: bool = None
    order_quantity_minimum: int = None
    order_quantity_maximum: int = None
    page_title: str = None
    meta_keywords: list = None
    meta_description: str = None
    view_count: int = None
    preorder_release_date: str = None
    preorder_message: str = None
    is_preorder_only: bool = None
    price_hidden_label: str = None
    custom_url: dict = None
    open_graph_type: str = None
    open_graph_title: str = None
    open_graph_description: str = None
    open_graph_use_meta_description: bool = None
    open_graph_use_product_name: bool = None
    open_graph_use_image: bool = None
    brand_id: str = None
    gtin: str = None
    mpn: str = None
    reviews_rating_sum: float = None
    reviews_count: int = None
    total_sold: int = None
    custom_fields: list = None
    bulk_pricing_rules: list = None
    images: list = None
    videos: list = None

    def __post_init__(self):
        super().__post_init__()

        PRODUCT_TYPES = {'physical', 'digital'}
        INVENTORY_TRAKING_TYPES = {'none', 'product', 'variant'}
        AVAILABILITY = {'available', 'disable', 'preorder'}
        GIFT_WRAPPING_OPTIONS_TYPES = {'any', 'none', 'list'}
        CONDITION_TYPES = {'New', 'Used', 'Refurbished'}
        OPEN_GRAPH_TYPES = {
            'product', 'album', 'book', 'drink','food',
            'game', 'movie', 'song', 'tv_show'
        }

        self.enum_validation('type', PRODUCT_TYPES)
        self.enum_validation('inventory_traking', INVENTORY_TRAKING_TYPES)
        self.enum_validation('availability', AVAILABILITY)
        self.enum_validation('gift_wrapping_options_type', GIFT_WRAPPING_OPTIONS_TYPES)
        self.enum_validation('condition', CONDITION_TYPES)
        self.enum_validation('open_graph_type', OPEN_GRAPH_TYPES)
