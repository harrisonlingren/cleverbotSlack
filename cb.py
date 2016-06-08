from cleverbot import Cleverbot


class cb:
    def __init__(self):
        self.bot = {}

    def getResponse(self, memberid, message):
        try:
            if self.bot[memberid] is None:
                self.bot[memberid] = Cleverbot()
        except KeyError:
            self.bot[memberid] = Cleverbot()
        else:
            return self.bot[memberid].ask(message)

            # def respond(self, message, memberid):
            #    response = self.bot[memberid].ask(message)
            #    return response
