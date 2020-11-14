import os
import subprocess
sources = ["/bin", "/usr/bin"]

def get_initial_list():
    programms_list = []
    for element in sources:
        programms_list.extend(os.listdir(path = element))

    programms_list = sorted(set(programms_list))
    return programms_list

def handle_entry(value):
    programms_list = get_initial_list()
    newlist = [program for program in programms_list if program.startswith(value)]
    return newlist

def handle_click(selected):
    subprocess.Popen([selected])
    return True