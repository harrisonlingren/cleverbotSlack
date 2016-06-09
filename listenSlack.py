from slacksocket import SlackSocket

import slacktools

token = slacktools.getSlackToken()
sc = SlackSocket(token, translate=True)

for event in sc.events():
    if (str(event.json['type']) == "message"):
        if (str(event.json['channel']) == "harrison-testing"):
            msg = str(event.json['text'])
            # response with msg goes here
            print("Message found:  " + msg)

        else:
            print("Message is not on the right channel")
