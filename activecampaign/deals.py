import requests
import simplejson as json

def ac_api_request(querystring, payload, v2url):
    querystring = querystring
    payload = payload
    base_url = v2url
    url = base_url + "/admin/api.php?"
    headers = {
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    return response

############################  V2 API  #################################################
class deals(object):
    def __init__(self, key=None, url=None):
        self.api_key = key
        self.base_url = url

    '''
        Available Fields to Create a Deal
        title*  Title of the new deal. Example: 'Deal Title'
        value*  Value of the new deal in dollars. Example: '450.00' or 450
        currency* Currency of the new deal. Example: 'usd'
        pipeline* ID of the new deal's pipeline. Example: '3' (Get available pipeline IDs with "deal_pipeline_list" call)
        stage*  ID of the new deal's stage. Example: '52' (Get available stage IDs with "deal_stage_list" call)
        contactid ID of an existing contact for the new deal. Example: '8'. NOTE: IF THIS IS NOT PROVIDED, 'contact' MUST BE. (Get available contact IDs with "contact_list" call)
        contact_name  Name of the contact for the new deal. Example: 'John Doe'
        organization  Name of the organization of the contact for the new deal. Example: 'Acme Corp'
    '''
    def add_deal(title, value, pipeline, contactid, **kwargs):
        querystring = {"api_key": deals.api_key,
                       "api_action": "deal_add",
                       "api_output": "json"
                    }
        payload = {"title": title,
                    "value": value,
                    "currency": 'usd',
                    "pipeline": pipeline,
                    "contactid": contactid
                }
        for key in kwargs:
            payload['{}'.format(key)] = "{}".format(kwargs[key])
        request = ac_api_request(querystring, payload, deals.base_url)

        return json.loads(request.text)


    '''
        Available Fields to add a note to a deal
        note*   Text of the note. Example: 'Follow up about this deal soon'
        dealid* ID of the deal for the new deal note. Example: '31' (Get available deal IDs with "deal_list" call)
        owner   ID of the owner of the new deal note. Example: '4' (Get available owner IDs with "user_list" call)
    '''

    def add_deal_note(note, dealid, **kwargs):
        querystring = {"api_key": deals.api_key,
                       "api_action": "deal_note_add",
                       "api_output": "json"
                    }
        payload = { "note": note,
                    "dealid": dealid,
                }
        for key in kwargs:
            payload['{}'.format(key)] = "{}".format(kwargs[key])
        request = ac_api_request(querystring, payload, deals.base_url)

        return json.loads(request.text)