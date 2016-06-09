from slacksocket import SlackSocket

import json
import slacktools

token = slacktools.getSlackToken()
sc = SlackSocket(token, translate=True)

for event in sc.events():
    data = json.load(event.json)
    if ((data['type']) == "message"):
        if ((data['channel']) == "harrison-testing"):
            msg = (data['text'])
            # response with msg goes here
            print("Message found:  " + msg)

        else:
            print("Message is not on the right channel")
