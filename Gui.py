import tkinter as tk
import Function as func


def main():
    # Create the main window
    main_window = tk.Tk()
    main_window.geometry("400x300")
    main_window.title("Her Assessment Python")

    # Create label containing the text "Hi" as a test
    label = tk.Label(main_window, text="File: ")
    label.place(x=40,
                y=60)

    # Create textfield, bestandsnaam zichtbaar na het kiezen van een bestand
    # Misschien veranderen in text inplaats van een input area (twijfel aanpassen aan het einde, als tijd over)
    textfield = tk.Entry(main_window, width=30)
    textfield.place(x=80,
                    y=60)

    # Create button to select
        # Werkt nog niet.
    select_button = tk.Button(main_window, text="Select",
                              command=func.dataProcess.select_file)
    select_button.place(x=280,
                        y=55)

    # Create button open file (Misschien later weg halen) open naar analyseer???
        # Werkt nog niet.
    button = tk.Button(main_window, text="Open :)")
    button.place(x=40,
                 y=100)

    tk.mainloop()


if __name__ == "__main__":
    main()