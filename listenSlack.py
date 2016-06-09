import time
from slackclient import SlackClient
import slacktools

token = slacktools.getSlackToken()
sc = SlackClient(token)

if sc.rtm_connect():
    while True:
        print(sc.rtm_read())
        time.sleep(1)
else:
    print("Connection failed, invalid token?")
