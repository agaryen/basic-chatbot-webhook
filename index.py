import argparse
from flask import Flask, jsonify, request, abort
from helpers import send_message

parser = argparse.ArgumentParser()
parser.add_argument('token')
args = parser.parse_args()

app = Flask(__name__)

@app.route('/webhook', methods=['GET'])
def webhookGET():
    token = 'testinginprogress0'

    arg_mode = request.args.get('hub.mode')
    arg_token = request.args.get('hub.verify_token')
    arg_challenge = request.args.get('hub.challenge')

    if arg_mode is not None and arg_token is not None:
        if arg_mode == 'subscribe' and arg_token == token:
            print('Token verified')
            return arg_challenge, 200
        else:
            abort(403)

@app.route('/webhook', methods=['POST'])
def webhookPOST():
    body = request.get_json()

    if body['object'] == 'page':
        for entry in body['entry']:
            event = entry['messaging'][0]
            try:
                send_message(args.token, event['sender']['id'], 'Hello ! You sent: "%s"' % event['message']['text'])
            except KeyError:
                pass
        return 'EVENT_RECEIVED', 200
    else:
        abort(404)


app.run(host='0.0.0.0', debug=True, port=1337)
