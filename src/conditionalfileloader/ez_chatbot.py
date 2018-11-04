import os

from programy.utils.text.dateformat import DateFormatter

from programy.utils.logging.ylogger import YLogger
from programy.clients.events.console.client import ConsoleBotClient


class EzChatBot(ConsoleBotClient):
    def __init__(self, arg_parser=None):
        ConsoleBotClient.__init__(self,arg_parser)

    def parse_configuration(self):
        self.configuration.client_configuration.configurations[0].configurations[0].files.aiml_files._file=\
        [os.path.dirname(__file__)]
        print("parsed configuration at : ",os.path.dirname(__file__))

    def add_local_properties(self):
        client_context = self.create_client_context('console')
        client_context.brain.properties.add_property('name','EZ chatbot')
        client_context.brain.properties.add_property('app_version','0.0.1')
        client_context.brain.properties.add_property('grammar_version','0.0.1')
        date_formatter = DateFormatter()
        client_context.brain.properties.add_property('birthday',date_formatter.locate_appropriate_date_time())
        

    def display_basic_configuration(self):
        print("---CURRENT CONFIGURATION:-------")
        print(self.get_description())
        print(self.get_client_configuration())
        print(self._bot_factory._bots['bot']._brain_factory.brain('brain')._aiml_parser._topic)

        '''
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
        '''
    

if __name__ == '__main__':
    
    ez_chatbot = EzChatBot()
    
    ez_chatbot.add_local_properties()

    ez_chatbot.display_basic_configuration()

    ez_chatbot.run()
        
