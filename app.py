from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

BASE_URL = os.environ['MAILGUN_BASE_URL']
DOMAIN = os.environ['MAILGUN_DOMAIN']
API_KEY = os.environ['MAILGUN_API_KEY']
TO_EMAIL = os.environ['MAILGUN_TO_EMAIL']

MAILGUN_URL = '{}/{}/messages'.format(BASE_URL, DOMAIN)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/send-email', methods=['POST'])
def send_email():
    FROM_EMAIL = request.json['from']
    SUBJECT = request.json['subject']
    MESSAGE = request.json['text']
    DATA = {
        'from': FROM_EMAIL,
        'to': TO_EMAIL,
        'subject': SUBJECT,
        'text': MESSAGE
    }
    r = requests.post(MAILGUN_URL, data=DATA, auth=('api', API_KEY))
    data = r.json()
    return jsonify(data)
