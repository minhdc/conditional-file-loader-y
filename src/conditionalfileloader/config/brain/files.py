from programy.config.brain.files import BrainFilesConfiguration
from programy.config.brain.file import BrainFileConfiguration
from conditionalfileloader.config.brain.aiml_file import CustomizedConditionalBrainAIMLFileConfiguration

class CustomizedConditionalBrainFilesConfiguration(BrainFilesConfiguration):
    def __init__(self,topic_info="auto"):
        BrainFilesConfiguration.__init__(self,"files") #files = section name in yaml file
        self._aiml_files = CustomizedConditionalBrainAIMLFileConfiguration(topic_info=topic_info)
    