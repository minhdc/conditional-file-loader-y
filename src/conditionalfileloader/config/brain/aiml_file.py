from programy.utils.logging.ylogger import YLogger

from programy.config.brain.debugfile import DebugFileConfiguration
from programy.config.brain.aiml_file import BrainAIMLFileConfiguration

class CustomizedConditionalBrainAIMLFileConfiguration(BrainAIMLFileConfiguration):
    def __init__(self, name="aiml", topic_info = "auto"):
        BrainAIMLFileConfiguration.__init__(self,name)
        self._topic_info = topic_info

    @property
    def topic_info(self):
        return self._topic_info

    
    #customize by filtering the returnefd list from get_multi_file_option
    def load_config_section(self,configuration_file,configuration,bot_root):
        files_config = configuration_file.get_option(configuration,self.section_name)

        if files_config is not None:
            files = configuration_file.get_multi_file_option(files_config,'files',bot_root)
            if files is not None and files:
                filtered_files = []
                
                #customizing here....
                for each_file in files:
                    if each_file.endswith(self._topic_info):
                        filtered_files.append(each_file)

                self._files = filtered_files
                self._extension = configuration_file.get_option(files_config,"extension")
                self._directories = configuration_file.get_option(files_config,"directories")
            else:
                file = configuration_file.get_option(files_config,"file")
                if file is not None:
                    self._file = self.sub_bot_root(file,bot_root)
            self._errors = self.get_debug_file_configuration(configuration_file, files_config, "errors", bot_root)
            self._duplicates = self.get_debug_file_configuration(configuration_file, files_config, "duplicates", bot_root)
            self._conversation = self.get_debug_file_configuration(configuration_file, files_config, "conversation", bot_root)

        else:
            YLogger.warning(self, "'%s' section missing from bot config, using to defaults", self.section_name)

    def get_debug_file_configuration(self, configuration_file, files_config, debug_name, bot_root):
        keys = configuration_file.get_keys(files_config)
        if debug_name in keys:
            section = configuration_file.get_section(debug_name, files_config)
            if configuration_file.is_string(section):
                debug_config = configuration_file.get_option(files_config, debug_name, missing_value=None)
                if debug_config is not None:
                    filename = self.sub_bot_root(debug_config, bot_root)
                    return DebugFileConfiguration(debug_name, filename=filename)
            else:
                debug_file = DebugFileConfiguration(debug_name)
                debug_file.load_config_section(configuration_file, files_config, bot_root)
                return debug_file
        return None
