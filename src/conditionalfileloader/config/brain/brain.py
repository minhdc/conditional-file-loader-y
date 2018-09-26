from programy.config.brain.brain import BrainConfiguration
from conditionalfileloader.config.brain.files import CustomizedConditionalBrainFilesConfiguration

class CustomizedConditionalBrainConfiguration(BrainConfiguration):
    def __init__(self,section_name="brain",topic_info="auto"):
        BrainConfiguration.__init__(self,section_name)
        self._files = CustomizedConditionalBrainFilesConfiguration(topic_info=topic_info)
        self._security = None

    def load_configuration(self, configuration_file, bot_root):
        brain_config = configuration_file.get_section(self.section_name)
        if brain_config is not None:
            self._overrides.load_config_section(configuration_file, brain_config, bot_root)
            self._defaults.load_config_section(configuration_file, brain_config, bot_root)
            self._nodes.load_config_section(configuration_file, brain_config, bot_root)

            self._binaries.load_config_section(configuration_file, brain_config, bot_root)
            self._braintree.load_config_section(configuration_file, brain_config, bot_root)
            self._files.load_config_section(configuration_file, brain_config, bot_root)

            self._services.load_config_section(configuration_file, brain_config, bot_root)
            self._security.load_config_section(configuration_file, brain_config, bot_root)
            self._oob.load_config_section(configuration_file, brain_config, bot_root)
            
            self._dynamics.load_config_section(configuration_file, brain_config, bot_root)
            self._tokenizer.load_config_section(configuration_file, brain_config, bot_root)