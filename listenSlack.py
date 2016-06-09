import json
from datetime import datetime
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
            user = (data['user'])
            rsp = str(cleverbot.getResponse(user, msg))
            dateNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            finalString = "Time: '" + dateNow + "'\nMessage: '" + msg + "'\nUser: '" + user + "'\nBotResponse: '" + rsp + "'\n"
            with open('./log.txt', 'a') as f:
                f.write(finalString)

            ifSent = sc.send_msg(rsp, channel_name="harrison-testing")

            print(finalString + "\nSent?: " + ifSent.sent)

        else:
            print("Message is not on the right channel")
