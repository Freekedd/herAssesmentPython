import tkinter as tk


def main():
    # Create the main window
    main_window = tk.Tk()
    main_window.geometry("450x300")
    main_window.title("Her Assessment Python")

    # Create label containing the text "Hi" as a test
    label = tk.Label(main_window, text="Hi")
    label.place(x=40,
                y=60)

    # Create textfield, bestandsnaam zichtbaar na het kiezen van een bestand
    # Misschien veranderen in text inplaats van een input area (twijfel aanpassen aan het einde, als tijd over)
    textfield = tk.Entry(main_window, width=30)
    textfield.place(x=110,
                    y=60)

    # Create button to select file
        # Werkt nog niet.
    select_button = tk.Button(main_window, text="Select")
    select_button.place(x=300,
                        y=55)

    # Create button open file (Misschien later weg halen)
        # Werkt nog niet.
    button = tk.Button(main_window, text="Open :)")
    button.place(x=40,
                 y=100)

    tk.mainloop()


if __name__ == "__main__":
    main()