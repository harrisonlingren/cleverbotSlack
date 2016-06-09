import json
import time
from datetime import datetime
from slacksocket import SlackSocket

import slacktools
from cb import cb

token = slacktools.getSlackToken()
sc = SlackSocket(token, translate=True)
cleverbot = cb()

for event in sc.events():
    data = json.loads(event.json)
    if (data['type']) == "message":

        try:
            msg = (data['text'])
            readSuccess = True
        except KeyError:
            print("Error: Could not read message body")
            readSuccess = False

        if readSuccess:
            if "<@U1ES5EE1J>" in msg:
                if (data['channel']) == "xternsimulator":

                    msg = msg.replace('<@U1ES5EE1J>', '')
                    msg.replace('@cleverbot:', '')
                    msg = msg.replace('@cleverbot', '')
                    user = (data['user'])
                    rsp = str(cleverbot.getResponse(user, msg))
                    dateNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    finalString = "\nTime: '" + dateNow + "'\nMessage: '" + msg + "'\nUser: '" + user + "'\nBotResponse: '" + rsp + "'\nSent?: " + str(
                        ifSent.sent)
                    with open('./log.txt', 'a') as f:
                        f.write(finalString)

                    ifSent = sc.send_msg(rsp, channel_name="xternsimulator")

                    print(finalString)

                else:
                    print("Message is not on the right channel")
            else:
                print("Cleverbot not called in msg: " + msg)

    time.sleep(1)
