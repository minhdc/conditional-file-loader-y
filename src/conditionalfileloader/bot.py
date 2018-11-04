import logging 
import os

from programy.utils.logging.ylogger import YLogger

from programy.bot import Bot,BrainFactory

from conditionalfileloader.config.brain.brain import CustomizedConditionalBrainConfiguration
from conditionalfileloader.brain import CustomizedConditionalBrain


class CustomizedConditionalBrainFactory(BrainFactory):
    def __init__(self,bot):
        print("initin brains...")        
        BrainFactory.__init__(self,bot)
        

    def load_brains(self, bot): 
        print("loading brains.........")
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

        #customizing###########################################      
        
        if 'topic' in question.combine_sentences().lstrip():
            print("changing topic to fit quest...")
            #self._brain_factory.brain('brain')._aiml_parser._topic = question.combine_sentences().lstrip()
            
            #for each_file in os.listdir(self.configuration.configurations[0].files.aiml_files._files[0]):
            #    if each_file.endswith('aiml'):        
            #        file_loc = os.path.join(self.configuration.configurations[0].files.aiml_files._files[0],each_file)
            #        self._brain_factory.brain('brain')._aiml_parser._aiml_loader.load_file_contents('brain',file_loc)
            print("aiml reparsed")


         

        
        YLogger.info(self,question)
        
        #print("this is current topic: ",self._topic.combine_sentences())
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


    