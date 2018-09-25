import os

from programy.utils.logging.ylogger import YLogger

#from programy.clients.events.client import EventBotClient
from programy.clients.events.console.config import ConsoleConfiguration
from programy.utils.text.dateformat import DateFormatter
from conditionalfileloader.clients.events.console.client import CustomizedConditionalConsoleBotClient


class NewChatBot(CustomizedConditionalConsoleBotClient):
    def __init__(self, argument_parser=None):
        CustomizedConditionalConsoleBotClient.__init__(self, argument_parser)
 
    def parse_configuration(self):
        self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._files = \
            [os.path.dirname(__file__)]

    def add_local_properties(self):
        client_context = self.create_client_context("console")
        client_context.brain.properties.add_property("name", "ProgramY")
        client_context.brain.properties.add_property("app_version", "1.0.0")
        client_context.brain.properties.add_property("grammar_version", "1.0.0")
        date_formatter = DateFormatter()
        client_context.brain.properties.add_property("birthdate", date_formatter.locate_appropriate_date_time())

if __name__ == '__main__':

    print ("Running ProgramY Chatbot with default options....")

    chatbot = NewChatBot()

    chatbot.add_local_properties()

    chatbot.run()
