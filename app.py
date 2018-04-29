#!/usr/bin/env python3
'''An app to interpret sms and execute the command'''
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import os
import sys


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    '''Receive message and respond'''
    # get sms message body
    body = request.form['Body']

    # create response
    resp = MessagingResponse()

    # check command
    if body == 'docker start' or body == 'Docker start':
        # get container id by name
        status = os.system('docker start $(docker ps -a | grep p0bailey/docker-flask | head -1 | cut -d " " -f1)')
        if status == 0:
            resp.message('Woohoo! Your app has started.')
        else:
            resp.message('Your app is not started.')
    elif body == 'docker stop' or body == 'Docker stop':
        status = os.system('docker stop $(docker ps | grep p0bailey/docker-flask | head -1 | cut -d " " -f1)')
        if status == 0:
            resp.message('Your app has stopped.')
        else:
            resp.message('Sorry, operation failed.')

    else:
        resp.message('Sorry, we cannot recognize the command.')

    # return response
    return str(resp)


if __name__ == '__main__':
    app.run()
