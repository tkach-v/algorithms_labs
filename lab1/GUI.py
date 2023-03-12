import random
import json
import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import showerror
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk

import algoritms


class Task1(tk.Toplevel):
    def __init__(self):
        image = ImageTk.PhotoImage(Image.open(algoritms.resource_path('lab1/task1.jpg')))
        super().__init__()

        self.title("Лінійний алгоритм")

        test = tk.Label(self, image=image)
        test.image = image
        test.grid(row=0, column=0, columnspan=2)

        self.a = tk.StringVar()
        tk.Label(self, text="Задайте значення a:").grid(row=1, column=0, pady=5)
        tk.Entry(self, textvariable=self.a).grid(row=1, column=1)
        self.b = tk.StringVar()
        tk.Label(self, text="Задайте значення b:").grid(row=2, column=0, pady=5)
        tk.Entry(self, textvariable=self.b).grid(row=2, column=1)

        tk.Button(self, text="Розрахувати за формулою", bg='white', borderwidth=2,
                  command=self.get_values_and_calculate).grid(row=3, column=0, columnspan=2, pady=5, padx=15,
                                                              sticky='we')

    def get_values_and_calculate(self):
        try:
            result = algoritms.task1(float(self.a.get()), float(self.b.get()))
            tk.Label(self, text=f"Y1 = {result}", bg='white', font='Arial 13').grid(row=4, column=0, columnspan=2,
                                                                                    pady=10, sticky='nswe')

        except ValueError:
            showerror(title="Помилка", message="a та b повинні бути числами!")
            tk.Label(self, text=f"Y1 = None", bg='white', font='Arial 13').grid(row=4, column=0, columnspan=2, pady=10,
                                                                                sticky='nswe')


class Task2(tk.Toplevel):
    def __init__(self):
        image = ImageTk.PhotoImage(Image.open(algoritms.resource_path('lab1/task2.jpg')))
        super().__init__()

        self.title("Алгоритм, що розгалужується")

        test = tk.Label(self, image=image)
        test.image = image
        test.grid(row=0, column=0, columnspan=2)

        self.b = tk.StringVar()
        tk.Label(self, text="Задайте значення b:").grid(row=1, column=0, pady=5)
        tk.Entry(self, textvariable=self.b).grid(row=1, column=1)
        self.g = tk.StringVar()
        tk.Label(self, text="Задайте значення g:").grid(row=2, column=0, pady=5)
        tk.Entry(self, textvariable=self.g).grid(row=2, column=1)
        self.i = tk.StringVar()
        tk.Label(self, text="Задайте значення i:").grid(row=3, column=0, pady=5)
        tk.Entry(self, textvariable=self.i).grid(row=3, column=1)
        self.k = tk.StringVar()
        tk.Label(self, text="Задайте значення k:").grid(row=4, column=0, pady=5)
        tk.Entry(self, textvariable=self.k).grid(row=4, column=1)
        self.n = tk.StringVar()
        tk.Label(self, text="Задайте значення n:").grid(row=5, column=0, pady=5)
        tk.Entry(self, textvariable=self.n).grid(row=5, column=1)

        tk.Button(self, text="Розрахувати за формулою", bg='white', borderwidth=2,
                  command=self.get_values_and_calculate).grid(row=6, column=0, columnspan=2, pady=5, padx=15,
                                                              sticky='we')

    def get_values_and_calculate(self):
        try:
            result = algoritms.task2(float(self.b.get()), float(self.g.get()), float(self.i.get()), float(self.k.get()),
                                     float(self.n.get()))
            tk.Label(self, text=f"y = {result}", bg='white', font='Arial 13').grid(row=7, column=0, columnspan=2,
                                                                                   pady=10, sticky='nswe')

        except ValueError:
            showerror(title="Помилка", message="b, g, i, k, n повинні бути числами!")
            tk.Label(self, text=f"Y1 = None", bg='white', font='Arial 13').grid(row=7, column=0, columnspan=2, pady=10,
                                                                                sticky='nswe')


class Task3(tk.Toplevel):
    def __init__(self):
        image = ImageTk.PhotoImage(Image.open(algoritms.resource_path('lab1/task3.jpg')))
        super().__init__()

        self.title("Циклічний алгоритм")

        test = tk.Label(self, image=image)
        test.image = image
        test.grid(row=0, column=0, rowspan=2)

        tk.Button(self, text="Згенерувати масиви випадково", bg='white', command=self.generate_window,
                  borderwidth=2).grid(row=0, column=1, sticky='nswe', pady=5, padx=5)
        tk.Button(self, text="Ввести дані з файлу", bg='white', command=self.file_enter,
                  borderwidth=2).grid(row=1, column=1, sticky='nswe', pady=5, padx=5)

        tk.Label(self, text="\nВведіть або згенеруйте масиви (роздільник між числами - пробіл):"
                 ).grid(row=2, column=0, columnspan=2, sticky='nswe', padx=5, pady=5)

        lbl_frame = tk.LabelFrame(self, text="Масиви вхідних даних:", bg='white')
        lbl_frame.grid(row=3, column=0, columnspan=3, padx=10)
        tk.Label(lbl_frame, text="Масив c:", bg='white').grid(row=0, column=0)
        self.text_c = ScrolledText(lbl_frame, height=5, width=37)
        self.text_c.grid(row=0, column=1)
        tk.Label(lbl_frame, text="Масив m:", bg='white').grid(row=1, column=0)
        self.text_m = ScrolledText(lbl_frame, height=5, width=37)
        self.text_m.grid(row=1, column=1, pady=10)
        tk.Label(lbl_frame, text="Масив p:", bg='white').grid(row=2, column=0)
        self.text_p = ScrolledText(lbl_frame, height=5, width=37)
        self.text_p.grid(row=2, column=1)

        tk.Button(self, text="Очистити", bg='white', command=self.clear_textfields).grid(row=4, column=0, padx=10,
                                                                                         pady=5, sticky='nsew')
        tk.Button(self, text="Зберегти", bg='white', command=self.save_and_calculate).grid(row=4, column=1, padx=10,
                                                                                           pady=5, sticky='nsew')

    @staticmethod
    def parse_textfield(textfield):
        # get list of float numbers from Text
        try:
            result = [float(i) for i in textfield.get('1.0', tk.END).split(" ")]
            return result
        except ValueError:
            showerror(title="Помилка", message="Дозволено вводити лише числа!")

    def file_enter(self):
        # зчитування json файлу та збереження даних з нього
        try:
            filename = askopenfilename()
            with open(filename) as f1:
                data = json.load(f1)

            self.c = data['c']
            self.m = data['m']
            self.p = data['p']
            self.set_textfields()
        except:
            showerror(title="Помилка", message="Помилка! Дозволено використовували лише json файли")



    def clear_textfields(self):
        self.text_c.delete('1.0', tk.END)
        self.text_m.delete('1.0', tk.END)
        self.text_p.delete('1.0', tk.END)

    def set_textfields(self):
        self.text_c.insert(tk.INSERT, self.c)
        self.text_m.insert(tk.INSERT, self.m)
        self.text_p.insert(tk.INSERT, self.p)

    def save_and_calculate(self):
        try:
            self.c = self.parse_textfield(self.text_c)
            self.m = self.parse_textfield(self.text_m)
            self.p = self.parse_textfield(self.text_p)
            result = algoritms.task3(self.c, self.m, self.p)
        except TypeError:
            result = None

        tk.Label(self, text=f"f = {result}", bg='white',
                 font='Arial 13').grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='nswe')

    def generate_random_arrays(self):
        try:
            self.c = [round(random.random() * 100, 1) for i in range(int(self.n.get()))]
            self.m = [round(random.random() * 100, 1) for i in range(int(self.n.get()))]
            self.p = [round(random.random() * 100, 1) for i in range(int(self.n.get()))]
            self.clear_textfields()
            self.set_textfields()
        except ValueError:
            showerror(title="Помилка", message="n повинно бути цілим числом!")
            return None

    def generate_window(self):
        top = tk.Toplevel()
        self.n = tk.StringVar()
        tk.Label(top, text="Задайте значення n (кількість елементів у масивах):").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(top, textvariable=self.n).grid(row=0, column=1, padx=10)
        tk.Button(top, text="Згенерувати", bg='white', borderwidth=2,
                  command=self.generate_random_arrays).grid(row=1, column=0, columnspan=2, padx=10, pady=5,
                                                            sticky='nswe')


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        default_font = tkFont.Font(root=self, name="TkDefaultFont", exists=True)
        default_font.configure(size=10)

        self.title("Лабораторна робота №1")
        self.geometry("290x90")

        tk.Label(self, text="Виконав: Ткач Володимир\n"
                            "Група: ІО-15\n\n"
                            "Варіант №18", justify=tk.LEFT).grid(row=0, column=0, padx=20, pady=10, sticky='we')

        menubar = tk.Menu(self)
        self.config(menu=menubar)
        menu_dropdown = tk.Menu(menubar, tearoff=0)
        menu_dropdown.add_command(label="Лінійний алгоритм", command=Task1)
        menu_dropdown.add_command(label="Алгоритм з розгалуженням", command=Task2)
        menu_dropdown.add_command(label="Циклічний алгоритм", command=Task3)
        menubar.add_cascade(label="Вибрати алгоритм", menu=menu_dropdown)


if __name__ == "__main__":
    main = Main()
    main.mainloop()
