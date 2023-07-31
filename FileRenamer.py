import os
from Filename_Extension_Dictionarie import filename_extension_dictionarie
from customtkinter import *

def FR(gui_path):
    path = gui_path[0]
    path = path.replace("/", "\\")
    rec_names = []
    for source, dir, files in os.walk(path):
        rec_names = []
        extensions = []
        filees = []
        flag = 1
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
                            for dir_file in  dir_files:
                                if dir_file.find(".exe") != -1:
                                    rec_names.append(dir_file[:-4])
                        elif dir_files == []:
                            for file in  files:
                                if file.find(".exe") != -1:
                                    rec_names.append(file[:-4])
                        elif dir_files != [] and files != []:
                            for file, dir_file in tuple(zip(files, dir_files)):
                                if file.find(".exe") != -1:
                                    rec_names.append(file[:-4])
                                elif dir_file.find(".exe") != -1:
                                    rec_names.append(dir_file[:-4])
                rec_names=set(rec_names)
                for name in rec_names:
                    print(name)
                choice=int(input())
                rec_names=list(rec_names)
                rec_names=rec_names[choice]
                flag=0
            if flag != 0:
                rec_names = set(rec_names)
            if len(rec_names) > 1 and flag != 0:
                rec_names = tuple(zip(rec_names))
                temp = ""
                for i in rec_names: 
                    temp = f"{temp},{i[0]}"
                rec_names = temp[1:]
                del temp
                flag = 0
            if str(rec_names).find("{") != -1:
                rec_names = str(rec_names)[2:-2]
            if str(rec_names) == "set()":
                continue
            temp=source[:source.rfind("\\")]
            os.rename((f"{source}"),f"{temp}\\{rec_names}")  
            del temp 
