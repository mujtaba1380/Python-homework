from tkinter import *
win = Tk()
win.geometry("680x400")
win.title("Application For Programming Home Works")
win.resizable(width=False,height=False)
fram1 = Frame(win,bg="lightblue")
fram1.pack(expand=True,fill=BOTH)
scroll = Scrollbar(fram1)
scroll.pack(side=RIGHT,fill=Y)
def text_scroll(*args):
    my_text.yview(*args)

def first_work():
    my_text.delete(1.0,END)
    with open("C:\\Users\\Mujtaba\\Desktop\\programming homework\\built-in function.txt","r") as f:
        data = f.read()
        my_text.insert(INSERT,data)
        f.close()
def second_work():
    my_text.delete(1.0,END)
    with open("C:\\Users\\Mujtaba\\Desktop\\programming homework\\factorial and fibonanci.txt","r") as f:
        data = f.read()
        my_text.insert(INSERT,data)
        f.close()
def third_work():
    my_text.delete(1.0,END)
    with open("C:\\Users\\Mujtaba\\Desktop\\programming homework\\honai.txt","r") as f:
        data = f.read()
        my_text.insert(INSERT,data)
        f.close()
my_text = Text(win,width=70,height=25,yscrollcommand=scroll.set)
my_text.place(x=100)
Label(fram1,text="HOMEWORKS",bg="lightblue").place(x=5,y=20)
first = Button(fram1,text="Built-in function",width=12,command=first_work)
first.place(y=40)
second = Button(fram1,text="factorial",width=12,command=second_work)
second.place(y=70)
third = Button(fram1,text="Hanoi tower",width=12,command=third_work)
third.place(y=100)

scroll.config(command=text_scroll)
# scale = Scale(win,showvalue=False)
# scale.pack(side=RIGHT,fill=BOTH)
# scale.config(command=my_text.yview)
win.mainloop()


