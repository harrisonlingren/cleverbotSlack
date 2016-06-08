import json
from bottle import Bottle, request, run

from cb import cb

app = Bottle()
cleverbot = cb()


@app.route('/hello')
def hello():
    return "Test request received!"


@app.route('/slackbot', method='POST')
def slackbot():
    if request.json is not None:
        msgText = str(request.json['text'])
        msgSender = str(request.json['member'])  # fix this to include correct params for member
    else:
        print("Could not read text")
        msgText = "Could not read text"
        print("Could not get member id")
        msgSender = "blank"
        return msgText

    strDump = json.dumps(request.json)

    with open('./log.txt', 'wb') as f:
        f.write(bytes(strDump, 'UTF-8'))
    # print(msgText)
    print("\n" + strDump)

    cbInstance = cleverbot.getBot(msgSender)
    msgResponse = cleverbot.getBot(msgSender).ask(msgText)
    msgResponse2 = cbInstance.ask(msgText)

    print(msgResponse, msgResponse2)
    return msgResponse


run(app, host='10.0.0.100', port=8080, debug=True)
