from programy.utils.logging.ylogger import YLogger

from conditionalfileloader.clients.client import CustomizedConditionalBotClient

class CustomizedConditionalEventBotClient(CustomizedConditionalBotClient):
    def __init__(self, id, argument_parser=None):
        #self._running = False
        CustomizedConditionalBotClient.__init__(self, id, argument_parser=argument_parser)

    def run_loop(self):
        self._running = True
        while self._running is True:
            self._running = self.wait_and_answer()

    def run(self):
    
        if self.arguments.noloop is False:
            YLogger.info(self, "Entering conversation loop...")

            self.prior_to_run_loop()

            self.run_loop()

            self.post_run_loop()

        else:
            YLogger.debug(self, "noloop set to True, exiting...")