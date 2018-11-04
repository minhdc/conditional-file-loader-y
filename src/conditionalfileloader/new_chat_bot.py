import os

from programy.utils.logging.ylogger import YLogger

from programy.utils.text.dateformat import DateFormatter
from conditionalfileloader.clients.events.console.client import CustomizedConditionalConsoleBotClient
from conditionalfileloader.bot import CustomizedConditionalBot
from programy.config.bot.bot import BotConfiguration

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
        print(self.get_description())
        print(self.get_client_configuration())
        print(self._bot_factory._bots['bot']._brain_factory.brain('brain')._aiml_parser._topic)

    #customized
    def get_answer(self,input_text):
        result = self._bot_factory._bots['bot'].ask_question(client.create_client_context("console"),input_text)
        return result

if __name__ == '__main__':

    print ("Running Customized Chatbot with default options....")

    #client = NewChatBot()
        
    #print(client.get_answer(" tại sao phải đăng kí tín"))
    #print(client.get_answer("talk topic9"))
    #print(client.get_answer(" tại sao phải đăng kí tín"))
    
    
    

    #print(bot)

    #chatbot = NewChatBot()

    #chatbot.add_local_properties()

    #chatbot.display_basic_configuration()

    #chatbot.run()
