from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
import numpy as np

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Menghitung polinom Lagrange
f = lagrange(x, y)

# Membuat array x baru untuk plotting
x_new = np.linspace(min(x), max(x), 500)

# Membuat plot
fig = plt.figure(figsize = (10,8))
plt.plot(x_new, f(x_new), 'b', label='Polinom Lagrange')
plt.plot(x, y, 'ro', label='Data Asli')
plt.title('Polinom Lagrange')
plt.grid()
plt.xlabel('Tegangan, x (kg/mm2)')
plt.ylabel('Waktu Patah, y (jam)')
plt.legend()
plt.show()
