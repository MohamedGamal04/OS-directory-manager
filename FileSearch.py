from os import walk
from psutil import disk_partitions
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Folder Manager")
        self.minsize(560, 300)
        self.maxsize(560, 300)
        self.toplevel = None
        self.iconbitmap('icon.ico')
        global search_results
        search_results = CTkTextbox(
            master=self,
            width=620,
            height=590,
            fg_color="#ffffff",
            text_color="black",
            border_color="black",
            border_width=1.2,
        )


def FS(gui_path, Wanted, byType):
    app = App()
    wanted = Wanted.strip()
    path = gui_path[0]
    path = path.replace("/", "\\")
    if gui_path == []:
        path = "all"
    flag = False
    Type = byType
    instance = FileSearch(path, wanted, flag, Type)
    if path == "all":
        instance.check_every_partition().final()
    else:
        instance.single_path().final()


class FileSearch(object):
    """
        This class is used to search files whether it's by name or by type
    """

    def __init__(self, path, wanted, flag, Type) -> None:
        self.path = path
        self.wanted = wanted
        self.flag = flag
        self.Type = Type
        self.files_found = []
        self.app = App()

    def check_every_partition(self) -> None:
        """
            searches a file in all partitions
        """
        for partitions in disk_partitions():
            self.path = partitions[0]
            for source, dir, files in walk(self.path):
                for file in files:
                    print(file)
                    if self.Type is False:
                        temp = file[:file.rfind(".")]
                    else:
                        try:
                            temp = file[file.rfind(".")+1:]
                        except IndexError:
                            pass
                        if temp == self.wanted:
                            self.flag = True
                            self.files_found.append(
                                f"{source}\\{file}".replace("\\\\", "\\"))
        return self

    def single_path(self) -> None:
        """
            searches a file in one partition
        """
        for source, dir, files in walk(self.path):
            for file in files:
                if self.Type is False:
                    temp = file[:file.rfind(".")]
                else:
                    try:
                        temp = file[file.rfind(".")+1:]
                    except IndexError:
                        pass
                if temp == self.wanted:
                    self.flag = True
                    self.files_found.append(
                        f"{source}\\{file}".replace("\\\\", "\\"))
        return self

    def final(self) -> None:
        """
            displaying results
        """
        f = ""
        if self.flag is False:
            f = "files not found"
        for line in self.files_found:
            f = f+line+"\n"
        search_results.insert(END, f)
        search_results.pack()
        self.app.mainloop()
        return self
