from tkinter import *
from tkinter import ttk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title('Калькулятор')
        self.master.geometry('260x270')
        self.master.resizable(False, False)

        self.expression = ''

        # Frame and Canvas
        self.frame = Frame(self.master, padx=10, pady=10)
        self.frame.pack(expand=True)

        self.canvas = Canvas(self.frame, bg="white", width=240, height=260)
        self.canvas.pack(anchor=CENTER, expand=1)

        self.result = StringVar()
        self.expression_field = Entry(self.canvas, textvariable=self.result, font='Montserrat 15')
        self.canvas.create_window(0, 0, anchor=NW, window=self.expression_field, width=240, height=60)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('1', 0, 60), ('2', 60, 60), ('3', 120, 60), ('+', 180, 60),
            ('4', 0, 110), ('5', 60, 110), ('6', 120, 110), ('-', 180, 110),
            ('7', 0, 160), ('8', 60, 160), ('9', 120, 160), ('*', 180, 160),
            ('.', 0, 210), ('0', 60, 210), ('/', 120, 210), ('=', 180, 210),
            ('clear', 180, 10)
        ]

        for (text, x, y) in buttons:
            if text == '=':
                cmd = self.calculate
            elif text == 'clear':
                cmd = self.clear
            else:
                cmd = lambda x=text: self.append_to_expression(x)

            btn = ttk.Button(self.frame, text=text, command=cmd)
            self.canvas.create_window(x, y, anchor=NW, window=btn, width=60, height=50)

    def append_to_expression(self, value):
        self.expression += str(value)
        self.result.set(self.expression)

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
            self.result.set(self.expression)
        except Exception:
            self.result.set('error')
            self.expression = ''

    def clear(self):
        self.expression = ''
        self.result.set(self.expression)

if __name__ == '__main__':
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()
