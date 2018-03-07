import requests
import simplejson as json


#activeCampaign.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#activeCampaign.base_url = "https://xxxxxxxxxxxx.api-us1.com"

def ac_api_request(querystring, payload, v2url):
    querystring = querystring
    payload = payload
    base_url = v2url
    url = base_url + "/admin/api.php?"
    print(url)
    headers = {
        'cache-control': "no-cache",
        'content-type': "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    #print(response)
    return response

############################  V2 API  #################################################
class activeCampaign(object):
    def __init__(self, key=None, url=None):
        self.api_key = key
        self.base_url = url
        #self.endpoint = "/admin/api.php?"
        #self.v2url = self.base_url + self.endpoint

    '''
                Available Fields to Create a Contact
                first_name	First name of the contact. Example: 'FirstName'
                last_name	Last name of the contact. Example: 'LastName'
                phone	Phone number of the contact. Example: '+1 312 201 0300'
                orgname	Organization name (if doesn't exist, this will create a new organization) - MUST HAVE CRM FEATURE FOR THIS.
                tags	Tags for this contact (comma-separated). Example: "tag1, tag2, etc"
                ip4	IP address of the contact. Example: '127.0.0.1' If not supplied, it will default to '127.0.0.1'
                field[345,0]	Custom field values. Example: field[345,0] = 'value'. In this example, "345" is the field ID. Leave 0 as is.
                field[%PERS_1%,0]	'value' (You can also use the personalization tag to specify which field you want updated)
                p[123]*	Assign to lists. List ID goes in brackets, as well as the value.
                status[123]	The status for each list the contact is added to. Examples: 1 = active, 2 = unsubscribed
                form	Optional subscription Form ID, to inherit those redirection settings. Example: 1001. This will allow you to mimic adding the contact through a subscription form, where you can take advantage of the redirection settings.
                noresponders[123]	Whether or not to set "do not send any future responders." Examples: 1 = yes, 0 = no.
                sdate[123]	Subscribe date for particular list - leave out to use current date/time. Example: '2009-12-07 06:00:00'
                instantresponders[123]	Use only if status = 1. Whether or not to set "send instant responders." Examples: 1 = yes, 0 = no.
                lastmessage[123]	Whether or not to set "send the last broadcast campaign." Examples: 1 = yes, 0 = no.
    '''
    def add_contact(email, **kwargs):
        querystring = {"api_key": activeCampaign.api_key,
                       "api_action": "contact_add",
                       "api_output": "json",
                       "email": "{}".format(email)}
        payload = {"email": email ,}
        for key in kwargs:
            payload['{}'.format(key)] = "{}".format(kwargs[key])
        request = ac_api_request(querystring, payload, activeCampaign.base_url)
        return json.loads(request.text)

    def update_contact(contact_id, **kwargs):
        querystring = {"api_key":  ActiveCampaign.api_key,
                       "api_action": "contact_edit",
                       "api_output": "json",
                        }

        payload = {"id": contact_id,
                   "overwrite": 0,
                   }

        for key in kwargs:
            payload['{}'.format(key)] = "{}".format(kwargs[key])
        request = ac_api_request(querystring, payload, ActiveCampaign.base_url)
        return json.loads(request.text)

    def delete_contact(contact_id):
        querystring = {"api_key":  activeCampaign.api_key,
                       "api_action": "contact_delete",
                       "api_output": "json",
                       }

        payload = {"id": contact_id,
                   }

        request = ac_api_request(querystring, payload, activeCampaign.base_url)
        return json.loads(request.text)

    def lookup_contact_by_email(email):
        querystring = {"api_key": activeCampaign.api_key,
                       "api_action": "contact_view_email",
                       "api_output": "json",
                       "email": "{}".format(email)}
        request = ac_api_request(querystring, None, activeCampaign.base_url)
        return json.loads(request.text)

    def add_contact_note(user_email, contact_email, note):
        try:
            contact = lookup_contact_by_email(contact_email)
            contact_id = contact['id']
        except:
            print("Error Finding Contact in Active Campaign")
            return "Error Finding Contact in Active Campaign"

        querystring = {"api_key":  activeCampaign.api_key,
                       "api_action": "contact_note_add",
                       "api_output": "json",
                       "email": "{}".format(user_email)}

        payload = {"email": "test@outboundops.com",
                   "id": "{}".format(contact_id),
                   "listid": "0",
                   "note": "{}".format(note)
                   }
        request = ac_api_request(querystring, payload, activeCampaign.base_url)
        return json.loads(request.text)

    def get_contact_automation(email):
        querystring = {"api_key":  activeCampaign.api_key,
                       "api_action": "contact_automation_list",
                       "api_output": "json",
                       "contact_email": "{}".format(email)}
        request = ac_api_request(querystring, None, activeCampaign.base_url)
        return json.loads(request.text)

    def add_contact_to_automation(email, automation_number):
        querystring = {"api_key":  activeCampaign.api_key,
                       "api_action": "automation_contact_add",
                       "api_output": "json",
                       }

        payload = {"contact_email": "{}".format(email),
                   "automation": "{}".format(automation_number) }

        request = ac_api_request(querystring, payload, activeCampaign.base_url)
        return json.loads(request.text)

    def remove_contact_from_automation(email, automation_number):
        querystring = {"api_key":  activeCampaign.api_key,
                       "api_action": "automation_contact_remove",
                       "api_output": "json",
                       }

        payload = {"contact_email": "{}".format(email),
                   "automation": "{}".format(automation_number) }

        request = ac_api_request(querystring, payload, activeCampaign.base_url)
        return json.loads(request.text)

    def add_contact_tag(contact_email, tag):
        querystring = {"api_key":  activeCampaign.api_key,
                       "api_action": "contact_tag_add",
                       "api_output": "json",
                       }

        payload = {"email": "{}".format(contact_email),
                   "tags": "{}".format(tag)
                   }
        request = ac_api_request(querystring, payload, activeCampaign.base_url)
        return json.loads(request.text)

    def get_all_campaign_details():
        querystring = {"api_key":  activeCampaign.api_key,
                       "api_action": "campaign_list",
                       "api_output": "json",}
        request = ac_api_request(querystring, None, activeCampaign.base_url)
        return json.loads(request.text)