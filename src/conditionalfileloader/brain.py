from programy.utils.logging.ylogger import YLogger
from programy.brain import Brain
from conditionalfileloader.config.brain.brain import CustomizedConditionalBrainConfiguration
from conditionalfileloader.parser.aiml_parser import CustomizedConditionalAimlParser

class CustomizedConditionalBrain(Brain):
    def __init__(self,bot,configuration: CustomizedConditionalBrainConfiguration):
        print("initing CustomizedConditionalBrain")
        YLogger.info(self,"initning CustomizedConditionalBrain")
        Brain.__init__(self,bot,configuration)
        self._bot=bot
        self._configuration = configuration        
        self._authentication = None
        self._authorisation = None
        self._aiml_parser = self.load_aiml_parser()

        
    def load_aiml_parser(self):
        YLogger.info("loading customized aiml parser")
        print("loading customized aiml parser")
        return CustomizedConditionalAimlParser(self) 