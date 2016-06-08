from cleverbot import Cleverbot


class cb:
    cb = {}
    cb['blank'] = Cleverbot()

    def getCb(self, memberid):
        if cb[memberid] is not None:
            return cb[memberid]
        else:
            cb[memberid] = Cleverbot()
            return cb[memberid]

    def respond(self, message, memberid):
        response = cb[memberid].ask(message)
        return response
