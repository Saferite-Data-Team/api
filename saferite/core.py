from dataclasses import dataclass, field
import requests
import json

@dataclass
class API:
    endpoint: str
    headers: dict = field(default_factory=dict)
    prefix: str = field(default_factory=str)
    suffix: str = field(default_factory=str)
    
    def _standard_call(self, module: str, call_type: str, data: dict=None, **kwargs):
        self.payload = f'{self.endpoint}{self.prefix}{module}{self.suffix}'
        additional_args = locals()['kwargs']
        if len(additional_args) == 0:
            self.params = None
            self.data = data
        else:
            self.data = data
            self.params = {}
            keys = []
            extra_param = {}
            for i in kwargs:
                keys.append(i)
                extra_param = {i: additional_args[i]}
                self.params.update(extra_param)
        if call_type == 'GET':
            self.request = requests.get(url=self.payload, headers=self.headers, params=self.params,data=self.data).text
        elif call_type == 'POST':
            self.request = requests.post(url=self.payload, headers=self.headers, params=self.params,data=self.data).text
        elif call_type == 'PUT':
            self.request = requests.put(url=self.payload, headers=self.headers, params=self.params,data=self.data).text
        elif call_type == 'DELETE':
            self.request = requests.delete(url=self.payload, headers=self.headers, params=self.params,data=self.data).text
        try:
            self.r = json.loads(self.request)
        except:
            self.r = self.request
        return self.r

@dataclass
class ZohoBooksBase():
    def __init__(self, token:str, organization_id:str):
        self.api = API(
            endpoint = 'https://books.zoho.com/api/v3/',
            headers = {
                "Authorization": f'Zoho-oauthtoken {token}'
            },
            suffix = f'?organization_id={organization_id}'
        )

@dataclass
class ZohoInventoryBase():
    def __init__(self, token:str, organization_id:str):
        self.api = API(
            endpoint = 'https://inventory.zoho.com/api/v1/',
            headers = {
                "Authorization": f'Zoho-oauthtoken {token}'
            },
            suffix = f'?organization_id={organization_id}'
        )

@dataclass
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

