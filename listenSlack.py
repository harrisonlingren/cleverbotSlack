from slackclient import SlackClient

token = "xoxp-37319837201-42485232481-49540458243-b109bbb8c6"
sc = SlackClient(token)

if sc.rtm_connect():
    while True:
        print sc.rtm_read()
        time.sleep(1)
else:
    print("Connection failed, invalid token?")
