from programy.config.brain.brain import BrainConfiguration
from conditionalfileloader.config.brain.files import CustomizedConditionalBrainFilesConfiguration

class CustomizedConditionalBrainConfiguration(BrainConfiguration):
    def __init__(self,section_name="brain",topic_info="auto"):
        self._files = CustomizedConditionalBrainFilesConfiguration(topic_info=topic_info)