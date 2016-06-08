from cleverbot import Cleverbot


class cb:
    def __init__(self, memberid, cb):
        bot = {}

    def getBot(self, memberid):
        if self.bot[memberid] is not None:
            return self
        else:
            self.bot[memberid] = Cleverbot()
            return self

    def respond(self, message, memberid):
        response = self.bot[memberid].ask(message)
        return response
