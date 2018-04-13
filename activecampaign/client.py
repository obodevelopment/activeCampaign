import requests
from requests.auth import HTTPBasicAuth
from activecampaign import exception
from .contacts import Contacts
from .deals import Deals

class Client(object):

    def __init__(self, url, apikey):

        if not url.startswith("http"):
            self._base_url = "https://" + url
        else:
            self._base_url = url
            self._apikey = apikey
            self.contacts = Contacts(self)
            self.deals = Deals(self)

    def _get(self, action, additional_data=None):
        return self._request('GET', action, additional_data=additional_data)

    def _post(self, action, data=None, additional_data=None):
        return self._request('POST', action, data=data, additional_data=additional_data)

    def _delete(self, action):
        return self._request('DELETE', action)

    def _request(self, method, action, data=None, additional_data=None):
        params =[
            ('api_action', action),
            ('api_key', self._apikey),
            ('api_output', 'json'),
        ]
        if additional_data is not None:
            for aditional in additional_data:
                params.append(aditional)
        response = requests.request(method, self._base_url+"/admin/api.php", params=params, data=data).json()
        return self._parse(response)

    def _parse(self, response):
        if response['result_code'] == 1:
            return response
        else:
            raise exception.ActiveCampaignError(response["result_message"])
