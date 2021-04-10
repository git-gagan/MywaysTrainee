"""#import tkinter module
import tkinter as tk

#Create the GUI application main Window where we are gonna add all the visuals
window = tk.Tk()

#adding inputs/widgets 
#widgets are like elements in HTML
inp = tk.Label(window, text = "Hello World!", font = ("Times New Roman", 50))       #label is the output to be shown on the window for single line definitions only

#Frames
frame1 = tk.Frame(window, height = 100, width = 100, cursor = "dot")
frame2 = tk.Frame(window, height = 100, width = 100, cursor = "dot")
l1 = tk.Label(frame1, text = "Mail", height = 1, width = 50)
l2 = tk.Label(frame1, text = "Password", height = 1, width = 50)
inp1 = tk.Entry(frame1, width = 10)
inp2 = tk.Entry(frame1, width = 10)
inp3 = tk.Entry(frame2, width = 10)
window.title("My first Tkinter program")    #title
window.geometry("400x400")                  #size
window.config(bg = "Pink")                  #bg color
l3 = tk.Label(frame2, text = "Name", height = 1, width = 50)
bt = tk.Button(window, text = "SUBMIT", height =5, width=10, fg="red",font = ("Times New Roman", 15))                                           #button widget

#pack the input to show the object in the window
inp.pack()
frame1.pack(side = "top")
frame2.pack(side = "bottom")
l1.pack()
inp1.pack()
l2.pack()
inp2.pack()
bt.pack(pady = 50)
l3.pack()
inp3.pack()

#run the main event loop suggesting to display the window till manually closed..
window.mainloop()"""

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Custom Design")
window.geometry("500x500")
window.config(bg = "black")

#creating a menu
menu = Menu(window)

File = Menu(menu, tearoff = 0)
File.add_command(label = "New")
File.add_command(label = "Open")
File.add_command(label = "Save")
File.add_command(label = "Save as")
File.add_separator()
File.add_command(label = "Exit", command = window.quit)

Edit = Menu(menu, tearoff = 0)
Edit.add_command(label = "Draw")
Edit.add_command(label = "Select")
Edit.add_command(label = "Cut")
Edit.add_command(label = "Paste")

View = Menu(menu, tearoff = 0)
View.add_command(label = "FullScreen")
View.add_command(label = "Half Screen")
View.add_command(label = "Terminal")
View.add_command(label = "No view")

Go = Menu(menu)
Go.add_command(labe= "Execute")

Run = Menu(menu)
Run.add_command(labe= "Debug")
Run.add_command(labe= "Compile")

Help = Menu(menu)
Help.add_command(labe= "References")
Help.add_command(labe= "Wikipedia")

menu.add_cascade(label = "File", menu = File)
menu.add_cascade(label = "Edit", menu = Edit)
menu.add_cascade(label = "View", menu = View)
menu.add_cascade(label = "Go", menu = Go)
menu.add_cascade(label = "Run", menu = Run)
menu.add_cascade(label = "Help", menu = Help)

window.config(menu = menu)

var = StringVar()
disp = Message(window, textvariable = var, padx = 30, pady = 30)


def clicked():
    #message Box
    response = messagebox.askyesno("Confirmation","Do you want to login?")
    if response:
        messagebox.showinfo("LogIN","Logged IN")
        la = Label(window, text = "Logged in successfully!", font = ("comic sans ms",15))
        la.pack(fill = X, expand = 1)
        bt = Button(text = "Log Out!", command = la.destroy)
        bt.pack(side =  BOTTOM, fill = X)
    else:
        messagebox.showerror("Negative","You didn't logged in")

bt = Button(window, text = "LOGIN", font = ("comic sans ms",15), bg = "grey", fg = "black", activebackground = "black", activeforeground = "white", command = clicked)
data = StringVar()

def done():
    var.set((data.get()))

inp = Entry(window, textvariable = data ,width = 30)
but = Button(window, text = "OK!", command = done)

label1 = Label(text = "label1", bg="red")
label2 = Label(text = "label2", bg="blue")
label3 = Label(text = "label3", bg="green")
label4 = Label(text = "label4", bg="yellow")

#Canvas
c = Canvas(window, height = 300, width = 600)
c.create_line(0,0,600,300, fill = "black" , width = 5)
c.create_line(600,0,0,300, fill = "black" , width = 5)
c.create_rectangle(0,0,300,300, fill = "pink")

#checkbuttons
c1 = Checkbutton(window, text = "Working ?", padx= 15, pady= 15, relief = GROOVE, height = 10, width = 20)
c2 = Checkbutton(window, text = "Done ?", padx = 15, pady = 15, relief = GROOVE, height = 10, width = 20)

label1.pack(side = TOP, fill=X)
bt.pack(fill = X)
label2.pack(side = LEFT, fill=Y)
label3.pack(side = RIGHT, fill=Y)
label4.pack(side = BOTTOM, fill=X)
inp.pack(padx = 15, pady = 15)
but.pack()
c.pack(pady =20)
disp.pack(fill =X)
c1.pack(side = LEFT)
c2.pack(side = RIGHT)

#fill allows to take as much space as available and expand allows additional space to the widget
#For geometry management, either use place or grid or pack

window.mainloop()