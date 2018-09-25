import logging
import datetime
import re

from programy.parser.aiml_parser import AIMLParser
from conditionalfileloader.utils.files.filefinder import FileFinder


class CustomizedConditionalAimlLoader(FileFinder):
    
    def __init__(self,aiml_parser):
        FileFinder.__init__(self)
        self._aiml_parser = aiml_parser

    #have to implement later
    def load_file_contents(self, id, filename, userid="*"):
        pass


class CustomizedConditionalAimlParser(AIMLParser):
    def __init__(self,brain):
        AIMLParser.__init__(self)
        

    def load_files_from_directory(self,configuration):
        
        start = datetime.datetime.now()
        totals_aimls_loaded = 0

        #customize this for conditional loading
        for file in configuration.files.aiml_files.files:
            aimls_loaded = self._aiml_loader.load_dir_contents()
            totals_aimls_loaded = len(aimls_loaded)