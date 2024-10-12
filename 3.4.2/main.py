import numpy as np
import matplotlib.pyplot as plt

filename = 'data.txt'
n = 4

data = np.loadtxt(filename)
x = data[:, 0]
y = data[:, 1]

plt.figure(figsize=(10, 6))

plt.plot(x[:n], y[:n], 'o', color='gray', markersize=5)

plt.plot(x[n:], y[n:], 'o', color='orange', markersize=5)

x_poly = x[:n]
y_poly = y[:n]
coeffs_poly = np.polyfit(x_poly, y_poly, 2)
poly = np.poly1d(coeffs_poly)

x_line = x[n:]
y_line = y[n:]
coeffs_line = np.polyfit(x_line, y_line, 1)
line = np.poly1d(coeffs_line)

x_fit_poly = np.linspace(x_poly.min(), x_poly.max(), 100)
y_fit_poly = poly(x_fit_poly)

x_fit_line = np.linspace(x.min(), x_line.max(), 100)
y_fit_line = line(x_fit_line)

intersection_x = -coeffs_line[1] / coeffs_line[0]
intersection_x = round(intersection_x, 1)

plt.plot(x_fit_poly, y_fit_poly, label='Ферромагнетизм', color='gray', linestyle='--')
plt.plot(x_fit_line, y_fit_line, label='Парамагнетизм', color='orange', linestyle='--')

plt.axhline(0, color='black', lw=0.5)
plt.scatter(intersection_x, 0, color='red')
plt.text(35, 0.1, fr'$\theta_p$ = ({intersection_x}$\pm$0,5)℃', fontsize=30, ha='center')
plt.text(31, 0.03, fr'$\theta_k$ = (20.1$\pm$0,5)℃', fontsize=30, ha='center')

plt.title('1/$\chi$ от T')
plt.xlabel('T, ℃')
plt.ylabel('1/$\chi$')
plt.xlim(10, 45)
plt.ylim(0, 0.365)
plt.grid(which='both')
plt.minorticks_on()
plt.legend()
plt.show()
