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
        self.iconbitmap('pngwing.ico')
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
    app=App()
    wanted = Wanted.strip()
    files_found = []
    path = gui_path[0]
    path = path.replace("/", "\\")
    if gui_path == []:
        path="all"
    flag = False
    Type = byType
    if str(path).lower() == "all":
        for partitions in disk_partitions():
            path = partitions[0]
            for source, dir, files in walk(path):
                for file in files:
                    print(file)
                    if Type is False:
                        temp = file[:file.rfind(".")]
                    else:
                        try:
                            temp = file[file.rfind(".")+1:]
                        except IndexError:
                            pass
                    if temp == wanted:
                        flag = True
                        files_found.append(
                            f"{source}\\{file}".replace("\\\\", "\\"))
    else:
        for source, dir, files in walk(path):
            for file in files:
                if Type is False:
                    temp = file[:file.rfind(".")]
                else:
                    try:
                        temp = file[file.rfind(".")+1:]
                    except IndexError:
                        pass
                if temp == wanted:
                    flag = True
                    files_found.append(
                        f"{source}\\{file}".replace("\\\\", "\\"))
                    
    f = "" 
    if flag is False:
        f = "files not found"
    for line in files_found:
        f = f+line+"\n"
    search_results.insert(END,f)
    search_results.pack()
    app.mainloop()
