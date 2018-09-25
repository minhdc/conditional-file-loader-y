from programy.brain import Brain
from conditionalfileloader.config.brain.brain import CustomizedConditionalBrainConfiguration

class CustomizedConditionalBrain(Brain):
    def __init__(self,bot,configuration: CustomizedConditionalBrainConfiguration):
        self._configuration = configuration