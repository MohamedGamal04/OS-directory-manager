from os import listdir, makedirs
from shutil import move
from typing import List
from Filename_Extension_Dictionarie import filename_extension_dictionarie


def FOmain(gui_paths: List[str]):
    paths = gui_paths
    instance = []
    num_of_instance = len(paths)
    for i in zip(range(num_of_instance), paths):
        instance.append(i[0])
        instance[i[0]] = FileOrgnizer(i[1])
    for i in range(num_of_instance):
        instance[i].explore_path().categorization().make_dirs().move_files()
    for i in range(num_of_instance):
        instance.clear()


class FileOrgnizer(object):
    """
        This class is used to organize different files by moving them into different directories
    """

    def __init__(self, path) -> None:
        self.extensions = []
        self.files = []
        self.dir_names = []
        path =path.replace("/","\\")
        self.path = path
        

    def explore_path(self) -> None:
        """
            this function is used to explore the chosen path and record the file and it's extension
        """
        try:
            for file_name in listdir(path=self.path):
                if (file_name.rfind(".") != -1):
                    self.extensions.append(file_name[file_name.rfind(".")+1:])
                    self.files.append([file_name, self.extensions[-1]])
            return self
        except FileNotFoundError:
            return self

    def categorization(self) -> None:
        """
            this function is used to categorize each file extension e.g(png -> Photos)
        """
        for key, value in filename_extension_dictionarie.items():
            for _ in self.extensions:
                if _ in key:
                    self.dir_names.append(value)
        self.dir_names = set(self.dir_names)
        return self

    def make_dirs(self) -> None:
        """
             this function is used to make directories to move the files with the same category into it
        """
        for dir_name in self.dir_names:
            makedirs(f"{self.path}\\{dir_name}", exist_ok=True)
        return self

    def move_files(self) -> None:
        """
             this function is used to move the files
        """
        for file in self.files:
            for key, value in filename_extension_dictionarie.items():
                if file[1] in key:
                    file.append(value)
            move(f"{self.path}\\{file[0]}", f"{self.path}\\{file[2]}")
        return self
