class Contacts(object):

    def __init__(self, client):
        self.client = client

    '''
        Available Fields to Create a Contact
        first_name  First name of the contact. Example: 'FirstName'
        last_name Last name of the contact. Example: 'LastName'
        phone Phone number of the contact. Example: '+1 312 201 0300'
        orgname Organization name (if doesn't exist, this will create a new organization) - MUST HAVE CRM FEATURE FOR THIS.
        tags  Tags for this contact (comma-separated). Example: "tag1, tag2, etc"
        ip4 IP address of the contact. Example: '127.0.0.1' If not supplied, it will default to '127.0.0.1'
        field[345,0]  Custom field values. Example: field[345,0] = 'value'. In this example, "345" is the field ID. Leave 0 as is.
        field[%PERS_1%,0] 'value' (You can also use the personalization tag to specify which field you want updated)
        p[123]* Assign to lists. List ID goes in brackets, as well as the value.
        status[123] The status for each list the contact is added to. Examples: 1 = active, 2 = unsubscribed
        form  Optional subscription Form ID, to inherit those redirection settings. Example: 1001. This will allow you to mimic adding the contact through a subscription form, where you can take advantage of the redirection settings.
        noresponders[123] Whether or not to set "do not send any future responders." Examples: 1 = yes, 0 = no.
        sdate[123]  Subscribe date for particular list - leave out to use current date/time. Example: '2009-12-07 06:00:00'
        instantresponders[123]  Use only if status = 1. Whether or not to set "send instant responders." Examples: 1 = yes, 0 = no.
        lastmessage[123]  Whether or not to set "send the last broadcast campaign." Examples: 1 = yes, 0 = no.
    '''

    def add(self, data):
        if 'email' not in data:
            raise KeyError('The contact must have an email')
        return self.client._post("contact_add", data)

    def edit(self, data):
        additional_data = [('overwrite', 0),]
        return self.client._post("contact_edit", data, additional_data)

    def delete(self, id):
        additional_data = [('id', id),]
        return self.client._get('contact_delete', additional_data)

    def lookup_by_email(self, email):
        additional_data = [('email', email),]
        return self.client._get('contact_view_email', additional_data)

    def add_note(self, list_id, email, note):
        try:
            contact = lookup_by_email(email)
            contact_id = contact['id']
        except:
            print("Error Finding Contact in Active Campaign")
            return "Error Finding Contact in Active Campaign"

        additional_data = [
            ('id', contact_id),
            ('listid', list_id),
            ('note', note),
        ]
        return self.client._post('contact_note_add', additional_data)

    def add_tag(self, email, tags):
        aditional_data = [
            ('email', email),
            ('tags', tags),
        ]
        return self.client._post('contact_tag_add', aditional_data)

    def remove_tag(self, email, tags):
        aditional_data = [
            ('email', email),
            ('tags', tags),
        ]
        return self.client._post('contact_tag_remove', aditional_data)
