from cleverbot import Cleverbot


class cb:
    cb = {}
    cb['blank'] = Cleverbot()

    def getCb(self, memberid):
        if self.cb[memberid] is not None:
            return self
        else:
            self.cb[memberid] = Cleverbot()
            return self

    def respond(self, message, memberid):
        response = self.cb[memberid].ask(message)
        return response
