import pytest
from activecampaign import activeCampaign

test_email = "test@testing.com"
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
base_url = "https://xxxxxxxxxxxx.api-us1.com"

def test_add_contact():
    activeCampaign.api_key = api_key
    activeCampaign.base_url = base_url
    add_contact = activeCampaign.add_contact(test_email, firstName="Test")
    response = add_contact
    print(response)

    assert (response) != None
    assert (response['result_code']) == 1
    assert (response['result_message']) == 'Contact added'


def test_delete_contact():
    activeCampaign.api_key = api_key
    activeCampaign.base_url = base_url
    response = activeCampaign.lookup_contact_by_email(test_email)
    id = response['id']
    delete_contact = activeCampaign.delete_contact("{}".format(id))
    response = delete_contact

    assert(response) != None
    assert (response['result_code']) == 1
    assert (response['result_message']) == 'Contact deleted'

