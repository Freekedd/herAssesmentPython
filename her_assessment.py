import tkinter as tk
from tkinter import filedialog
import os


class DataProcessor:
    def __init__(self):
        self.file_data = None

    @staticmethod
    def read_file(filepath):
        if filepath:
            with open(filepath, "r") as file:
                return file.read()

    def process_file_data(self, file_data):
        if file_data:
            accession_code = []
            species = []
            sequences = ""
            read = False

            lines = file_data.split("\n")
            for line in lines:
                if line.startswith("AC"):
                    accession_code.append(line.strip("\n"))
                if line.startswith("OS"):
                    species.append(line.strip("\n"))
                if line.startswith("SQ"):
                    read = True
                if line.startswith("//"):
                    read = False
                if read:
                    sequences += line

            return accession_code, species, sequences

    def seperate_header_seq(self, sequences):
        entries = sequences.split("SQ   SEQUENCE")[1:]

        result_dict = {}

        for entry in entries:
            lines = entry.strip().split('\n')

            # Extracting header and sequence
            header = lines[0].strip()
            sequence = ''.join(lines[1:]).replace(' ', '')

            # Storing in dictionary
            result_dict[header] = sequence
        print(result_dict.keys())

        return result_dict


class Data:
    def __init__(self, result_dict):
        self.result_dict = result_dict


class Species(Data):
    def __init__(self, result_dict, organisme):
        super().__init__(result_dict)
        self.organisme = organisme


class ID(Data):
    pass


class GUI:
    # De constructor
    def __init__(self):
        self.file_data = None
        self.filepath = None

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
        self.file_data = DataProcessor.read_file(self.filepath)
        accession_code, species, sequences = DataProcessor().process_file_data(self.file_data)
        result_dict = DataProcessor().seperate_header_seq(sequences)


# Create an instance of the GUI class. ...
if __name__ == "__main__":
    test = GUI()
    test.create_GUI()
    test.main_window.mainloop()

