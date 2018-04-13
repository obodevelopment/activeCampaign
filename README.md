# ActiveCampaign Python
## Python wrapper for the ActiveCampaign V2 API

The contact endpoints are implemented as a class.

To access the endpoint the base instance URL and ActiveCampaign API Key are needed.

To make a request add your API Key and your Active Campaign Endpoint.

## Import Lib and api url + key

from activecampaign.client import Client
ac = Client(settings.ACTIVECAMPAIGN_URL, settings.ACTIVECAMPAIGN_API_KEY)

## Contact

### Add Contact:
data = {
    'email': 'hey@email.com',
    'first_name': 'Name',
}
ac.contacts.add(data)
response = {'subscriber_id': XXX, 'sendlast_should': 0, 'sendlast_did': 0, 'result_code': 1, 'result_message': 'Contact added', 'result_output': 'json'}

***
    Available Keyword Arguments when editing contacts:
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
***

### Update Contact:
data = {
    'email': 'hey@email.com',
    'first_name': 'Name',
    'last_name': 'Henry',
}
ac.contacts.edit(data)
  This is set to not overwrite all list fields by default.

### Delete Contact:
ac.contacts.delete(id)
	response = {'result_code': 1, 'result_message': 'Contact deleted', 'result_output': 'json'}

### Lookup Contact By Email:
ac.contacts.lookup_by_email('hey@email.com')

### Add Note To Contact:
ac.contacts.add_note(list_id, email, note)

### Add Tag To Contact:
ac.contacts.add_tag(contact_email, tag)

## Deals

### Add Deal
ac.deals.add(title, value, pipeline, contact_id)

***
    Available Fields to Create a Deal
    title*  Title of the new deal. Example: 'Deal Title'
    value*  Value of the new deal in dollars. Example: '450.00' or 450
    currency* Currency of the new deal. Example: 'usd'
    pipeline* ID of the new deal's pipeline. Example: '3' (Get available pipeline IDs with "deal_pipeline_list" call)
    stage*  ID of the new deal's stage. Example: '52' (Get available stage IDs with "deal_stage_list" call)
    contactid ID of an existing contact for the new deal. Example: '8'. NOTE: IF THIS IS NOT PROVIDED, 'contact' MUST BE. (Get available contact IDs with "contact_list" call)
    contact_name  Name of the contact for the new deal. Example: 'John Doe'
    organization  Name of the organization of the contact for the new deal. Example: 'Acme Corp'
***

### Add Note to Deal
ac.deals.add_note(note, deal_id)

***
    Available Fields to add a note to a deal
    note*   Text of the note. Example: 'Follow up about this deal soon'
    dealid* ID of the deal for the new deal note. Example: '31' (Get available deal IDs with "deal_list" call)
    owner   ID of the owner of the new deal note. Example: '4' (Get available owner IDs with "user_list" call)
***
