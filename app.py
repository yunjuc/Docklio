#!/usr/bin/env python3
'''An app to interpret sms and execute the command'''
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
from subprocess import call 
 
app = Flask(__name__)
 
 
@app.route('/sms', methods=['POST'])
def sms():
    '''Parse receving message'''
    number = request.form['From']
    body = request.form['Body']
    

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, body))
    print(resp)
    return str(resp)

def deploy():
    '''Deploy container'''
    call('ls')
 
if __name__ == '__main__':
    app.run()
