from os import makedirs
def MDmain(gui_path,gui_names):
    path=gui_path[0]
    print(path)
    names=str(gui_names).split("\n")
    for name in names:
        makedirs(f"{path}\\{name}",exist_ok=True)
