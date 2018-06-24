import sys
import os
import requests
import json

FB_MESSENGER_ENDPOINT = 'https://graph.facebook.com/v2.6/me/messages'

def send_message(page_token, sender_psid, message):
    body = {
        'recipient': {
            'id': str(sender_psid)
        },
        'message': { 'text': message },
    }
    r = requests.post(
        FB_MESSENGER_ENDPOINT,
        headers={'content-type': 'application/json'},
        params={'access_token':page_token},
        data=json.dumps(body),
    )
    print(r.text)
