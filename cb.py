from cleverbot import Cleverbot

forMember = ''
cb = {}


def __init__(self):
    self.forMember = ''
    self.cb['blank'] = Cleverbot()


def __init__(self, memberid):
    self.forMember = memberid
    self.cb[memberid] = Cleverbot()


def getCb(memberid):
    if cb[memberid] is not None:
        return cb[memberid]
    else:
        return cb['blank']


def respond(message, memberid):
    response = cb[memberid].ask(message)
    return response
