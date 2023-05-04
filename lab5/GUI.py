import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import showerror

import matplotlib
import numpy as np

matplotlib.use("TkAgg")
import algorithms


class SolveTask(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Метод верхньої релаксації")

        tk.Label(self, text="Введіть СЛАР:").grid(row=0, column=0, columnspan=10, sticky='ew', padx=10, pady=5)

        self.a_text = [[tk.StringVar() for j in range(3)] for i in range(3)]
        self.b_text = [tk.StringVar() for i in range(3)]

        for i in range(3):
            for j in range(0, 7, 3):
                tk.Entry(self, width=8, textvariable=self.a_text[i][j // 3]).grid(row=i + 1, column=j, padx=2, pady=5)
                tk.Label(self, text=f"x{j // 3 + 1}").grid(row=i + 1, column=j + 1, sticky='ew', pady=5)

            tk.Label(self, text=f"+").grid(row=i + 1, column=2, sticky='nsw', pady=5)
            tk.Label(self, text=f"+").grid(row=i + 1, column=5, sticky='nsw', pady=5)
            tk.Label(self, text=f"=").grid(row=i + 1, column=8, sticky='nsw', pady=5)
            tk.Entry(self, textvariable=self.b_text[i], width=8).grid(row=i + 1, column=9, sticky='nse', padx=5, pady=5)

        tk.Button(self, text="Розв'язати", bg='white', borderwidth=2, command=self.calculate).grid(row=4, column=0,
                                                                                                   columnspan=10,
                                                                                                   padx=5,
                                                                                                   pady=5,
                                                                                                   sticky='nswe')

        self.a_text[0][0].set('11')
        self.a_text[0][1].set('3')
        self.a_text[0][2].set('-1')
        self.a_text[1][0].set('2')
        self.a_text[1][1].set('5')
        self.a_text[1][2].set('-5')
        self.a_text[2][0].set('1')
        self.a_text[2][1].set('1')
        self.a_text[2][2].set('1')
        self.b_text[0].set('15')
        self.b_text[1].set('-11')
        self.b_text[2].set('1')


    def calculate(self):
        try:
            initial_guess = np.zeros(3)
            a = [[0 for j in range(3)] for i in range(3)]
            b = [0 for i in range(3)]
            for i in range(3):
                for j in range(3):
                    a[i][j] = float(self.a_text[i][j].get())
                b[i] = float(self.b_text[i].get())


            result = algorithms.sor_solver(np.array(a), np.array(b), 0.5, initial_guess, 1e-9)


        except ValueError:
            showerror(title="Помилка", message="Всі значення у полях СЛАР повинні бути числами!")
            result = None

        tk.Label(self, text=f"x = {result}").grid(row=5, column=0, columnspan=10, sticky='nsew', padx=10, pady=10)


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        default_font = tkFont.Font(root=self, name="TkDefaultFont", exists=True)
        default_font.configure(size=10)

        self.title("Лабораторна робота №5")
        self.geometry("285x130")

        tk.Label(self, text="Виконав: Ткач Володимир\n"
                            "Група: ІО-15\n\n"
                            "Варіант №17 (Метод верхньої релаксації)", justify=tk.LEFT).grid(row=0, column=0, padx=15,
                                                                                             pady=5,
                                                                                             sticky='we')

        tk.Button(self, text="Розв'язати СЛАР", bg='white', borderwidth=2, command=SolveTask).grid(row=1, column=0,
                                                                                                   padx=15, pady=5,
                                                                                                   sticky='nswe')


if __name__ == "__main__":
    main = Main()
    main.mainloop()
