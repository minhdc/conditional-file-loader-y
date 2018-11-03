import os

from programy.utils.logging.ylogger import YLogger

from programy.utils.text.dateformat import DateFormatter
from conditionalfileloader.clients.events.console.client import CustomizedConditionalConsoleBotClient


class NewChatBot(CustomizedConditionalConsoleBotClient):
    def __init__(self, argument_parser=None):
        CustomizedConditionalConsoleBotClient.__init__(self, argument_parser)
 
    def parse_configuration(self):
        self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._file = \
            [os.path.dirname(__file__)]
        print("aaa:",os.path.dirname(__file__))

    def add_local_properties(self):
        client_context = self.create_client_context("console")
        client_context.brain.properties.add_property("name", "Customized chat bot")
        client_context.brain.properties.add_property("app_version", "1.0.0")
        client_context.brain.properties.add_property("grammar_version", "1.0.0")
        date_formatter = DateFormatter()
        client_context.brain.properties.add_property("birthdate", date_formatter.locate_appropriate_date_time())

    def display_basic_configuration(self):
        print("---CURRENT CONFIGURATION:-------")
        print("bot root? ",self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._file)
        print("aiml root location",self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._files)
        for each_file in os.listdir(self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._files[0]):
            if each_file.endswith('aiml'):
                print(each_file)
        print("Convo File: ",self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files)
        print("additional : ",self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._additionals)
        print("directories: ",self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._directories)
        print("errors: ",self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._errors)
        print("bot root : ",self.configuration.client_configuration.configurations[0]._bot_root)
        print("brain file config : ",self.configuration.client_configuration.configurations[0].configurations[0]._files._aiml_files._file)

if __name__ == '__main__':

    print ("Running Customized Chatbot with default options....")

    chatbot = NewChatBot()

    chatbot.add_local_properties()

    chatbot.display_basic_configuration()

    chatbot.run()
