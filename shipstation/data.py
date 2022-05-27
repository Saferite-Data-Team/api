from saferite.core import Data
from dataclasses import dataclass, field, fields

@dataclass
class AddressData(Data):
    name: str
    company: str
    street1: str
    city: str
    state: str
    postalCode: str
    phone: str
    residential: bool = False
    street2: str = None
    street3:str = None

@dataclass
class ItemData(Data):
    sku: str
    name: str
    quantity: int
    shippingAmount: float
    _salesorder_id: str
    _line_item_id: str
    _item_id: str
    _weight_unit: str = None
    _weight_value: float = None
    unitPrice: float = None
    taxAmount: float = None
    options: list = field(default_factory=list)
    adjustment: bool = False
    upc: str = None
    weight: dict = None
    data: list = field(default_factory=list, init=False)
    
    def __post_init__(self):
        super().__post_init__()
        
        WEIGHT_UNITS = {'pounds', 'ounces', 'grams'}
        
        if self._weight_unit is not None and self._weight_value is None:
            raise TypeError('weight_value is required when weight_unit is passed')
        
        if self._weight_value is not None and self._weight_unit is None:
            raise TypeError('weight_unit is required when weight_value is passed')
            
        if self._weight_unit is not None and self._weight_value is not None:
            self.enum_validation("_weight_unit", WEIGHT_UNITS)
            self.weight = {
                'value': self._weight_value,
                'units': self._weight_unit
            }
        
        self.options = [
            {'name': 'salesorder_id', 'value': self._salesorder_id},
            {'name': 'line_item_id', 'value': self._line_item_id},
            {'name': 'item_id', 'value': self._item_id}
        ]
        
        _data = {k:v for k, v in self.__dict__.items() if v is not None and k != "data" and not k.startswith('_')}
        for k, v in _data.items():
            _type = self.schema[k]
            if not isinstance(v, _type):
                raise ValueError(f'Expected {k} to be {_type}, 'f'got {type(v)}')
        self.data.append(_data)
    
    def __call__(
        self,
        sku: str,
        name: str,
        quantity: int,
        shippingAmount: float,
        _salesorder_id: str,
        _line_item_id: str,
        _item_id: str,
        _weight_unit: str = None,
        _weight_value: float = None,
        unitPrice: float = None,
        taxAmount: float = None,
        options: list = [],
        adjustment: bool = False,
        upc: str = None,
        weight: dict = None
        ):
        
        WEIGHT_UNITS = {'pounds', 'ounces', 'grams'}
        
        if locals()['_weight_unit'] is not None and locals()['_weight_value'] is None:
            raise TypeError('weight_value is required when weight_unit is passed')
        
        if locals()['_weight_value'] is not None and locals()['_weight_unit'] is None:
            raise TypeError('weight_unit is required when weight_value is passed')
            
        if locals()['_weight_unit'] is not None and locals()['_weight_value'] is not None:
            self.enum_validation("_weight_unit", WEIGHT_UNITS)
            self.weight = {
                'value': self._weight_value,
                'units': self._weight_unit
            }
        
        self.options = [
            {'name': 'salesorder_id', 'value': locals()['_salesorder_id']},
            {'name': 'line_item_id', 'value': locals()['_line_item_id']},
            {'name': 'item_id', 'value': locals()['_item_id']}
        ]
        
        _data = {k:v for k, v in locals().items() if v is not None and k not in ["self", "WEIGHT_UNITS"] and not k.startswith('_')}
        for k, v in _data.items():
            _type = self.schema[k]
            if not isinstance(v, _type):
                raise ValueError(f'Expected {k} to be {_type}, 'f'got {type(v)}')
        self.data.append(_data)
    @property
    def schema(self):
        return {field.name: field.type for field in fields(self) if field.name != 'data'}
        

@dataclass
class OrderData(Data):
    orderNumber: str #max 50
    orderDate: str #
    orderStatus: str #awaiting_payment, awaiting_shipment, shipped, on_hold, cancelled
    billTo: AddressData ###
    shipTo: AddressData
    _store_id: str
    _salesorder_id: str
    items: list = field(default_factory=list) #
    amountPaid: float = None
    taxAmount: float = None
    shippingAmount: float = None
    customerNotes: str = None
    internalNotes: str = None
    gift: bool = None
    giftMessage: str = None
    paymentMethod: str = None
    requestedShippingService: str = None
    carrierCode: str = None
    serviceCode: str = None
    packageCode: str = None
    confirmation: str = None
    _weight_value: float = None
    _weight_unit: str = None #ounces, grams, pounds
    _dim_unit: str = None #inches, centimeters
    _dim_length: int = None
    _dim_width: int = None
    _dim_height: int = None
    insuranceOptions: dict = None
    _warehouse_id: str = '194522'
    _source: str = 'Zoho'
    advanceOptions: dict = field(default_factory=dict)
    dimensions: dict = field(default_factory=dict)
    weight: dict = field(default_factory=dict)
    
    def __post_init__(self):
        super().__post_init__()
        
        self.advanceOptions = {
            'warehouseId': self._warehouse_id,
            'customField1': self._salesorder_id,
            'storeId': self._store_id,
            'source': self._source
        }
        
        self.dimentions = {
            'unit': self._dim_unit,
            'length': self._dim_length,
            'width': self._dim_width,
            'height': self._dim_height
        }
        
        self.weight = {
            'value': self._weight_value,
            'units': self._weight_unit
        }
        
        # PRODUCT_TYPES = {'goods', 'service', 'digital_service'}
        # ITEM_TYPES = {"sales", "purchases", "sales_and_purchases", "inventory"}
        
        # self.enum_validation("product_type", PRODUCT_TYPES)
        # self.enum_validation("item_type", ITEM_TYPES)
