from tkinter import Tk, Label, Button

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('500x500')

lbl = Label(window, text="Moving nowhere")
lbl.grid(column=3, row=1)

def clicked(arg):
  if arg == 1:
    lbl.configure(text="UP")
  elif arg == 2:
    lbl.configure(text="LEFT")
  elif arg == 3:
    lbl.configure(text="RIGHT")
  else:
    lbl.configure(text="BOTTOM")

Button.winfo_width

Button(window, justify='center', width=2, text="↑", command=lambda:clicked(1)).grid(column=1, row=1)
Button(window, justify='center', width=2, text="←", command=lambda:clicked(2)).grid(column=0, row=2)
Button(window, justify='center', width=2, text="→", command=lambda:clicked(3)).grid(column=2, row=2)
Button(window, justify='center', width=2, text="↓", command=lambda:clicked(4)).grid(column=1, row=3)

# w = Label(window, text="red", bg="red", fg="white")
# w = Label(window, text="green", bg="green", fg="black")
# w = Label(window, text="blue", bg="blue", fg="white")

window.mainloop()
