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
    jsonResp = request.json
    msgText = str(jsonResp['text'])
    msgSender = str(jsonResp['member'])  # fix this to include correct params for member
    strDump = json.dumps(jsonResp)

    with open('./log.txt', 'wb') as f:
        f.write(bytes(strDump, 'UTF-8'))
    # print(msgText)

    cbInstance = cleverbot.getCb(msgSender)
    msgResponse = cbInstance.respond(msgText)

    print(msgResponse)
    return msgResponse


run(app, host='10.0.0.100', port=8080, debug=True)
