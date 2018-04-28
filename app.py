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
    if body == 'docker deploy' or body == 'Docker deploy':

        # execute deploymenet script
        status = os.system('./run')

        # confirm success for fail
        if status == 0:
            resp.message('Woohoo! Your app has been deployed.')
        else:
            resp.message('Your app is not deployed.')
    else:
        resp.message('Sorry, we cannot recognize the command.')

    # return response
    return str(resp)


if __name__ == '__main__':
    app.run()
