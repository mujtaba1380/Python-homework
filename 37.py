from tkinter import *
class ToDoApp:
    def __init__(self,window):
        self.entry = Entry(window)
        self.entry.pack()
        self.list = Listbox(window,width=30)
        self.list.pack()
        self.add_button = Button(window,text="ADD_TASK",width=12,command=self.add_task)
        self.add_button.pack()
        self.remove_button = Button(window,text="REMOVE_TASK",width=12,command=self.remove_task)
        self.remove_button.pack()
    def add_task(self):
        if not self.entry.get() == "":
            self.list.insert(END,self.entry.get())
    def remove_task(self):
        self.list.delete(END)
if __name__ == "__main__":
    window = Tk()
    window.title("ToDoApp")
    app = ToDoApp(window)
    window.mainloop()