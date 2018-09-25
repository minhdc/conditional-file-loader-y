from programy.utils.logging.ylogger import YLogger

from programy.context import ClientContext
from programy.clients.client import BotFactory
from programy.clients.client import BotClient
from conditionalfileloader.bot import CustomizedConditionalBot


class CustomizedConditionalBotFactory(BotFactory):
    def __init__(self, client, configuration):
        BotFactory.__init__(self,client, configuration)

    def load_bots(self,configuration):
        for config in configuration.configurations:
            bot = CustomizedConditionalBot(config, client=self._client)
            self._bots[bot.id] = bot

class CustomizedConditionalBotClient(BotClient):
    def __init__(self, id, argument_parser=None):
        BotClient.__init__(self, id, argument_parser=argument_parser)
        self._bot_factory = CustomizedConditionalBotFactory(self,self.configuration.client_configuration)

    