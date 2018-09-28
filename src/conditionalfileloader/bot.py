import logging 
import os

from programy.utils.logging.ylogger import YLogger

from programy.bot import Bot,BrainFactory

from conditionalfileloader.config.brain.brain import CustomizedConditionalBrainConfiguration
from conditionalfileloader.brain import CustomizedConditionalBrain

class CustomizedConditionalBrainFactory(BrainFactory):
    def __init__(self,bot):
        BrainFactory.__init__(self,bot)

    def load_brains(self, bot):
        for config in bot.configuration.configurations:
            brain = CustomizedConditionalBrain(bot,config)
            self._brains[brain.id] = brain

class CustomizedConditionalBot(Bot):

    def __init__(self, config: CustomizedConditionalBrainConfiguration, client=None):
        Bot.__init__(self, config, client)
        self._brain_factory = CustomizedConditionalBrainFactory(self)
        self._topic = "auto" #EDIT THIS@!!!!!Initial step

    @property
    def topic(self):
        return self._topic

    
    def ask_question(self, client_context, text, srai=False, responselogger=None):

        if srai is False:
            client_context.bot = self
            client_context.brain = client_context.bot.brain

        client_context.mark_question_start(text)

        pre_processed = self.pre_process_text(client_context, text, srai)

        question = self.get_question(client_context, pre_processed, srai)

        #temporary##########################################
        self._topic = question
        print(question.combine_sentences())
        print("current config for aiml: ",self.configuration.configurations[0].files.aiml_files._files)
        self.configuration.configurations[0].files.aiml_files._files[0] = os.path.join(self.configuration.configurations[0].files.aiml_files._files[0],self._topic.combine_sentences())
        print("modified config for aiml: ",self.configuration.configurations[0].files.aiml_files._files)
        YLogger.info(self,question)
        #########################################################

        conversation = self.get_conversation(client_context)

        conversation.record_dialog(question)

        answers = []
        sentence_no = 0
        for sentence in question.sentences:
            question.set_current_sentence_no(sentence_no)
            answer = self.process_sentence(client_context, sentence, srai, responselogger)
            answers.append(answer)
            sentence_no += 1

        client_context.reset_question()

        if srai is True:
            conversation.pop_dialog()

        response = self.combine_answers(answers)

        self.log_question_and_answer(client_context, text, response)

        return response
