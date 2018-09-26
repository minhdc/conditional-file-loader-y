from programy.utils.logging.ylogger import YLogger

from conditionalfileloader.clients.client import CustomizedConditionalBotClient

class CustomizedConditionalEventBotClient(CustomizedConditionalBotClient):
    def __init__(self, id, argument_parser=None):
        #self._running = False
        CustomizedConditionalBotClient.__init__(self, id, argument_parser=argument_parser)

    def prior_to_run_loop(self):
        print("starting run loop....")
        YLogger.info(self,"starting runloop")
        pass

    def run_loop(self):
        self._running = True
        while self._running is True:
            self._running = self.wait_and_answer()

    def wait_and_answer(self):
        raise NotImplementedError("Must customized this...")

    def post_run_loop(self):
        print("stopping run loop....")
        YLogger.info(self,"stopping runloop")
        pass

    def run(self):
    
        if self.arguments.noloop is False:
            YLogger.info(self, "Entering conversation loop...")

            self.prior_to_run_loop()

            self.run_loop()

            self.post_run_loop()

        else:
            YLogger.debug(self, "noloop set to True, exiting...")