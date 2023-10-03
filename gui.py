from typing import Tuple
from customtkinter import *
from tkinter import filedialog, ttk, messagebox
from PIL import Image
import tomlkit
from Folder_Manager_Config import *
import webbrowser


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title(title)
        self.minsize(minsize[0], minsize[1])
        self.maxsize(maxsize[0], maxsize[1])
        self.toplevel = None
        self.iconbitmap(icon)
        self.Image = Image.open(
            background)
        self.img = CTkImage(self.Image, size=(
            background_geometry[0], background_geometry[1]))
        l = CTkLabel(self, text="", image=self.img)
        l.place(x=0, y=0)
        self.organizer_btn = CTkButton(
            master=self,
            width=80,
            height=80,
            text="Organizor",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.organizer,
            border_color=button_bordercolor,
            border_width=button_borderwidth,
        )
        self.Folders_creator_btn = CTkButton(
            master=self,
            width=80,
            height=80,
            text="Folders creator",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.DirMaker,
            border_color=button_bordercolor,
            border_width=button_borderwidth,
        )
        self.Empty_Folder_Deleter_btn = CTkButton(
            master=self,
            width=80,
            height=80,
            text="Empty folders deleter",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.EFD,
            border_color=button_bordercolor,
            border_width=button_borderwidth,
        )
        self.signature = CTkButton(
            master=self,
            width=50,
            height=30,
            bg_color="#641960",
            fg_color="#641960",
            hover_color="#641960",
            text="https://github.com/MohamedGamal04",
            font=entry_font,
            command=self.github
        )
        self.File_search_btn = CTkButton(
            master=self,
            width=80,
            height=80,
            text="File search",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.FS,
            border_color=button_bordercolor,
            border_width=button_borderwidth,
        )

        self.logo = CTkImage(Image.open(
            "logo.png"), size=(35, 35))
        self.github_logo = CTkLabel(
            master=self, text="", image=self.logo, bg_color="#641960")
        self.organizer_btn.grid(row=0, column=1, sticky=S, pady=18, padx=5)
        self.Folders_creator_btn.grid(
            row=0, column=2, sticky=S, pady=18, padx=5)
        self.Empty_Folder_Deleter_btn.grid(
            row=0, column=3, sticky=S, pady=18, padx=5)
        self.File_search_btn.grid(
            row=0, column=4, sticky=S, pady=18, padx=5)
        self.github_logo.place(x=0, y=98)
        self.signature.place(x=30, y=100)

    def organizer(self):
        if self.toplevel is None or not self.toplevel.winfo_exists():
            self.toplevel = OrganizerToplevelWindow(self)
        else:
            self.toplevel.focus()

    def DirMaker(self):
        if self.toplevel is None or not self.toplevel.winfo_exists():
            self.toplevel = DMToplevelWindow(self)
        else:
            self.toplevel.focus()

    def EFD(self):
        if self.toplevel is None or not self.toplevel.winfo_exists():
            self.toplevel = EFDToplevelWindow(self)
        else:
            self.toplevel.focus()

    def FS(self):
        if self.toplevel is None or not self.toplevel.winfo_exists():
            self.toplevel = FSToplevelWindow(self)
        else:
            self.toplevel.focus()

    def github(self):
        webbrowser.open("https://github.com/MohamedGamal04")


class FSToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.path = StringVar()
        self.search = StringVar()
        self.search_by_type = BooleanVar()
        self.color = "#5f1842"
        self.config(background=self.color)
        self.iconbitmap(icon)
        self.title("File search")
        self.minsize(560, 100),
        self.maxsize(560, 100)
        self.path_entry = CTkEntry(
            master=self,
            width=385,
            height=30,
            fg_color=entry_color,
            border_color=entry_bordercolor,
            text_color=entry_textcolor,
            font=entry_font,
            placeholder_text="type all if you want to search all partitions"
        )
        self.path_entry.bind("<FocusIn>", self.path_entry_var)
        self.open_dir_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Open directory",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.path_getter,
        )
        self.ok_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Ok",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.ok_destroy,
        )
        self.cancel_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Cancel",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.destroy,
        )
        self.search_type = CTkCheckBox(
            master=self,
            width=50,
            height=30,
            bg_color=self.color,
            text="Search by type",
            font=button_font,
            variable=self.search_by_type
        )
        self.search_entry = CTkEntry(
            master=self,
            width=385,
            height=30,
            bg_color=self.color,
            fg_color=entry_color,
            border_color=entry_bordercolor,
            text_color=entry_textcolor,
            placeholder_text="Name of the file or type",
            font=entry_font,
            textvariable=self.search
        )
        self.waiting_label = CTkLabel(
            master=self,
            text="It may take some time please wait",
            text_color=entry_textcolor,
            fg_color=label_color
        )
        self.ok_btn.place(x=390, y=40)
        self.cancel_btn.place(x=470, y=40)
        self.path_entry.grid(row=0, column=0, columnspan=2,
                             sticky=W, pady=2, padx=2)
        self.open_dir_btn.grid(row=0, column=2, sticky=W, pady=2, padx=2)
        self.search_type.grid(row=2, column=0, columnspan=2,
                              sticky=W, pady=2, padx=2)
        self.search_entry.grid(row=1, column=0, columnspan=2,
                               sticky=W, pady=2, padx=2)
        self.waiting_label.place(x=360, y=80)
        self.toplevel = None
        self.grab_set()

    def path_getter(self):
        global path
        self.path_entry.configure(textvariable=self.path)
        path = filedialog.askdirectory()
        self.path.set(path)
        paths.clear()
        paths.append(path)

    def path_entry_var(self, event):
        self.path_entry.configure(textvariable=self.path)

    def ok_destroy(self):
        if not os.path.exists(self.path.get()) and not (self.path.get() == "all"):
            messagebox.showerror("Path error", "Empty or invalid path")
        else:
            if paths == []:
                paths.append(self.path.get())
            self.ok_destroy = True
            from FileSearch import FS
            FS(paths, self.search.get(), self.search_by_type.get())
            self.destroy()

    def destroy(self):
        paths.clear()
        self.ok_destroy = False
        return super().destroy()


class EFDToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.path = StringVar()
        self.NF_only_bool = BooleanVar()
        self.nested_bool = BooleanVar()
        self.color = "#5f1842"
        self.config(background=self.color)
        self.iconbitmap(icon)
        self.title("Empty folder deleter")
        self.minsize(560, 100)
        self.maxsize(560, 100)
        self.path_entry = CTkEntry(
            master=self,
            width=385,
            height=30,
            fg_color=entry_color,
            border_color=entry_bordercolor,
            text_color=entry_textcolor,
            font=entry_font,
            textvariable=self.path
        )
        self.open_dir_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Open directory",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.path_getter,
        )
        self.ok_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Ok",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.ok_destroy,
        )
        self.cancel_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Cancel",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.destroy,
        )
        self.Newfolder_only = CTkCheckBox(
            master=self,
            width=50,
            height=30,
            bg_color=self.color,
            text="Delete \"New folder(s)\" only",
            font=checkbox_font,
            variable=self.NF_only_bool
        )
        self.Nested_only = CTkCheckBox(
            master=self,
            width=50,
            height=30,
            bg_color=self.color,
            text="Apply on nested folders",
            font=button_font,
            variable=self.nested_bool
        )
        self.ok_btn.place(x=390, y=40)
        self.cancel_btn.place(x=470, y=40)
        self.path_entry.grid(row=0, column=0, columnspan=2,
                             sticky=W, pady=2, padx=2)
        self.open_dir_btn.grid(row=0, column=2, sticky=W, pady=2, padx=2)
        self.Newfolder_only.grid(row=1, column=0, columnspan=2,
                                 sticky=W, pady=2, padx=2)
        self.Nested_only.grid(row=2, column=0, columnspan=2,
                              sticky=W, pady=2, padx=2)
        self.grab_set()

    def path_getter(self):
        global path
        path = filedialog.askdirectory()
        self.path.set(path)
        paths.clear()
        paths.append(path)

    def ok_destroy(self):
        if not os.path.exists(self.path.get()):
            messagebox.showerror("Path error", "Empty or invalid path")
        else:
            if paths == []:
                paths.append(self.path.get())
            self.ok_destroy = True
            from EmptyFolderDeleter import EFD
            EFD(paths, self.nested_bool.get(), self.NF_only_bool.get())
            paths.clear()
            self.destroy()

    def destroy(self):
        if self.ok_destroy is not True:
            paths.clear()
        self.ok_destroy = False
        return super().destroy()


class DMToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.path = StringVar()
        self.color = "#5f1842"
        self.config(background=self.color)
        self.iconbitmap(icon)
        self.title("Folders creator")
        self.minsize(560, 250)
        self.maxsize(560, 250)
        self.path_entry = CTkEntry(
            master=self,
            width=385,
            height=30,
            font=entry_font,
            fg_color=entry_color,
            border_color=entry_bordercolor,
            text_color=entry_textcolor,
            textvariable=self.path
        )
        self.open_dir_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Open directory",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.path_getter,
        )
        self.ok_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Ok",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.ok_destroy,
        )
        self.cancel_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Cancel",
            fg_color=button_color,
            font=button_font,
            hover_color=button_hovercolor,
            text_color=button_textcolor,
            command=self.destroy,
        )
        self.names_label = CTkLabel(
            master=self,
            text="Directories names:",
            fg_color=label_color,
            font=button_font,
            bg_color="transparent"
        )
        self.names_note_label = CTkLabel(
            master=self,
            text="if you want to create\nnested directories use \"\\\" in between\ne.g(New folder \\ New folder 1\nNew folder \\ New folder 2)",
            fg_color=label_color,
            font=("Arial", 14),
            bg_color="transparent"
        )
        self.names_textbox = CTkTextbox(
            master=self,
            width=310,
            height=200,
            fg_color=entry_color,
            text_color=entry_textcolor,
            border_color=button_bordercolor,
            border_width=button_borderwidth,

        )
        self.ok_btn.place(x=5, y=140)
        self.cancel_btn.place(x=5, y=200)
        self.path_entry.grid(row=0, column=0, columnspan=2,
                             sticky=W, pady=2, padx=2)
        self.open_dir_btn.grid(row=0, column=2, sticky=W, pady=2, padx=2)
        self.names_label.grid(row=1, column=0, sticky=W, pady=2, padx=2)
        self.names_note_label.grid(row=2, column=0, sticky=W, pady=2, padx=2)
        self.names_textbox.place(x=240, y=40)
        self.grab_set()

    def path_getter(self):
        global path
        path = filedialog.askdirectory()
        self.path.set(path)
        paths.clear()
        paths.append(path)

    def ok_destroy(self):
        if not os.path.exists(self.path.get()):
            messagebox.showerror("Path error", "Empty or invalid path")
        else:
            if paths == []:
                paths.append(self.path.get())
            self.ok_destroy = True
            from MakeDirs import MDmain
            self.names = self.names_textbox.get(1.0, "end-1c")
            MDmain(paths, self.names)
            paths.clear()
            self.destroy()

    def destroy(self):
        if self.ok_destroy is not True:
            paths.clear()
        self.ok_destroy = False
        return super().destroy()


class OrganizerToplevelWindow(CTkToplevel):
    first_time = True
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.iconbitmap('icon.ico')
        self.title("File Organizer")
        self.first_time = True
        self.paths = StringVar()
        self.organize_folders_bool = BooleanVar()
        self.organize_to_path_bool = BooleanVar()
        self.minsize(470, 160)
        self.maxsize(470, 160)
        self.path_entry = CTkEntry(
            master=self,
            width=300,
            height=30,
            font=("Arial", 15, ),
            fg_color="#ffffff",
            border_color="#ffffff",
            text_color="black",
            textvariable=self.paths
        )
        self.open_dir_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Open directory",
            font=("Arial", 20, "bold"),
            command=self.path_getter,
        )
        self.ok_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Ok",
            font=("Arial", 20, "bold"),
            command=self.ok_destroy,
        )
        self.cancel_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Cancel",
            font=("Arial", 20, "bold"),
            command=self.destroy,
        )
        self.Organize_folders = CTkCheckBox(
            master=self,
            width=50,
            height=30,
            text="Organize Folders",
            font=("Arial", 20, "bold"),
            variable=self.organize_folders_bool
        )
        self.Organize_to_path = CTkCheckBox(
            master=self,
            width=50,
            height=30,
            text="Organize to another path",
            font=("Arial", 20, "bold"),
            variable=self.organize_to_path_bool,
            command=self.OTP
        )
        self.path_entry.grid(row=0, column=0, columnspan=2,
                             sticky=W, pady=2, padx=2)
        self.open_dir_btn.grid(row=0, column=2, sticky=W, pady=2, padx=2)
        self.Organize_folders.place(x=5, y=38)
        self.Organize_to_path.place(x=5, y=78)
        self.ok_btn.place(x=5, y=122)
        self.cancel_btn.place(x=90, y=122)
        self.grab_set()

    def OTP(self):
            if self.organize_to_path_bool.get():
                self.minsize(530, 190)
                self.maxsize(530, 190)
                self.sec_path = StringVar()
                self.sec_path_entry = CTkEntry(
                    master=self,
                    width=300,
                    height=30,
                    font=("Arial", 15, ),
                    fg_color="#ffffff",
                    border_color="#ffffff",
                    text_color="black",
                    textvariable=self.sec_path
                )
                self.sec_open_dir_btn = CTkButton(
                    master=self,
                    width=50,
                    height=30,
                    text="Open directory",
                    font=("Arial", 20, "bold"),
                    command=self.sec_path_getter,
                )
                self.from_label = CTkLabel(
                    master=self,
                    width=50,
                    height=30,
                    text="From:",
                    font=("Arial", 20, "bold"),
                )
                self.to_label = CTkLabel(
                    master=self,
                    width=50,
                    height=30,
                    text="To:",
                    font=("Arial", 20, "bold"),
                )
                self.from_label.grid(row=0, column=0, sticky=W, pady=2, padx=2)
                self.to_label.grid(row=1, column=0, sticky=W, pady=2, padx=2)
                self.path_entry.grid(row=0, column=1, columnspan=2,
                                     sticky=W, pady=2, padx=2)
                self.open_dir_btn.grid(
                    row=0, column=3, sticky=W, pady=2, padx=2)
                self.sec_path_entry.grid(row=1, column=1, columnspan=2,
                                         sticky=W, pady=2, padx=2)
                self.sec_open_dir_btn.grid(
                    row=1, column=3, sticky=W, pady=2, padx=2)
                self.Organize_folders.place(x=5, y=78)
                self.Organize_to_path.place(x=5, y=118)
                self.ok_btn.place(x=5, y=152)
                self.cancel_btn.place(x=90, y=152)
                self.grab_set()
            else:
                self.minsize(470, 160)
                self.maxsize(470, 160)
                self.from_label.destroy()
                self.to_label.destroy()
                self.sec_path_entry.destroy()
                self.sec_open_dir_btn.destroy()
                self.path_entry.grid(row=0, column=0, columnspan=2,
                                     sticky=W, pady=2, padx=2)
                self.open_dir_btn.grid(
                    row=0, column=2, sticky=W, pady=2, padx=2)
                self.Organize_folders.place(x=5, y=38)
                self.Organize_to_path.place(x=5, y=78)
                self.ok_btn.place(x=5, y=122)
                self.cancel_btn.place(x=90, y=122)
                self.grab_set()

    def path_getter(self):
            path = filedialog.askdirectory()
            self.paths.set(path)

    def sec_path_getter(self):
            path = filedialog.askdirectory()
            self.sec_path.set(path)

    def ok_destroy(self):
            if not os.path.exists(self.paths.get()):
                messagebox.showerror("Path error", "Empty or invalid path")
            else:
                self.ok_destroy = True
                paths.append(self.paths.get())
                if self.organize_to_path_bool.get():
                    paths.append(self.sec_path.get())
                from FileOrgnizer import FOmain
                FOmain(paths, self.organize_folders_bool.get(),self.organize_to_path_bool.get())
                paths.clear()
                self.destroy()

    def destroy(self):
            if self.ok_destroy is not True:
                paths.clear()
            self.ok_destroy = False
            return super().destroy()



paths = []
app = App()
app.mainloop()
