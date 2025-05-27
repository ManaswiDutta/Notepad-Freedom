from tkinter import *
from tkinter import filedialog

def savetext():
    path = filedialog.asksaveasfilename(defaultextension='.txt' , filetypes=[("Text file" , ".txt"),("HTML file" , ".html")], title="Save File")
    file=open(path,'w')
    text = str(note.get(1.0, END))
    file.write(text)
    file.close()

def openfile():
    path = filedialog.askopenfilename(title="Open File", filetypes=[("Text file", ".txt"), ("HTML file", ".html")])
    if path:
        with open(path, 'r') as file:
            opentext = file.read()
        note.delete(1.0, END)  # Clear existing content
        note.insert(END, opentext)  # Insert new content


window = Tk()
window.title("Notepad Freedom")
window.geometry("800x450")
# icon = PhotoImage(file='icon.png') # WILL ADD LOGO LATER
# window.iconphoto(True, icon)

menuframe = Frame(window).pack()

menubar = Menu(menuframe)
window.config(menu=menubar)
file_menu = Menu(menubar, tearoff=0 , font=("Arial", 10))
file_menu.add_command(label="New")
file_menu.add_command(label="Open" , command = openfile)
file_menu.add_command(label="Save" , command = savetext)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit) # will add warning later


edit_menu = Menu(menubar, tearoff=0 , font=("Arial", 10))
edit_menu.add_command(label="cut")
edit_menu.add_command(label="copy")
edit_menu.add_command(label="paste")

menubar.add_cascade(label="File" , menu=file_menu)
menubar.add_cascade(label="Edit" , menu=edit_menu)



textframe = Frame(window).pack()


note = Text(textframe, wrap=WORD, font=("Arial", 12))
note.pack(side='bottom' , expand=True , fill="both")

window.mainloop()