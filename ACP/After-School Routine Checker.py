from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("After-School Routine Checker")
screen.geometry("500x350")
screen.configure(bg="#07264b")

heading = Label(screen, text="After-School Routine Checker", font=("Arial", 18, "bold"))
heading.pack(pady=20)
instructions = Label(screen,
                     text="Check off the tasks you have completed after school.",
                     font=("Arial", 12)
                     )
instructions.pack(pady=10)
entry = Entry(screen, width=30)
entry.pack(pady=10)

key_lbl = Label(screen, text=f"Current Entry: {entry.get()}", font=("Arial", 12))
key_lbl.pack(pady=10)

routine_message = Label(
    screen,
    text="Click here to check your routine",
    bg="#398ab3",
    width=32,
    height=3
)
routine_message.config(text="Routine area selected!")  
routine_message.pack(pady=10)
routine_message.bind("<Button-1>", lambda event: routine_message.config(text="Routine area selected!"))

def handle_keypresss(event):
    read = event.char
    key_lbl.config(text=f"Current Entry: {read}")
    entry.bind("<KeyPress>", handle_keypresss)

def handle_click(event):
    routine = entry.get()
    routine_lbl = Label(screen, text=f"Routine: {routine}", font=("Arial", 12))
    routine_lbl.pack(pady=10)
    routine_lbl.bind("<Button-1>", handle_click)

    routine_message = Label(
    screen,
    text="Click here to check your routine",
    bg="#398ab3",
    width=32,
    height=3
)
    routine_message.pack(pady=10)
    routine_message.bind("<Button-1>", handle_click)
def check_routine():
    routine = entry.get()
    if routine == "":
        messagebox.showwarning("Warning", "Please enter a routine before checking.")
    elif routine:
        messagebox.showinfo("Routine Checked", f"You have checked off: {routine}")
    else:
        routine_message.config(text="Next task: " + routine)
         
Check_button = Button(screen, text="Check Routine", command=check_routine)
Check_button.pack(pady=10)
screen.mainloop()