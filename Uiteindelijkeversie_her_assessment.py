"""
Written by: Freeke den Dulk
date: 11 January 2024
Herkansing assessment

Een mislukte poging om dit assesment te maken, want waarom iets doen wat je toch niet kan.
"""

import tkinter as tk
from tkinter import filedialog
import os
import re
import matplotlib.pyplot as plt


class DataProcessor:
    def __init__(self):
        self.read = False
        self.sequences = ""
        self.accession_code = []
        self.species = []
        self.consensus = re.compile("[GSTNP]-x(6)-[FYVHR]-[IVN]-[KEP]-x-G-[STIVKRQ]-Y-[DNQKRMV]-[EP]-x(3)-[LIMVA]")

    def open_file(self, filepath):
        """
        Leest het bestand in en slaat het vervolgens op in de variabele file_data. Mocht er geen bestand
        geselecteerd zijn, geeft het een FileNotFoundError aan.
        :param filepath: Het geselecteerde bestand.
        :return: file_data: De inhoud van het bestand.
        """
        try:
            file_data = ""
            if filepath:
                with open(filepath, "r") as file:
                    file_data = file.read()
            return self.process_data(file_data)
        except FileNotFoundError:
            raise FileNotFoundError("Select the correct file")

    def process_data(self, file_data):
        """
        Zoekt per regel naar de accessiecode, organismen en sequenties. De accessiecode en organismen worden
        in een lijst opgeslagen, de sequenties met headers worden op geslagen in een string.
        :param file_data: De inhoud van het bestand.
        :return: accessie_code, species, sequences.
        """
        if file_data:
            for line in file_data.splitlines():
                if line.startswith("AC"):
                    self.accession_code.append(line.strip("\n"))
                if line.startswith("OS"):
                    self.species.append(line.strip("\n"))
                if line.startswith("SQ"):
                    self.read = True
                if line.startswith("//"):
                    self.read = False
                if self.read:
                    self.sequences += line

        return self.accession_code, self.species, self.sequences

    def seperate_header_seq(self, sequences):
        """
        Had de header en sequentie van elkaar moeten scheidden en vervolgens op moeten slaan in
        een dictionary.
        :param sequences:
        :return:
        """
        seq_dict = {}
        if sequences:
            print(sequences)

    def compare(self):
        """
        Had de consensus sequentie in de sequenties van het bestand moeten vinden.
        :return:
        """
        pass

    def plot(self):
        """
        Als er op de knop plot geklikt wordt, wordt de functie plot aangeroepen.
        Deze functie laat een lege plot zien.
        :return:
        """
        plt.plot()
        plt.title("Title plot")
        plt.xlabel("title X-axis")
        plt.ylabel("title Y-axis")

        plt.show()

class GUI:
    def __init__(self, data_processor):
        self.data_processor = data_processor
        self.create_gui()

    def create_gui(self):
        """
        Maakt een window aan waarin je een bestand kan selecteren en openen. Daarnaast heeft het ook een knop om
        een plot te bekijken.
        """
        # Create main window
        self.main_window = tk.Tk()
        self.main_window.geometry("400x300")
        self.main_window.title("Her Assessment Python")

        # Create Label containing the text "Select File"
        self.label = tk.Label(self.main_window, text="File: ")
        self.label.place(x=40,
                         y=60)

        # Create Entry, when file is selected the name of the file will be visible
        self.textfield = tk.Entry(self.main_window, width=30)
        self.textfield.place(x=80,
                             y=60)

        # Create Button to select a file
        self.select_button = tk.Button(self.main_window, text="Select",
                                       command=lambda: self.select_file(self.textfield))
        self.select_button.place(x=280,
                                 y=55)

        # Create Button to open a file
        self.open_button = tk.Button(self.main_window, text="Open",
                                     command=lambda: self.data_processor.open_file(self.textfield.get()))
        self.open_button.place(x=330,
                               y=55)

        # Create Button to show a plot
        self.plot_button = tk.Button(self.main_window, text="Plot",
                                     command=lambda: self.data_processor.plot())
        self.plot_button.place(x=40,
                               y=100)

    def select_file(self, textfield):
        """
        Als er op de knop select wordt geklikt roept het de functie select_file aan. Dit weergeeft een nieuw venster
        om een bestand te selecteren.
        :param textfield: Geeft in de entry balk de naam van het bestand weer, nadat deze is geselecteerd.
        :return: filepath.
        """
        filepath = filedialog.askopenfilename()
        filename = os.path.basename(filepath)

        textfield.delete(0, tk.END)
        textfield.insert(0, filename)

        return filepath


if __name__ == "__main__":
    """
    Maakt een object voor de class GUI en DataProcessor.
    """
    data_processor = DataProcessor()
    gui = GUI(data_processor)
    tk.mainloop()
