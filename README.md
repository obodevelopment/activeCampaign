# ActiveCampaign Python
## Python wrapper for the ActiveCampaign V2 API

The contact endpoints are implemented as a class.

To access the endpoint the base instance URL and ActiveCampaign API Key are needed.

To make a request add your API Key and your Active Campaign Endpoint.

activeCampaign.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  
https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API  
activeCampaign.base_url = "https://xxxxxxxxxxxx.api-us1.com"  

### Add Contact:
activeCampaign.add_contact(email, FirstName="John")  
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
activeCampaign.update_contact("contact_id", FirstNAme="Johns")  
  This is set to not overwrite all list fields by default.  

### Delete Contact:  
activeCampaign.delete_contact(contact_id)  
	response = {'result_code': 1, 'result_message': 'Contact deleted', 'result_output': 'json'}  

### Lookup Contact By Email:  
activeCampaign.lookup_contact_by_email(email)  

### Add Note To Contact:  
activeCampaign.add_contact_note(user_email, contact_email, note)  

### Get Contact Automations:  
activeCampaign.get_contact_automation(email)  

### Add Contact to Automation:  
activeCampaign.add_contact_to_automation(email, automation_number)  

### Remove Contact From Automation:  
activeCampaign.remove_contact_from_automation(email, automation_number)  

### Add Tag To Contact:  
activeCampaign.add_contact_tag(contact_email, tag)  

### Get all Campaign Details  
activeCampaign.get_all_campaign_details()  







 




