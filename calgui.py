from tkinter import*

def cal(option):
    num1 = float(entry.get())
    num2 = float(entry1.get())
    if(option == "+"):
        res = num1 + num2
    elif(option == "-"):
        res = num1 - num2
    elif(option == "*"):
        res = num1 * num2
    else:
        res = num1 / num2  

    res_o.config(text=str(res))              

window= Tk()

window.geometry("400x400")
window.title("calculator")

icon= PhotoImage(file='logo.png')
window.iconphoto(True,icon)
t1=Label(window,text="Calculator",font=("times new roman",16)).place(x=15,y=10)
label = Label(window,text="Type value 1:",font=("times new roman",10,'bold'))
label.place(x=100,y=50)
entry = Entry(window,font=("times new roman",10))
entry.place(x=200,y=50)

label1 = Label(window,text="Type value 2:",font=("times new roman",10,'bold'))
label1.place(x=100,y=100)
entry1 = Entry(window,font=("times new roman",10))
entry1.place(x=200,y=100) 

frame = Frame(window)
frame.pack(pady=150)

button1 = Button(frame,text="+",command=lambda:cal("+"),bg='green',width='3')
button1.pack(side=LEFT,padx=10)

button2 = Button(frame,text="-",command=lambda:cal("-"),bg='green',width='3')
button2.pack(side=LEFT,padx=10)

button3 = Button(frame,text="x",command=lambda:cal("*"),bg='green',width='3')
button3.pack(side=LEFT,padx=10)

button4 = Button(frame,text="/",command=lambda:cal("/"),bg='green',width='3')
button4.pack(side=LEFT,padx=10)

res_1 = Label(window,text="Result:",font=("times new roman",10,'bold'))
res_1.pack()

res_o = Label(window,bg="white",width=20,font=("times new roman",10,'bold'),relief='sunken')
res_o.pack()

window.mainloop() 