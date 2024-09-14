import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Чтение данных из файла
def read_data(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            x.append(float(values[0]))
            y.append(float(values[1]))
    return np.array(x), np.array(y)

# Построение графика с гладкими кривыми и прямыми МНК
def plot_data_with_fits(file_list, x_min, x_max, y_min, y_max):
    plt.figure()

    # Цвета для прямых и точек
    colors = ['red', 'orange']

    for i, filename in enumerate(file_list):
        x, y = read_data(filename)

        # Построение исходных точек
        plt.scatter(x, y, color=colors[i])

        # Выполнение МНК для нахождения коэффициентов прямой
        A = np.vstack([x, np.ones_like(x)]).T
        m, c = np.linalg.lstsq(A, y, rcond=None)[0]

        # Оценка погрешности
        delta = 0.2 * 10 ** -5

        # Построение линии регрессии
        x_fit = np.linspace(x_min, x_max, 500)
        plt.plot(x_fit, m * x_fit + c, color=colors[i], linestyle='--',
                 label=f'$k = {m:.5f} \pm 0.98 \\times 10^{{-7}}$')

    # Настройка графика
    plt.xlabel('Ток через экспериментальный образец I, мА')
    plt.ylabel('$k \\times 10^{{-5}}$, В/Тл')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # Настройка сетки
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Основная сетка
    plt.minorticks_on()  # Включение мелких делений
    plt.grid(True, which='minor', linestyle=':', linewidth=0.5)  # Мелкая сетка

    plt.legend()
    plt.show()

# Установите минимальные и максимальные значения для осей X и Y
x_min = 20
x_max = 101
y_min = 0
y_max = 8

# Список файлов с данными
file_list = [
    'coeffs_data.txt'
]

# Построение графика
plot_data_with_fits(file_list, x_min, x_max, y_min, y_max)
