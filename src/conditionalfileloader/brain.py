from programy.utils.logging.ylogger import YLogger
from programy.brain import Brain
from conditionalfileloader.config.brain.brain import CustomizedConditionalBrainConfiguration

class CustomizedConditionalBrain(Brain):
    def __init__(self,bot,configuration: CustomizedConditionalBrainConfiguration):
        print("initing CustomizedConditionalBrain")
        YLogger.info(self,"initning CustomizedConditionalBrain")
        Brain.__init__(self,bot,configuration)
        self._configuration = configuration
        self._authentication = None
        self._authorisation = None
        