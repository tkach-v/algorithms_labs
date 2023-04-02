def aitken_interpolation(x, y, n, x_int):
    f = [[0] * n for _ in range(n)]

    # заповнення першого стовпця таблиці
    for i in range(n):
        f[i][0] = y[i]


    # побудова таблиці
    for j in range(1, n):
        for i in range(n - j):
            f[i][j] = ((x_int - x[i + j]) * f[i][j - 1] - (x_int - x[i]) * f[i + 1][j - 1]) / (x[i] - x[i + j])

    # результат - значення функції в точці x_int
    for i in range(n-1):
        if (x[i] <= x_int <= x[i + 1]):
            row = i
            break
        else:
            row = 0

    result = f[row][-1]
    delta = []
    res1 = 999
    for i in range(1, n-1):
        if f[row][i] == 0:
            result = f[row][i-1]
            break
        res2 = abs(f[row][i+1] - f[row][i])
        delta.append(res2)
        if(res2 < res1):
            res1 = res2
        else:
            result = f[row][i]
            break

    return result
