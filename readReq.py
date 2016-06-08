from bottle import Bottle, get, post, request, route, run, template
import json
from cb import toCleverbot

app = Bottle()

@app.route('/hello')
def hello():
	return "Test request received!"

@app.route('/cbSlack', method='POST')
def cbSlack():
	jsonResp = request.json
	# msgText = str(jsonResp['text'])
	strDump = json.dumps(jsonResp)
	print(strDump)

	with open('./log.txt', 'wb') as f:
		f.write(bytes(strDump,'UTF-8'))
	# print(msgText)
	# return toCleverbot(msgText)

run(app, host='10.0.0.100', port=8080, debug=True)

