import tkinter as tk
from tkinter import filedialog
import os


class FileReader:
    @staticmethod
    def read_file(filepath):
        if filepath:
            with open(filepath, "r") as file:
                return file.read()


class DataProcessor:
    def process_file_data(self, file_data):
        print("Processing file data:", file_data)


class GUI:
    # De constructor
    def __init__(self):
        self.filepath = None
        self.data_processor = data_processor

    def create_GUI(self):
        # Create the main window
        self.main_window = tk.Tk()
        self.main_window.geometry("400x300")
        self.main_window.title("Her Assessment Python")
        # Create label containing the text "File"
        self.label = tk.Label(self.main_window, text="File: ")
        self.label.place(x=40,
                         y=60)

        # Create Entry, bedoeling om de bestandsnaam te zien die je selecteert :)
        self.textfield = tk.Entry(self.main_window, width=30)
        self.textfield.place(x=80,
                             y=60)

        # Create button to select the file
        self.select_button = tk.Button(self.main_window, text="Select",
                                       command=self.select_file)
        self.select_button.place(x=280,
                                 y=55)

    def select_file(self):
        self.filepath = filedialog.askopenfilename()
        print(self.filepath)

        # Update the Entry with the selected file's name
        filename = os.path.basename(self.filepath)
        self.textfield.delete(0, tk.END)
        self.textfield.insert(0, filename)

        # Call the seperated FileReader class and pass the data to the DataProcessor class
        file_data = FileReader.read_file(self.filepath)
        self.data_processor.process_file_data(file_data)

        return self.filepath


# Create an instance of the GUI class. ...
if __name__ == "__main__":
    data_processor = DataProcessor()
    test = GUI()
    test.create_GUI()
    test.main_window.mainloop()

