import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-poster')

def divided_diff(x, y):
    n = len(y)
    coef = np.zeros([n, n])
    # kolom pertama adalah y
    coef[:,0] = y

    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])

    return coef

def newton_poly(coef, x_data, x):
    '''
    Evaluasi polinom newton
    saat x
    '''
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p

# Data yang diberikan
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# mendapatkan koefisien selisih yang terbagi
a_s = divided_diff(x, y)[0, :]

# mengevaluasi titik data baru
x_new = np.arange(5, 40.1, .1)
y_new = newton_poly(a_s, x, x_new)

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo')
plt.title('Polinom Newton')
plt.grid()
plt.xlabel('Tegangan, x (kg/mm2)')
plt.ylabel('Waktu Patah, y (jam)')
plt.plot(x_new, y_new)
