import numpy
import json
import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import showerror
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
import algorithms


class Window1(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Сортування вибором з пошуком максимального елемента")

        tk.Label(self, text="Введіть масиви з файлу або згенеруйте випадково:", font="Arial 11 bold",
                 ).grid(row=0, column=0, columnspan=2, sticky='nswe', padx=5, pady=5)

        tk.Button(self, text="Ввести дані з файлу", bg='white', borderwidth=2, command=self.file_enter
                  ).grid(row=1, column=0, sticky='nswe', padx=5)
        tk.Button(self, text="Згенерувати масиви випадково", bg='white', borderwidth=2, command=self.generate_window
                  ).grid(row=1, column=1, sticky='nswe', padx=5)
        tk.Button(self, text="Відсортувати та побудувати графік", bg='white', borderwidth=2, command=self.sort_and_draw
                  ).grid(row=2, column=0, columnspan=2, sticky='nswe', padx=5, pady=5)
        self.data = {}


    def file_enter(self):
        # зчитування json файлу та збереження даних з нього
        try:
            filename = askopenfilename()
            with open(filename) as f1:
                self.data = json.load(f1)
        except:
            showerror(title="Помилка", message="Помилка! Дозволено використовували лише json файли")

    def generate_random_arrays(self):
        try:
            for i in range(1, 11):
                self.data["array"+str(i)] = numpy.random.randint(int(self.low_limit.get()), int(self.top_limit.get()), int(self.n.get())).tolist()
        except ValueError:
            showerror(title="Помилка", message="Межі та кількість елементів повинні бути цілими числами!")
            return None

    def generate_window(self):
        top = tk.Toplevel()
        self.n = tk.StringVar()
        tk.Label(top, text="Задайте кількість елементів:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(top, textvariable=self.n).grid(row=0, column=1, padx=5)
        self.low_limit = tk.StringVar()
        tk.Label(top, text="Задайте нижню межу:").grid(row=1, column=0, padx=5, pady=5, sticky='w')
        tk.Entry(top, textvariable=self.low_limit).grid(row=1, column=1, padx=5)
        self.top_limit = tk.StringVar()
        tk.Label(top, text="Задайте верхню межу:").grid(row=2, column=0, padx=5, pady=5, sticky='w')
        tk.Entry(top, textvariable=self.top_limit).grid(row=2, column=1, padx=5)
        tk.Button(top, text="Згенерувати", bg='white', borderwidth=2, command=self.generate_random_arrays
                  ).grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='nswe')

    def sort_and_draw(self):
        x = []
        y_time = []
        y_theory = []
        try:
            for key in self.data:
                x.append(len(self.data[key]))
                result = algorithms.selection_sort(self.data[key])
                y_time.append(result[0])
                y_theory.append(len(self.data[key])**2)

            fig, ax = plt.subplots(1, 2)
            ax[0].plot(x, y_time, marker="o", label='Часова складність')
            ax[0].set_xlabel("Довжина масиву")
            ax[0].set_ylabel("Час виконання")
            ax[0].legend(loc="lower right")

            ax[1].plot(x, y_theory, color='red', marker="o", label='Обчислювальна складність')
            ax[1].set_xlabel("Довжина масиву")
            ax[1].set_ylabel("Кількість операцій")
            ax[1].legend(loc="lower right")
            plt.show()

        except TypeError:
            showerror(title="Помилка", message="Елементи масивів повинні бути числами!")


class Main(tk.Tk):
    def __init__(self):
        super().__init__()

        default_font = tkFont.Font(root=self, name="TkDefaultFont", exists=True)
        default_font.configure(size=10)

        self.title("Лабораторна робота №2")
        self.geometry("290x90")

        tk.Label(self, text="Виконав: Ткач Володимир\n"
                            "Група: ІО-15\n\n"
                            "Варіант №17", justify=tk.LEFT).grid(row=0, column=0, padx=20, pady=10, sticky='we')

        menubar = tk.Menu(self)
        self.config(menu=menubar)

        menubar.add_command(label="Сортувати масив", command=Window1)


if __name__ == "__main__":
    main = Main()
    main.mainloop()
