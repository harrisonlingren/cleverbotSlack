import json
import time
from datetime import datetime
from slacksocket import SlackSocket

import slacktools
from cb import cb


# detect message in channel and get/post response, return final string
def respondToMessage(m, d):
    if (d['channel']) == "xternsimulator":

        m = m.replace('<@U1ES5EE1J>', '')
        m.replace('@cleverbot:', '')
        m = m.replace('@cleverbot', '')
        user = (d['user'])
        rsp = str(cleverbot.getResponse(user, m))
        dateNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        ifSent = sc.send_msg(rsp, channel_name="xternsimulator")

        finalString = "\nTime: '" + dateNow + "'\nMessage: '" + m \
                      + "'\nUser: '" + user + "'\nBotResponse: '" + \
                      rsp + "'\nSent?: " + str(ifSent.sent)
        return finalString

    else:
        print("Message is not on the right channel")
        return "ERROR: message is not on channel:'xternsimulator'"


# Main method
def go():
    for event in sc.events():
        data = json.loads(event.json)
        if (data['type']) == "message":

            try:
                msg = (data['text'])
                readSuccess = True
            except KeyError:
                print("  <KeyError> Error while reading message body")
                readSuccess = False

            if readSuccess:
                if "<@U1ES5EE1J|cleverbot>" in msg:
                    output = respondToMessage(msg, data)
                    output += "\nSUCCESS:  Got message and responded!\n"
                elif "<@U1ES5EE1J>" in msg:
                    output = respondToMessage(msg, data)
                    output += "\nSUCCESS:  Got message and responded!\n"
                else:
                    output = "\nERROR: Cleverbot not called in msg: " + msg
                    print(output)
            else:
                output = "\nERROR:: Could not read message body. Cleverbot might " \
                         "have been mentioned by a status change\n"
            # Logging
            with open('./log.txt', 'a') as f:
                f.write(output)

        time.sleep(1)


# -------------------------------------------------------------------

# START IT!
token = slacktools.getSlackToken()
sc = SlackSocket(token, translate=True)
cleverbot = cb()

go()
