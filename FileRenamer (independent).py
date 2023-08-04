import os
from Filename_Extension_Dictionarie import filename_extension_dictionarie
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.btn = CTkButton(
            master=self,
            text="close",
            command=self.destroy
        )
        self.btn.pack()

    def destroy(self):
        return super().destroy()


def gui(x):
    app = App()
    label = CTkLabel(
        master=app,
        text=x
    )
    global entry
    global gui_name
    gui_name = StringVar()
    entry = CTkEntry(
        master=app,
        textvariable=gui_name
    )
    entry.pack()
    label.pack()
    app.mainloop()


def FR(gui_path):
    path = gui_path[0]
    path = path.replace("/", "\\")
    rec_names = []
    for source, dir, files in os.walk(path):
        rec_names = []
        extensions = []
        filees = []
        skip = False
        if ((dir != []) or (files != [])) and (str(source).find("New folder") != -1):
            if dir == [] and (files != []):
                try:
                    for file in files:
                        if (file.rfind(".") != -1):
                            extensions.append(file[file.rfind(".")+1:])
                            filees.append([file, extensions[-1]])
                except FileNotFoundError:
                    pass
                finally:
                    for key, value in filename_extension_dictionarie.items():
                        for _ in extensions:
                            if _ in key:
                                rec_names.append(value)
            if dir != []:
                for d in dir:
                    for dir_source, dir_dir, dir_files in os.walk(f"{source}\{d}"):
                        if files == []:
                            for dir_file in dir_files:
                                if dir_file.find(".exe") != -1:
                                    rec_names.append(dir_file[:-4])
                        elif dir_files == []:
                            for file in files:
                                if file.find(".exe") != -1:
                                    rec_names.append(file[:-4])
                        elif dir_files != [] and files != []:
                            for file, dir_file in tuple(zip(files, dir_files)):
                                if file.find(".exe") != -1:
                                    rec_names.append(file[:-4])
                                elif dir_file.find(".exe") != -1:
                                    rec_names.append(dir_file[:-4])
                                elif (file.find(".exe") == -1) or (dir_file.find(".exe") == -1):
                                    pass
            while True:
                rec_names = set(rec_names)
                x = ""
                for name in rec_names:
                    x = f"{x}+\n{name}".replace("+", "").strip()
                gui(x)
                try:
                    choice = int(gui_name.get())
                except:
                    del rec_names
                    rec_names = str(gui_name.get())
                    skip = True
                if (skip is False):
                    rec_names = list(rec_names)
                    try:
                        rec_names = rec_names[choice]
                    except IndexError:
                        gui(x)
                    skip = False
                T = str(rec_names)
                if (T == "set()") or (T == "[]") or (T == ""):
                    continue
                else:
                    break
            print(rec_names)
            temp = source[:source.rfind("\\")]
            os.rename((f"{source}"), f"{temp}\\{rec_names}")
            del temp
FR()