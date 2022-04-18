from dataclasses import dataclass, field
import requests
import json
import pymongo
from bson import ObjectId
import os
import utils

USER = os.environ.get('mongo_user')
PASS = os.environ.get('mongo_pass')
SERVER = os.environ.get('mongo_server')

print(SERVER)
mongo = pymongo.MongoClient(f'mongodb://{USER}:{PASS}{SERVER}/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false')

@dataclass
class API:
    endpoint: str
    headers: dict = field(default_factory=dict)
    endpoint_suffix: str = field(default_factory=str)

    def _standard_call(self, module: str, call_type: str, data=None, **kwargs):
        self.payload = f'{self.endpoint}{module}{self.endpoint_suffix}'
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
class ZohoBooksBase:
    db: pymongo.database = field(init=False, default_factory=mongo['Zoho_Mirror'])
    token: str = utils.get_token(db,'Books')
    organization_id: str = '683229417'
    api: API = API('https://books.zoho.com/api/v3/', {"Authorization": f'Zoho-oauthtoken {token}'}, endpoint_suffix=f'?organization_id={organization_id}')


