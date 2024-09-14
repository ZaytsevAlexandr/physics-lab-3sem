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

def plot_data_with_smooth_curve(x, y, x_min, x_max, y_min, y_max):
    plt.figure()

    plt.scatter(x, y, color='red', label='Data points')

    x_smooth = np.linspace(x.min(), x.max(), 500)
    spline = make_interp_spline(x, y, k=3)  # Кубический сплайн
    y_smooth = spline(x_smooth)

    plt.plot(x_smooth, y_smooth, 'r-', label='Smooth curve')

    plt.xlabel('I, A')
    plt.ylabel('B, мТл')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.minorticks_on()
    plt.grid(True, which='minor', linestyle=':', linewidth=0.5)
    plt.show()
x_min = 0
x_max = 1.2
y_min = 0
y_max = 1100
x, y = read_data('data_0.txt')
plot_data_with_smooth_curve(x, y, x_min, x_max, y_min, y_max)
