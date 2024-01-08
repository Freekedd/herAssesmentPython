# Open file function die connected is met de GUI :) Op moment nog niet lekker werkend samen.

# Hier een class maken??? Nog niet zeker :/ Wordt nog wat :(
from tkinter import filedialog


def select_file():
    filepath = filedialog.askopenfilename()
    print(filepath)

    return filepath


def open_file(filepath):
    file = open(filepath, "r")
    for line in file:
        print(line)

    file.close()


filepath = select_file()
open_file(filepath)
