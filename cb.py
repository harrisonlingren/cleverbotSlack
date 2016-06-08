from cleverbot import Cleverbot


class cb:
    cb = {}
    cb['blank'] = Cleverbot()

    def getCb(self, memberid):
        if self.cb[memberid] is not None:
            return cb[memberid]
        else:
            self.cb[memberid] = Cleverbot()
            return self.cb[memberid]

    def respond(self, message, memberid):
        response = self.cb[memberid].ask(message)
        return response
