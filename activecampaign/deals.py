class Deals(object):

    def __init__(self, client):
        self.client = client

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

    def add_deal(self, title, value, pipeline, contact_id):
        data = {
            'title': title,
            'value': value,
            'currency': 'usd',
            'pipeline': pipeline,
            'contactid': contact_id
        }
        return self.client._post('deal_add', data)

    '''
        Available Fields to add a note to a deal
        note*   Text of the note. Example: 'Follow up about this deal soon'
        dealid* ID of the deal for the new deal note. Example: '31' (Get available deal IDs with "deal_list" call)
        owner   ID of the owner of the new deal note. Example: '4' (Get available owner IDs with "user_list" call)
    '''

    def add_deal_note(self, note, deal_id):
        data = {
            'note': note,
            'dealid': deal_id,
        }
        return self.client._post('deal_add', data)