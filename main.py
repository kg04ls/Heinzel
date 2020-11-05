import tkinter as tk 
import os
import config

programms_list = []
for element in config.sources:
    programms_list.extend(os.listdir(path = element))

programms_list = sorted(set(programms_list))

windows_size = f"{config.weight}x{config.height}"
root = tk.Tk()
root['bg'] = config.listbox_bg
root.geometry(windows_size)
root.resizable(False, False)
root.attributes('-type', 'dialog')


class Dialog(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.listlen = None

        self.var = tk.StringVar()
        self.var.trace("w", self.entry_changed)

        self.entry = tk.Entry(self, textvariable=self.var, bg=config.entry_bg, font=(config.text_font, config.font_size), fg=config.text_color, highlightthickness=0, bd=0, insertbackground=config.text_color)
        self.entry.pack(fill = 'x')

        self.fr = tk.Frame(self, height=config.separator_size, bg=config.separator_color)
        self.fr.pack(fill = 'x')

        self.listbox = tk.Listbox(self,exportselection=0, selectmode='single', bg=config.listbox_bg, font = (config.text_font, config.font_size), fg=config.text_color, selectforeground=config.text_color, selectbackground=config.focus_color, highlightthickness=0, bd=0, activestyle='none')
        self.listbox.pack(fill="both", expand=1)


        self.listbox.bind("<Double-Button-1>", self.start)

        root.bind("<Up>", self.list_up)
        root.bind("<Down>", self.list_down)
        root.bind("<Return>", self.start)
        root.bind("<Escape>", self.exit)

        self.entry.focus_set()

    def entry_changed(self, *args):
        value = self.var.get()
        newlist = [program for program in programms_list if program.startswith(value)]
        self.listlen = len(newlist)
        self.listbox.delete(0, tk.END)
        for program in newlist:
            self.listbox.insert(tk.END, program)
        self.listbox.select_set(0)

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

    def start(self, *args):
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
    dialog.listbox.insert(tk.END, program)

dialog.listbox.select_set(0)
dialog.listbox.activate(0)

dialog.pack(expand = 'True', fill = 'both')
if __name__ == '__main__':
    root.mainloop()