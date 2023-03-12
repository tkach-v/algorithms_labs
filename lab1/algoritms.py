from math import sin, cos, sqrt
from tkinter.messagebox import showerror
import os, sys

# function that helps to add image to exe file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("..")

    return os.path.join(base_path, relative_path)

def task1(a, b):
    y1 = sin(a + b) - (cos(a - b)) ** 2
    return y1


def task2(b, g, i, k, n):
    try:
        if (i % 5) < 3:
            y = (g ** (g + i)) / (n * (b ** (k + i)))
        elif g < 0:
            showerror(title="Помилка", message="Число під коренем має бути більше ніж 0")
            return None
        else:
            y = ((n * (b ** (g + i))) / (g ** (k + i))) ** (1 / 4)
        return y
    except ZeroDivisionError:
        showerror(title="Помилка", message="Ділення на нуль!")
        return None
    except OverflowError:
        showerror(title="Помилка", message="Результат є надто великим!")
        return None


def task3(c, m, p):
    # перевірка, чи всі списки мають однакову довжину n
    if len(c) != len(m) or len(m) != len(p):
        showerror(title="Помилка", message="Довжина списків повинна бути однаковою!")
        return None

    numerator = 0
    denominator = 0
    for i in range(len(c)):
        numerator += m[i] + c[i]
        denominator += p[i] + c[i]
    try:
        result = sqrt(numerator / denominator)
        return result
    except ZeroDivisionError:
        showerror(title="Помилка", message="Ділення на нуль!")
        return None
    except ValueError:
        showerror(title="Помилка", message="Від'ємне число під коренем!")
        return None

