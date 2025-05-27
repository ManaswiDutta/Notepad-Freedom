from tkinter import *

window = Tk()
window.title("Notepad Freedom")
window.geometry("800x450")
# icon = PhotoImage(file='icon.png') # WILL ADD LOGO LATER
# window.iconphoto(True, icon)

menubar = Menu(window)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0 , font=("Arial", 10))
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit) # will add warning later


edit_menu = Menu(menubar, tearoff=0 , font=("Arial", 10))
edit_menu.add_command(label="cut")
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")

menubar.add_cascade(label="File" , menu=file_menu)
menubar.add_cascade(label="Edit" , menu=edit_menu)


# note = Text(window, wrap=WORD, font=("Arial", 12)).pack(side='bottom' , expand=True)

window.mainloop()