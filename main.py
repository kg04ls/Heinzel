from tkinter import *
import os
from config import *


programms_list = os.listdir(path = "/bin")
programms_list = sorted(programms_list)

root = Tk()
root['bg'] = box_bg
root.geometry('300x300')
root.resizable(False, False)
root.attributes('-type', 'dialog')


class Dialog(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.var = StringVar()
        self.var.trace("w", self.vald)

        self.entry = Entry(self, textvariable = self.var, bg = entry_bg, font = ('Arial' , font_size), fg = text_color, highlightthickness=0, bd = 0, insertbackground = text_color)
        self.entry.pack(fill = 'x')

        self.fr = Frame(self, height=2, bg = border_color)
        self.fr.pack(fill = 'x')

        self.listbox = Listbox(self,exportselection=0, selectmode='single', bg = box_bg, font = ('Arial' , font_size), fg = text_color, highlightthickness=0, bd = 0, activestyle = 'none')
        self.listbox.pack(fill=BOTH, expand=1)


        self.listbox.bind("<Double-Button-1>", self.entst)

        root.bind("<Up>", self.lstu)
        root.bind("<Down>", self.lstd)
        root.bind("<Return>", self.entst)
        root.bind("<Escape>", self.exit)

        self.entry.focus_set()


    def vald(self, *args):
        global programms_list
        value = self.var.get()
        newlist = [x for x in programms_list if x.startswith(value)]
        self.listbox.delete(0,END)
        for program in newlist:
            self.listbox.insert(END, program)
        self.listbox.select_set(0)
        self.listbox.activate(0)

    

    def lstu(self, *args):
        if self.listbox.curselection()[0] == 0:
            pass
        else:
            x = self.listbox.curselection()[0]
            self.listbox.select_clear(x)
            self.listbox.select_set(x-1)

    def lstd(self, *args):
        if not self.listbox.curselection():
            self.listbox.select_set(0)
        else:
            x = self.listbox.curselection()[0]
            self.listbox.select_clear(x)
            self.listbox.select_set(x+1)

    def entst(self, *args):
        selection = self.listbox.curselection()
        if not selection:
            return
        command_name = self.listbox.get(selection)
        root.destroy()
        os.system(command_name)

    def exit(self, *args):
        root.destroy()

dialog = Dialog(root)

for program in programms_list:
    dialog.listbox.insert(END, program)
dialog.listbox.select_set(0)
dialog.listbox.activate(0)

dialog.pack(expand = 'True', fill = 'both')
root.mainloop()