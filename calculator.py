from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Калькулятор')
window.geometry('240x260')

frame = Frame(
    window,
    padx=10,
    pady=10
)

frame.pack(expand=True)

canvas = Canvas(bg="white", width=300, height=260)
canvas.pack(anchor=CENTER, expand=1)

result = StringVar()
expression_field = Entry(textvariable=result, font='Montserrat 15')
canvas.create_window(0, 0, anchor=NW, window=expression_field, width=480, height=60)

expression = ''


class Button:
    def __init__(self, num, k, t, command):
        dict_command = {'press_num': self.press_num, 'answer': self.answer, 'clear': self.clear}
        self.btn = ttk.Button(text=num, command=dict_command[command])
        canvas.create_window(k, t, anchor=NW, window=self.btn, width=60, height=50)

    def press_num(self):
        global expression
        expression += self.btn['text']
        result.set(expression)

    @staticmethod
    def answer():
        try:
            global expression
            expression = str(eval(expression))
            result.set(str(expression))
        except:
            result.set('error')
            expression = ''

    @staticmethod
    def clear():
        global expression
        expression = ''
        result.set(expression)


button_num = [Button('1', 0, 60, 'press_num'), Button('2', 60, 60, 'press_num'), Button('3', 120, 60, 'press_num'),
              Button('+', 180, 60, 'press_num'),Button('4', 0, 110, 'press_num'), Button('5', 60, 110, 'press_num'),
              Button('6', 120, 110, 'press_num'),Button('-', 180, 110, 'press_num'), Button('7', 0, 160, 'press_num'),
              Button('8', 60, 160, 'press_num'), Button('9', 120, 160, 'press_num'), Button('*', 180, 160, 'press_num'),
              Button('.', 0, 210, 'press_num'), Button('0', 60, 210, 'press_num'), Button('/', 120, 210, 'press_num'),
              Button('=', 180, 210, 'answer'), Button('clear', 180, 10, 'clear')]

window.mainloop()
