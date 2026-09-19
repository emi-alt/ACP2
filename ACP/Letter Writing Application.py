from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

screen = Tk()
screen.title("Letter Writing Application")
screen.geometry("600x500")
screen.grid_rowconfigure(0, weight=1)
screen.grid_columnconfigure(1, weight=1)

def open_letter():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    screen.title(f"Letter Writing Application - {filepath}")

def save_letter():
    filepath = asksaveasfilename(defaultextension=".txt")
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        output_file.write(txt_edit.get(1.0, END))
    screen.title(f"Letter Writing Application - {filepath}")

txt_edit = Text(screen)
fr_buttons = Frame(screen, relief=RAISED, bd = 2)

btn_open = Button(fr_buttons, text="Open Letter", command=open_letter)
btn_save = Button(fr_buttons, text="Save Letter As...", command=save_letter)

btn_open.grid(row=0, column=0, sticky="ew")
btn_save.grid(row=1, column=0, sticky="ew")
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

screen.mainloop()
# ---------- PART 5: lay it out with grid ----------
# YOUR CODE HERE
# btn_open   -> row 0, column 0 of the frame, sticky "ew"
# btn_save   -> row 1, column 0 of the frame, sticky "ew"
# fr_buttons -> row 0, column 0 of the window, sticky "ns"
# txt_edit   -> row 0, column 1 of the window, sticky "nsew"


# ---------- PART 6: start the program ----------
# YOUR CODE HERE
# One line. Without it the window is cre