import os
import shutil


def EFD(gui_path, nested_bool, NF_only_bool):
    path = gui_path[0]
    path = path.replace("/", "\\")
    Newfolder_only = NF_only_bool
    Nested = nested_bool
    instance = EmptyFolderDeleter(path, Nested, Newfolder_only)
    if Nested is True:
        instance.Nest_check().Deleter()
    else:
        instance.Deleter()


class EmptyFolderDeleter(object):
    def __init__(self, path, Nested, Newfolder_only) -> None:
        """
            This class is used to delete empty folders whether it was nested or not
        """
        self.gen = os.walk(path)
        self.path = path
        self.Nested = Nested
        self.Newfolder_only = Newfolder_only

    def Nest_check(self) -> None:
        """
            this function is used when it's nested is enabled
        """
        while self.Nested:
            self.flag = False
            for source, dir, file in self.gen:
                if self.Newfolder_only == True:
                    con = source.find("New folder") != -1
                else:
                    con = True
                if (dir == [] and file == [] and con):
                    self.flag = True
                    shutil.rmtree(source)
                    self.gen = os.walk(self.path)
                    break
                continue
            if self.flag == False:
                break
        return self

    def Deleter(self) -> None:
        """
            this function is used to delete empty folders whether it's "New folders" only or not
        """
        for source, dir, file in self.gen:
            if self.Newfolder_only == True:
                con = source.find("New folder") != -1
            else:
                con = True
            if (dir == [] and file == [] and con):
                if len(source.partition(self.path)[2].split("\\")) <= 2:
                    shutil.rmtree(source)
        return self
