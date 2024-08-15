import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.create_widgets()

    def create_widgets(self):
        # نمایشگر ماشین حساب
        self.display = tk.Entry(self.root, font=("Arial", 24), borderwidth=1, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # دکمه‌ها و جایگذاری آن‌ها در Grid
        buttons = [
            ('AC', 1, 0), ('()', 1, 1), ('%', 1, 2), ('÷', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('⌫', 5, 2), ('=', 5, 3)
        ]

        for (text, row, column) in buttons:
            self.create_button(text, row, column)

        # تنظیم نسبت‌های ردیف‌ها و ستون‌ها برای تنظیم بهتر فضای پنجره
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=2)
        for j in range(4):
            self.root.grid_columnconfigure(j, weight=1)

    def create_button(self, text, row, column):
        button = tk.Button(self.root, text=text, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=column, sticky="nsew")

    def on_button_click(self, char):
        # پردازش ورودی‌های کاربر
        if char == 'AC':
            self.display.delete(0, tk.END)
        elif char == '⌫':
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current_text[:-1])
        elif char == '=':
            try:
                expression = self.display.get().replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)


# ایجاد پنجره اصلی
root = tk.Tk()

# ایجاد ماشین حساب
calculator = Calculator(root)

root.mainloop()