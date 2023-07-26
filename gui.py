from typing import Tuple
from customtkinter import *
from tkinter import filedialog, ttk, PhotoImage
import os


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("File Manager")
        self.color = "#e31448"
        self.config(background=self.color)
        self.minsize(800, 125)
        self.maxsize(800, 125)
        self.toplevel = None
        self.organizer_btn = CTkButton(
            master=self,
            width=80,
            height=80,
            text="Organizor",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.organizer,
            border_color="black",
            border_width=1.2,
        )
        self.Folders_creator_btn = CTkButton(
            master=self,
            width=80,
            height=80,
            text="Directories creator",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.DirMaker,
            border_color="black",
            border_width=1.2,
        )
        self.organizer_btn.grid(row=0, column=1, sticky=S, pady=18, padx=5)
        self.Folders_creator_btn.grid(
            row=0, column=2, sticky=S, pady=18, padx=5)

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


class DMToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.path = StringVar()
        self.color = "#e31448"
        self.config(background=self.color)
        self.minsize(520, 250)
        self.path_entry = CTkEntry(
            master=self,
            width=350,
            height=30,
            fg_color="#ffffff",
            border_color="#ffffff",
            text_color="black",
            textvariable=self.path
        )
        self.open_dir_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Open directory",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.path_getter,
        )
        self.ok_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Ok",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.ok_destroy,
        )
        self.cancel_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Cancel",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.destroy,
        )
        self.names_label = CTkLabel(
            master=self,
            text="Directories names:",
            fg_color="#e31448",
            font=("Arial", 20, "bold"),
            bg_color="transparent"
        )
        self.names_textbox = CTkTextbox(
            master=self,
            width=330,
            height=200,
            fg_color="#ffffff",
            text_color="black",
            border_color="black",
            border_width=1.2,
        )
        self.ok_btn.place(x=5, y=90)
        self.cancel_btn.place(x=5, y=140)
        self.path_entry.grid(row=0, column=0, columnspan=2,
                             sticky=W, pady=2, padx=2)
        self.open_dir_btn.grid(row=0, column=2, sticky=W, pady=2, padx=2)
        self.names_label.grid(row=1, column=0, sticky=W, pady=2, padx=2)
        self.names_textbox.place(x=182,y=40)
        self.grab_set()
    def path_getter(self):
        global path
        path = filedialog.askdirectory()
        self.path.set(path)
        paths.clear()
        paths.append(path)
    def ok_destroy(self):
        self.ok_destroy = True
        from MakeDirs import MDmain
        self.names=self.names_textbox.get(1.0, "end-1c")
        MDmain(paths,self.names)
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
        self.paths = StringVar()
        self.color = "#e31448"
        self.config(background=self.color)
        self.minsize(520, 200)
        self.path_entry = CTkEntry(
            master=self,
            width=300,
            height=30,
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
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.path_getter,
        )
        self.confirm_dir_btn = CTkButton(
            master=self,
            width=30,
            height=30,
            text="✔",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.confirm_dir,
        )
        self.combobox = ttk.Combobox(
            master=self,
            width=60,
            values=paths,
        )
        self.directory_label = CTkLabel(
            master=self,
            text="Directories :",
            fg_color="#e31448",
            font=("Arial", 20, "bold"),
            bg_color="transparent"
        )
        self.del_selected_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Delete selected",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.delete,
        )
        self.ok_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Ok",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.ok_destroy,
        )
        self.cancel_btn = CTkButton(
            master=self,
            width=50,
            height=30,
            text="Cancel",
            fg_color="#02db06",
            font=("Arial", 20, "bold"),
            hover_color="#067d08",
            text_color="white",
            command=self.destroy,
        )
        self.path_entry.grid(row=0, column=0, columnspan=2,
                             sticky=W, pady=2, padx=2)
        self.open_dir_btn.grid(row=0, column=2, sticky=W, pady=2, padx=2)
        self.confirm_dir_btn.place(x=470, y=2)
        self.directory_label.grid(row=1, column=0, sticky=W, pady=5, padx=2)
        self.combobox.grid(row=1, column=1, columnspan=2, pady=5, padx=2)
        self.del_selected_btn.grid(
            row=2, column=1, columnspan=2, pady=1, padx=2)
        self.ok_btn.place(x=5, y=150)
        self.cancel_btn.place(x=90, y=150)
        self.grab_set()

    def path_getter(self):
        global path
        path = filedialog.askdirectory()
        self.paths.set(path)

    def confirm_dir(self):
        global paths
        if self.paths.get() != "":
            paths.append(self.paths.get())
            if OrganizerToplevelWindow.first_time is True:
                self.combobox['values'] += (self.paths.get().replace(" ", "-"))
                self.combobox.set((self.paths.get().replace(" ", "-")))
            else:
                self.combobox['values'] += (
                    self.paths.get().replace(" ", "-"),)
                self.combobox.set((self.paths.get().replace(" ", "-"),))
            self.paths.set("")
            OrganizerToplevelWindow.first_time = False

    def ok_destroy(self):
        self.ok_destroy = True
        from FileOrgnizer import FOmain
        FOmain(paths)
        paths.clear()
        self.destroy()

    def destroy(self):
        if self.ok_destroy is not True:
            paths.clear()
        self.ok_destroy = False
        return super().destroy()

    def delete(self):
        temp = []
        paths.remove(self.combobox.get().replace("-", " "))
        for i in self.combobox['values']:
            if(i != self.combobox.get()):
                temp.append(i)
        self.combobox['values'] = temp
        self.combobox.delete(0, 'end')


paths = []
app = App()
app.mainloop()
print(paths)
