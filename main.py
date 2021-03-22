#! /usr/bin/env python3
import tkinter as tk
import os
import config
import argparse
from importlib import import_module


class Dialog(tk.Frame):
    def __init__(self, master, module):
        super().__init__(master)
        self.root = master
        self.module = module
        self.listlen = None
        self.var = tk.StringVar()
        self.var.trace("w", self.entry_changed)

        self.entry = tk.Entry(self, textvariable=self.var, bg=config.entry_bg, font=(config.text_font, config.font_size), fg=config.text_color, highlightthickness=0, bd=0, insertbackground=config.text_color)
        self.entry.pack(fill = 'x')

        self.fr = tk.Frame(self, height=config.separator_size, bg=config.separator_color)
        self.fr.pack(fill = 'x')

        self.listbox = tk.Listbox(self,exportselection=0, selectmode='single', bg=config.listbox_bg, font = (config.text_font, config.font_size), fg=config.text_color, selectforeground=config.text_color, selectbackground=config.focus_color, highlightthickness=0, bd=0, activestyle='none')
        self.listbox.pack(fill="both", expand=1)

        self.listbox.bind("<Double-Button-1>", self.handle_click)

        self.root.bind("<Up>", self.list_up)
        self.root.bind("<Down>", self.list_down)
        self.root.bind("<Return>", self.handle_click)
        self.root.bind("<Escape>", self.exit)

        self.entry.focus_set()

    def list_up(self, *args):
        if self.listbox.curselection()[0] != 0:
            x = self.listbox.curselection()[0]
            self.listbox.select_clear(x)
            self.listbox.select_set(x-1)
            self.listbox.yview_scroll(-1, "units")

    def list_down(self, *args):
        x = self.listbox.curselection()[0]
        if self.listlen is None or self.listlen-1 != x:
            self.listbox.activate(x+1)
            self.listbox.select_clear(x)
            self.listbox.select_set(x+1)
            self.listbox.yview_scroll(1, "units")

    def entry_changed(self, *args):
        value = self.var.get()
        result_list = self.module.handle_entry(value)
        self.listbox.delete(0, tk.END)
        for item in result_list:
            self.listbox.insert(tk.END, item)
        self.listbox.select_set(0)

    def handle_click(self, *args):
        selected = self.listbox.get(self.listbox.curselection())
        self.module.handle_click(selected)
        self.close_window()

    def close_window(self, *args):
        it_close = self.module.close()
        if it_close:
            self.root.destroy()


    def exit(self, *args):
        self.root.destroy()

def main():

    parser = argparse.ArgumentParser(description='Select mode')
    parser.add_argument('-m', dest="mode")
    args = parser.parse_args()

    select_module = args.mode
    module = import_module(f"modules.{select_module}")

    windows_size = f"{config.weight}x{config.height}"

    root = tk.Tk()
    root['bg'] = config.listbox_bg
    root.geometry(windows_size)
    root.resizable(False, False)
    root.attributes('-type', 'dialog')

    dialog = Dialog(root, module)

    initial_list = module.get_initial_list()
    for item in initial_list:
        dialog.listbox.insert(tk.END, item)

    dialog.listbox.select_set(0)
    dialog.listbox.activate(0)

    dialog.pack(expand = 'True', fill = 'both')
    root.mainloop()

<<<<<<< HEAD

dialog.pack(expand = 'True', fill = 'both')
if __name__ == '__main__':
    root.mainloop()
=======
if __name__ == '__main__':
    main()
>>>>>>> 17fb70aac525ba02642e375763de1a2af03086fa
