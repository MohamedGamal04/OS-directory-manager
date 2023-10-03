import os
from shutil import move
from tkinter import messagebox
import pickle
file_extensions = {("png", "jpg", "jpeg", "webp"): "Photos",
                   ("webm", "mkv", "avi", "wmv", "mp3", "mp4", "mp2", "mov", "mpe", "mpv", "m3u8"): "Videos",
                   ("wav", "opus"): "Audios",
                   ("torrent"): "Torrents",
                   ("otf", "ttf"): "Fonts",
                   ("prfpset"): "Premiere",
                   ("ms14"): "Cirucits",
                   ("dll"): "Dlls",
                   ("apk"): "Files",
                   ("docx", "doc", "docm", "dot", "dotm", "dotx", "rtf"): "Word",
                   ("pptx", "pot", "ppa", "pps", "ppsm", "ppsx", "ppt", "pptm"): "Power Point",
                   ("xlsx", "xls", "xla", "xlsm", "xlt"): "Excel",
                   ("accdb"): "Access",
                   ("lnk", "url"): "Short cuts",
                   ("gif"): "Gifs",
                   ("pdf"): "PDFs",
                   ("exe", "msi"): "Programmes",
                   ("txt"): "Text files",
                   ("rar", "zip"): "Archive files",
                   ("psd"): "Photoshop",
                   ("mp3"): "Archive files"
                   }


def FOmain(gui_paths: list[str], organize_folders: bool,to_folder: bool):
    if to_folder:
        instance = Fileorganizer(gui_paths[0],gui_paths[1])
    else: instance = Fileorganizer(gui_paths[0])
    instance.explore_path(
            organize_folders).categorization().make_dirs().move_files()


class Fileorganizer(object):
    """
        This class is used to organize different files by moving them into different directories
    """

    def __init__(self, path, sec_path = None) -> None:
        self.extensions = []
        self.files = []
        self.dir_names = []
        self.sec_path = None
        if sec_path is not None:
            sec_path = sec_path.replace("/", "\\")
            self.sec_path = sec_path
        path = path.replace("/", "\\")
        self.path = path

    def explore_path(self, organize_folders) -> None:
        """
            this function is used to explore the chosen path and record the file and it's extension
        """
        try:
            for file_name in os.listdir(path=self.path):
                if os.path.isdir(self.path+'\\'+file_name) and organize_folders:
                    if not(file_name in file_extensions.values()):
                        if self.sec_path is not None:
                            move(f"{self.path}\\{file_name}",
                             f"{self.sec_path}\\Folders\\{file_name}")
                        else:
                            move(f"{self.path}\\{file_name}",
                                f"{self.path}\\Folders\\{file_name}")
                elif (file_name.rfind(".") != -1):
                    self.extensions.append(file_name[file_name.rfind(".")+1:])
                    self.files.append([file_name, self.extensions[-1]])

            return self
        except FileNotFoundError:
            return self

    def categorization(self) -> None:
        """
            this function is used to categorize each file extension e.g(png -> Photos)
        """
        for key, value in file_extensions.items():
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
            os.makedirs(f"{self.path}\\{dir_name}", exist_ok=True)
        return self

    def move_files(self) -> None:
        """
             this function is used to move the files
        """
        for file in self.files:
            for key, value in file_extensions.items():
                file[1] = file[1].lower()
                if file[1] in key:
                    file.append(value)
            try:
                if self.sec_path is not None:
                    move(f"{self.path}\\{file[0]}", f"{self.sec_path}\\{file[2]}")
                else:
                    move(f"{self.path}\\{file[0]}", f"{self.path}\\{file[2]}")
            except:
                messagebox.showerror(
                    "Move error", f"Failed to move {file[0]} extension unknown")
        return self