from tkinter import*

window=Tk()
window.title("Triangle Area Calculator") 
window.geometry('400x400')

label1 = Label (window, text="Enter the Height:", fg='blue', font=('Arial', 14))
label1.grid(row=0,column=0,padx=5,pady=10)

label2 = Label (window, text="Enter the Breadth:", fg='blue', font=('Arial', 14)) 
label2.grid(row=1,column=0,padx=5,pady=10)

height= IntVar()
breadth= IntVar()

textbox1 = Entry(window, textvariable= height, fg='blue', font=('Arial')) 
textbox1.grid(row=0,column=1)

textbox2= Entry(window, textvariable= breadth, fg='blue', font=('Arial')) 
textbox2.grid(row=1,column=1)

def findArea():
    area= 0.5*height.get()*breadth.get()
    emptylabel.config(text='The area is:'+str(area))

button1= Button(window,command=findArea, text='Calculate Area', fg='blue', font=('Arial', 14)) 
button1.grid(row=2,column=1,sticky=W)

emptylabel= Label(window, fg='green', font=('Arial',14)) 
emptylabel.grid(row=3,column=1,sticky=W,pady=10)

window.mainloop()




