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

    def __init__(self, config: CustomizedConditionalBrainConfiguration , client=None):
        Bot.__init__(self, config, client)
        self._brain_factory = CustomizedConditionalBrainFactory(self)
