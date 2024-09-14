import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

def read_data(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            x.append(float(values[0]))
            y.append(float(values[1]))
    return np.array(x), np.array(y)

def plot_data_with_fits(file_list, x_min, x_max, y_min, y_max):
    plt.figure()

    colors = ['red', 'orange']

    for i, filename in enumerate(file_list):
        x, y = read_data(filename)

        plt.scatter(x, y / 2, color=colors[i])
        A = np.vstack([x, np.ones_like(x)]).T
        m, c = np.linalg.lstsq(A, y / 2, rcond=None)[0]
        delta = 0.2 * 10 ** -5
        x_fit = np.linspace(x_min, x_max, 500)
        plt.plot(x_fit, m * x_fit + c, color=colors[i], linestyle='--',
                 label=f'$k = {m:.5f} \pm 0.2 \\times 10^{{-5}}$ В/Тл')

    plt.xlabel('Величина магнитного поля, мТл')
    plt.ylabel('Напряжение Холла, мВ')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.grid(True, which='minor', linestyle=':', linewidth=0.5)

    plt.legend()
    plt.show()

x_min = 250
x_max = 1000
y_min = 0
y_max = 0.075

file_list = [
    'data28_1.txt',
    'data28_2.txt'
]

plot_data_with_fits(file_list, x_min, x_max, y_min, y_max)
