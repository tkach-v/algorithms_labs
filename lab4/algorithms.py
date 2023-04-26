from math import log10
from tkinter.messagebox import showerror


# my function
def f(x):
    return 2 * log10(x) - (x / 2) + 1


def chord_method(func, a, b, tol=1e-6, max_iter=1000):
    try:
        fa, fb = func(a), func(b)

        if fa * fb >= 0:
            raise ValueError("Метод хорд не гарантує збіжності на даному інтервалі")

        for i in range(max_iter):
            c = (a * func(b) - b * func(a)) / (func(b) - func(a))
            fc = func(c)
            if abs(fc) < tol:
                return c
            if fa * fc < 0:
                b, fb = c, fc
            else:
                a, fa = c, fc

    except ValueError:
        return None

    showerror(title="Помилка", message="Досягнута максимальна кількість ітерацій!")
    return None

