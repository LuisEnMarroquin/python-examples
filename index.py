from tkinter import Tk, Label, Button, Frame, PhotoImage

WIDTH = 700
HEIGHT = 500
RESIZE = False

WINDOW = Tk()
WINDOW.title("Snake")
WINDOW.config(bg="red")
WINDOW.geometry('{}x{}'.format(WIDTH, HEIGHT)) # Window size adapts to frame
WINDOW.resizable(RESIZE, RESIZE)
WINDOW.iconbitmap("favicon.ico")

MAIN_FRAME = Frame(WINDOW)
MAIN_FRAME.config(bg="green", width=WIDTH, height=HEIGHT)
MAIN_FRAME.pack(fill="both", expand=True) # Expand on 'x' and 'y' on resize
MAIN_FRAME.config(cursor="hand2") # Change cursor on hover

MAIN_LABEL = Label(MAIN_FRAME, text="Moving nowhere", fg='red', font=("Comic Sans MS", 18))
MAIN_LABEL.place(x=100, y=200)

MAIN_IMAGE = PhotoImage(file='favicon.png')
Label(MAIN_FRAME, image=MAIN_IMAGE).place(x=300, y=200)

def clicked(arg):
  if arg == 1:
    MAIN_LABEL.configure(text="UP")
  elif arg == 2:
    MAIN_LABEL.configure(text="LEFT")
  elif arg == 3:
    MAIN_LABEL.configure(text="BOTTOM")
  else:
    MAIN_LABEL.configure(text="RIGHT")

Button(MAIN_FRAME, justify='center', width=2, text="↑", command=lambda: clicked(1)).grid(column=1, row=1)
Button(MAIN_FRAME, justify='center', width=2, text="←", command=lambda: clicked(2)).grid(column=0, row=2)
Button(MAIN_FRAME, justify='center', width=2, text="↓", command=lambda: clicked(3)).grid(column=1, row=2)
Button(MAIN_FRAME, justify='center', width=2, text="→", command=lambda: clicked(4)).grid(column=2, row=2)

WINDOW.mainloop()
