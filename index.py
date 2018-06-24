from flask import Flask, jsonify, request, abort

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
            print(entry['messaging'][0])
        return 'EVENT_RECEIVED', 200
    else:
        abort(404)


app.run(host='0.0.0.0', debug=True, port=1337)
