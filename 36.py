from tkinter import *
class CounterApp:
    def __init__(self,window):
        self.counter = 0
        self.label = Label(window,text="Conter: 0",font=("Helvetica",20))
        self.label.pack(pady=20)
        self.increment_button = Button(window,text="Increment",fg="green",width=15,font=("Arial",15),command=self.increment)
        self.increment_button.pack(pady=10)
        self.decrement_button = Button(window,text="Decrement",width=15,fg="red",font=("Arial",15),command=self.decrement)
        self.decrement_button.pack(pady=10)
    def increment(self):
        self.counter += 1
        self.update_label()
    def decrement(self):
        self.counter -= 1
        self.update_label()
    def update_label(self):
        self.check()
        self.label.config(text=f"Counter: {self.counter}")
    def check(self):
        if self.counter < 0:
            self.label.config(fg="red")
        elif self.counter > 0:
            self.label.config(fg="green")
        else:
            self.label.config(fg="black")
if __name__ == "__main__":
    window = Tk()
    window.title("Counter App")
    window.geometry("300x300")
    app = CounterApp(window)
    window.mainloop()