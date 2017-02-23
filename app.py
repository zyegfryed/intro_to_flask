import os

from flask import Flask, request
from fbmessenger import BaseMessenger
from redis import StrictRedis
from rq.decorators import job


class Messenger(BaseMessenger):
    def message(self, message):
        self.send({'text': 'Received: {0}'.format(message['message']['text'])})

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
redis = StrictRedis()


@job('default', connection=redis)
def messenger_handle(message):
    messenger.handle(message)


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        if request.args.get('hub.verify_token') == \
                os.environ.get('FB_VERIFY_TOKEN'):
            return request.args.get('hub.challenge')
        return 'FB_VERIFY_TOKEN does not match.', 400
    elif request.method == 'POST':
        messenger_handle.delay(request.get_json(force=True))
    return ''


@app.route('/')
def hello_world():
    return 'Hello, World!'
