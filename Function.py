# Open file function die connected is met de GUI :) Op moment nog niet lekker werkend samen.

# Hier een class maken??? Nog niet zeker :/ Wordt nog wat :(
from tkinter import filedialog


class dataProcess:
    def __init__(self):
        self.filepath = ""

    def select_file(self):
        self.filepath = filedialog.askopenfilename()
        print(self.filepath)

        #return filepath

    def open_file(self, filepath):
        file = open(self.filepath, "r")
        for line in file:
            print(line)

        file.close()


if __name__ == "__main__":
    test = dataProcess()
    #test.select_file()
    #filepath = select_file()
    #open_file(filepath)