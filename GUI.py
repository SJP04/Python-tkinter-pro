from tkinter import *

def click():
    print("you clicked the button!")
window = Tk()
window.geometry("400x400")
window.title("calculator")
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")
lable = Label(window,text="Type value:",font=('times new roman',10,'bold'),
              relief=RAISED,padx=10,pady=10)
entry = Entry(window,font=('times new roman',10,'bold'),relief=RAISED)
entry.pack(side=RIGHT)
entry.place(x=40,y=40)
#button = Button(window,text="click me!",command=click,padx=2,pady=30)
#button.pack()
lable.place(x=10,y=10)


window.mainloop()