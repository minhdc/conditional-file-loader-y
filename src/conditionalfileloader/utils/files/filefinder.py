import os


from programy.utils.files.filefinder import FileFinder

class CustomizedConditionalFileFinder(FileFinder):
    def __init__(self):
        pass
    
    #have to implement
    def load_file_contents(self,id,filename,userid="*"):
        pass


    def find_files(self, path, subdir=False, extension=None):
        
        found_files = []

        try:
            if subdir is False:
                paths = os.listdir(path)
                for filename in paths:
                    if filename.endswith(extension):
                        found_files.append(filename,os.path.join(path,filename))
        except FileNotFoundError:
            YLogger.error(self, "No directory found [%s]", path)


    
    def load_dir_contents(self, paths, subdir=False, extension=".txt", filename_as_userid=False):
        files = self.find_files(paths,subdir,extension)