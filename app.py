import os

from flask import Flask, request
from fbmessenger import BaseMessenger
from fbmessenger import elements


class Messenger(BaseMessenger):
    def message(self, message):
        element = elements.Text('Received: {0}'.format(message['message']['text']))
        self.send(element.to_dict())

    def delivery(self, message):
        pass

    def read(self, message):
        pass

    def account_linking(self, message):
        pass

    def postback(self, message):
        pass

    def optin(self, message):
        pass


app = Flask(__name__)
messenger = Messenger(os.environ.get('FB_PAGE_TOKEN'))


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == \
                os.environ.get('FB_VERIFY_TOKEN'):
            return request.args.get('hub.challenge')
        return 'FB_VERIFY_TOKEN does not match.', 400
    elif request.method == 'POST':
        messenger.handle(request.get_json(force=True))
    return ''


@app.route('/')
def hello_world():
    return 'Hello, World!'
