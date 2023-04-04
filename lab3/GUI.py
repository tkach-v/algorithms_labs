import numpy
import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import showerror
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import algorithms


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        default_font = tkFont.Font(root=self, name="TkDefaultFont", exists=True)
        default_font.configure(size=10)

        self.title("Лабораторна робота №2")
        self.geometry("210x165")

        tk.Label(self, text="Виконав: Ткач Володимир\n"
                            "Група: ІО-15\n\n"
                            "Варіант №17 (Схема Ейткена)", justify=tk.LEFT).grid(row=0, column=0, padx=15, pady=5, sticky='we')

        tk.Button(self, text="Інтерполювати функцію", bg='white', borderwidth=2, command=self.draw).grid(row=1, column=0, padx=15, pady=5, sticky='nswe')
        tk.Button(self, text="Оцінка похибки", bg='white', borderwidth=2, command=self.error_graph).grid(row=2, column=0, padx=15, pady=5, sticky='nswe')

    def draw(self):
        start = 0
        stop = 1.05
        x_theory = numpy.arange(start, stop, 0.05).tolist()
        y_theory = numpy.cos(x_theory).tolist()
        for i in range(len(y_theory)):
            y_theory[i] = y_theory[i]**2

        # Вхідні масиви
        x_interp_entry = [0, 0.25, 0.75, 1]
        y_interp_entry = numpy.cos(x_interp_entry).tolist()
        for i in range(len(y_interp_entry)):
            y_interp_entry[i] = y_interp_entry[i] ** 2

        y_interp = []
        for i in range(len(x_theory)):
            y_interp.append(algorithms.aitken_interpolation(x_interp_entry, y_interp_entry, len(x_interp_entry), x_theory[i]))

        x_interp_nodes = numpy.arange(start, 1.1, 0.1).tolist()
        y_interp_nodes = []
        for i in range(len(x_interp_nodes)):
            y_interp_nodes.append(algorithms.aitken_interpolation(x_interp_entry, y_interp_entry, len(x_interp_entry), x_interp_nodes[i]))



        fig, ax = plt.subplots(1, 2)

        ax[0].plot(x_theory, y_interp, label='Interpolation')
        ax[0].plot(x_interp_nodes, y_interp_nodes, "o")
        ax[0].set_xlabel("X")
        ax[0].set_ylabel("Y")
        ax[0].legend(loc="lower left")
        ax[1].plot(x_theory, y_theory, color="red", label='Y = (cos(x))^2')
        ax[1].set_xlabel("X")
        ax[1].set_ylabel("Y")
        ax[1].legend(loc="lower right")

        plt.show()

    def error_graph(self):
        x_range = [1, 0.5, 0.25, 0.15, 0.05]
        x_graph = []
        res = []
        for i in x_range:
            x = list(numpy.arange(0, 1.05, i))
            x_graph.append(len(x))
            y = numpy.cos(x).tolist()

            for i in range(len(y)):
                y[i] = y[i] ** 2

            res.append(algorithms.aitken_interpolation(x, y, len(x), 0.5))

        error = [numpy.absolute(numpy.cos(0.5) * numpy.cos(0.5) - i) for i in res]

        plt.plot(x_graph, error)
        plt.xlabel("Кількість елементів у вхідних масивах")
        plt.ylabel("Значення помилки")
        plt.show()


if __name__ == "__main__":
    main = Main()
    main.mainloop()
