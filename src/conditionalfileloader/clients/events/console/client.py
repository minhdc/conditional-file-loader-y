from programy.utils.logging.ylogger import YLogger

from conditionalfileloader.clients.events.client import CustomizedConditionalEventBotClient
from programy.clients.events.console.config import ConsoleConfiguration

class CustomizedConditionalConsoleBotClient(CustomizedConditionalEventBotClient):
    def __init__(self, argument_parser=None):
        #self.running=False
        CustomizedConditionalEventBotClient.__init__(self, 'console',argument_parser)

    def get_description(self):
        return "Customized Console Client"

    def get_client_configuration(self):
        return ConsoleConfiguration()

    def add_client_arguments(self,parser=None):
        return

    def parse_args(self, arguments, parse_args):
        return
    
    def get_question(self, client_context, input_func=input):
        ask = "%s " % self.get_client_configuration().prompt
        return input_func(ask)
    
    def display_startup_messages(self, client_context):
        self.process_response(client_context, client_context.bot.get_version_string(client_context))
        initial_question = client_context.bot.get_initial_question(client_context)
        self._renderer.render(client_context, initial_question)

    def process_question(self, client_context, question):
        # Returns a response
        return client_context.bot.ask_question(client_context , question, responselogger=self)

    def render_response(self, client_context, response):
        # Calls the renderer which handles RCS context, and then calls back to the client to show response
        self._renderer.render(client_context, response)

    def process_response(self, client_context, response):
        print(response)

    def process_question_answer(self, client_context):
        question = self.get_question(client_context)
        response = self.process_question(client_context, question)
        self.render_response(client_context, response)

    def wait_and_answer(self):
        running = True
        try:
            client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
            self.process_question_answer(client_context)
        except KeyboardInterrupt as keye:
            running = False
            client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
            self._renderer.render(client_context, client_context.bot.get_exit_response(client_context))
        except Exception as e:
            YLogger.exception(self, "Oops something bad happened !", e)
        return running

    def prior_to_run_loop(self):
        client_context = self.create_client_context(self._configuration.client_configuration.default_userid)
        self.display_startup_messages(client_context)

    


if __name__ == '__main__':

    def run():
        print("Loading, please wait...")
        console_app = CustomizedConditionalConsoleBotClient()
        console_app.run()

    run()

