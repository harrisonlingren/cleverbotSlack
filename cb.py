from cleverbot import Cleverbot


class cb:
    cb = {}

    def __init__(self):
        self.cb['blank'] = Cleverbot()

    def getCb(memberid):
        if cb[memberid] is not None:
            return cb[memberid]
        else:
            cb[memberid] = Cleverbot()
            return cb[memberid]

    def respond(message, memberid):
        response = cb[memberid].ask(message)
        return response
