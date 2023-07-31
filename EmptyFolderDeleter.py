import os
import shutil


def EFD(gui_path, nested_bool, NF_only_bool):
    path = gui_path[0]
    path =path.replace("/","\\")
    gen = os.walk(path)
    Newfolder_only = NF_only_bool
    Nested = nested_bool
    while Nested:
        flag = False
        for source, dir, file in gen:
            if Newfolder_only == True:
                con = source.find("New folder") != -1
            else:
                con = True
            if (dir == [] and file == [] and con):
                flag = True
                shutil.rmtree(source)
                gen = os.walk(path)
                break
            continue
        if flag == False:
            break
    for source, dir, file in gen:
        if Newfolder_only == True:
            con = source.find("New folder") != -1
        else:
            con = True
        if (dir == [] and file == [] and con):
            if len(source.partition(path)[2].split("\\")) <= 2:
                shutil.rmtree(source)
