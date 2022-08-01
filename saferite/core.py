from dataclasses import dataclass, field, fields
import requests
from datetime import datetime
import base64

@dataclass
class API:
    endpoint: str
    headers: dict = field(default_factory=dict)
    prefix: str = field(default_factory=str)
    suffix: str = field(default_factory=str)
    
    def _standard_call(self, module: str, call_type: str, data: dict=None, **kwargs):
        self.payload = f'{self.endpoint}{self.prefix}{module}{self.suffix}'
        additional_args = locals()['kwargs']
        self.params = None if len(additional_args) == 0 else additional_args
        return getattr(requests, call_type)(url=self.payload, headers=self.headers, params=self.params, data=data).json()

class ZohoBooksBase():
    def __init__(self, token:str, organization_id:str):
        self.api = API(
            endpoint = 'https://books.zoho.com/api/v3/',
            headers = {
                "Authorization": f'Zoho-oauthtoken {token}'
            },
            suffix = f'?organization_id={organization_id}'
        )

class ZohoInventoryBase():
    def __init__(self, token:str, organization_id:str):
        self.api = API(
            endpoint = 'https://inventory.zoho.com/api/v1/',
            headers = {
                "Authorization": f'Zoho-oauthtoken {token}'
            },
            suffix = f'?organization_id={organization_id}'
        )

class BCBase():
    def __init__(self, token:str, client:str, store_hash:str, version:int):
        self.api = API(
            endpoint = f'https://api.bigcommerce.com/stores/{store_hash}',
            headers = {
                'accept': "application/json",
                'content-type': "application/json",
                'x-auth-token': token,
                'x-auth-client': client,
            },
            prefix=f'/v{version}/'
        )


class ShipstationBase():
    def __init__(self, username:str, password:str):
        base64_auth = base64.b64encode(f'{username}:{password}'.encode()).decode('utf-8')
        self.api = API(
            endpoint = 'https://ssapi.shipstation.com/',
            headers = {
                'Authorization': f'Basic {base64_auth}'
            }
        )
    
class Data:

    @property
    def json(self):
        return {k: v for k,v in self.__dict__.items() if v is not None and k not in ['data'] and not k.startswith('_')}
    
    def __post_init__(self):
        for field in fields(self):
            value = getattr(self, field.name)
            if not isinstance(value, field.type) and value is not None:
                raise ValueError(f'Expected {field.name} to be {field.type}, 'f'got {type(value)}')
    
    def enum_validation(self, field_name:str, enum:set):
        if getattr(self,field_name) not in enum and getattr(self,field_name) is not None:
            raise ValueError(f'The allowed values for {field_name} are {enum}')
    
    def date_validation(self, date_fields: list, date_format:str):
        for date in date_fields:
            value = getattr(self,date)
            if value is not None:
                datetime.strptime(value, date_format)
    
    @classmethod
    def from_dataframe(cls, df, field_name:str, field_value:str, repeated:bool = False, **kwargs):
        additional_data = locals()['kwargs']

        class_columns = set(cls.__match_args__) if cls.__match_args__ != () else set(cls.fields())
        df_columns = set(df.columns)
        columns = list(df_columns.intersection(class_columns))

        data = df.loc[df[field_name] == field_value, columns].to_dict('records')

        for value in data:
            value.update(additional_data)
        
        if repeated:
            ins = cls()
            for value in data:
                ins(**value)
            return ins
        return cls(**data[0])

#From StackOverflow answer by @Ilya_Peterov
from typing import get_type_hints

def strict_types(f):
    def type_checker(*args, **kwargs):
        hints = get_type_hints(f)

        all_args = kwargs.copy()
        all_args.update(dict(zip(f.__code__.co_varnames, args)))

        for key in all_args:
            if key in hints:
                if type(all_args[key]) != hints[key]:
                    raise Exception(f'Type of {key} is {type(all_args[key])} and not {hints[key]}')

        return f(*args, **kwargs)

    return type_checker