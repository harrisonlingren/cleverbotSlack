import json
from slacksocket import SlackSocket

import slacktools
from cb import cb

token = slacktools.getSlackToken()
sc = SlackSocket(token, translate=True)
cleverbot = cb()

for event in sc.events():
    data = json.loads(event.json)
    if ((data['type']) == "message"):
        if ((data['channel']) == "harrison-testing"):

            msg = (data['text'])
            rsp = cleverbot.getResponse(msgSender, msgText)

            finalString = "Message: " + msg + "\nResponse: " + rsp + "\n"
            with open('./log.txt', 'wb') as f:
                f.write(bytes(finalString, 'UTF-8'))

            print(finalString)

        else:
            print("Message is not on the right channel")
