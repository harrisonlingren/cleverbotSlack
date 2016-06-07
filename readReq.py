from bottle import Bottle, get, post, request, route, run, template
import json
from MemeBot import MemeBot

app = Bottle()

@app.route('/hello')
def hello():
	return "Test request received!"

@app.route('/groupyBot', method='POST')
def groupyBot():
	jsonResp = request.json
	msgText = str(jsonResp['text'])
	strDump = json.dumps(jsonResp)
	
	with open('./log.txt', 'wb') as f:
		f.write(bytes(strDump,'UTF-8'))
	# print(msgText)
	return MemeBot(msgText)

run(app, host='192.168.1.115', port=8080, debug=True)

