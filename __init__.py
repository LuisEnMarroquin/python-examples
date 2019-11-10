from tkinter import Tk, Label, Button, Frame, PhotoImage

WIDTH = 700
HEIGHT = 500
RESIZE = False
BACKGROUND = 'green'

WINDOW = Tk()
WINDOW.title("Snake")
WINDOW.config(bg="red")
WINDOW.geometry('{}x{}'.format(WIDTH, HEIGHT)) # Window size adapts to frame
WINDOW.resizable(RESIZE, RESIZE)
WINDOW.iconbitmap("favicon.ico")

MAIN_FRAME = Frame(WINDOW)
MAIN_FRAME.config(bg=BACKGROUND, width=WIDTH, height=HEIGHT, cursor="hand2")
MAIN_FRAME.pack(fill="both", expand=True) # Expand on 'x' and 'y' on resize

BUTTON_FRAME = Frame(MAIN_FRAME)
BUTTON_FRAME.config(bg=BACKGROUND)
BUTTON_FRAME.pack(padx=5, pady=5)

MAIN_LABEL = Label(BUTTON_FRAME, text="Null", fg='red', font=("Comic Sans MS", 12))
MAIN_LABEL.grid(column=1, row=3)
# MAIN_LABEL.place(x=10, y=75)

def clicked(arg):
  if arg == 1:
    MAIN_LABEL.configure(text="UP")
  elif arg == 2:
    MAIN_LABEL.configure(text="LEFT")
  elif arg == 3:
    MAIN_LABEL.configure(text="BOTTOM")
  else:
    MAIN_LABEL.configure(text="RIGHT")

Button(BUTTON_FRAME, justify='center', text="↑", height=2, width=5, command=lambda: clicked(1)).grid(column=1, row=1)
Button(BUTTON_FRAME, justify='center', text="←", height=2, width=5, command=lambda: clicked(2)).grid(column=0, row=2)
Button(BUTTON_FRAME, justify='center', text="↓", height=2, width=5, command=lambda: clicked(3)).grid(column=1, row=2)
Button(BUTTON_FRAME, justify='center', text="→", height=2, width=5, command=lambda: clicked(4)).grid(column=2, row=2)

WINDOW.mainloop()
