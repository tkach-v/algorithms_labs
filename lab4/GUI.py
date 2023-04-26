import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import showerror

import matplotlib
import matplotlib.pyplot as plt
import numpy

matplotlib.use("TkAgg")
import algorithms


class SolveTask(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Метод хорд")

        tk.Label(self, text="Рівняння:").grid(row=0, column=0, sticky='nsw', padx=10, pady=5)
        tk.Label(self, text="2*lg(x) - x/2 + 1 = 0").grid(row=0, column=1, sticky='nse', padx=10, pady=5)

        tk.Label(self, text="Введіть границю a:").grid(row=1, column=0, sticky='nsw', padx=10, pady=5)
        self.a = tk.StringVar()
        tk.Entry(self, textvariable=self.a).grid(row=1, column=1, sticky='nse', padx=10, pady=5)

        tk.Label(self, text="Введіть границю b:").grid(row=2, column=0, sticky='nsw', padx=10, pady=5)
        self.b = tk.StringVar()
        tk.Entry(self, textvariable=self.b).grid(row=2, column=1, sticky='nse', padx=10, pady=5)

        tk.Label(self, text="Введіть потрібну точність:").grid(row=3, column=0, sticky='nsw', padx=10, pady=5)
        self.e = tk.StringVar()
        tk.Entry(self, textvariable=self.e).grid(row=3, column=1, sticky='nse', padx=10, pady=5)

        tk.Button(self, text="Обчислити", bg='white', borderwidth=2, command=self.calculate).grid(row=4, column=0,
                                                                                                  columnspan=2, padx=10,
                                                                                                  pady=5, sticky='nswe')
        tk.Button(self, text="Графік рівняння", bg='white', borderwidth=2, command=self.draw_graph).grid(row=5,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         padx=10,
                                                                                                         pady=5,
                                                                                                         sticky='nswe')

    def calculate(self):
        try:
            results = []
            a = float(self.a.get())
            b = float(self.b.get())
            x = numpy.arange(a, b, 0.1).tolist()

            for i in range(1, len(x)):
                temp = algorithms.chord_method(algorithms.f, x[i - 1], x[i], float(self.e.get()))
                if temp is not None:
                    results.append(temp)

        except ValueError:
            showerror(title="Помилка", message="Границі та точність повинні бути числами!")

        tk.Label(self, text="Результат:").grid(row=6, column=0, sticky='nsw', padx=10, pady=15)
        if not results:
            tk.Label(self, text="Коренів не знайдено").grid(row=6, column=1, sticky='nsew', padx=10, pady=15)
        else:
            tk.Label(self, text=f"{results}").grid(row=6, column=1, sticky='nsew', padx=10, pady=15)

    def draw_graph(self):
        x = numpy.arange(0.01, 13, 0.01).tolist()
        y = []
        y_0 = []
        for i in x:
            y.append(algorithms.f(i))
            y_0.append(0)

        fig, ax = plt.subplots(1, 1)

        ax.plot(x, y, label='f = 2*lg(x) - x/2 + 1')
        ax.plot(x, y_0, label='f = 0')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend(loc="lower right")

        plt.show()


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        default_font = tkFont.Font(root=self, name="TkDefaultFont", exists=True)
        default_font.configure(size=10)

        self.title("Лабораторна робота №4")
        self.geometry("200x130")

        tk.Label(self, text="Виконав: Ткач Володимир\n"
                            "Група: ІО-15\n\n"
                            "Варіант №17 (Метод Хорд)", justify=tk.LEFT).grid(row=0, column=0, padx=15, pady=5,
                                                                              sticky='we')

        tk.Button(self, text="Розв'язати рівняння", bg='white', borderwidth=2, command=SolveTask).grid(row=1, column=0,
                                                                                                       padx=15, pady=5,
                                                                                                       sticky='nswe')


if __name__ == "__main__":
    main = Main()
    main.mainloop()
