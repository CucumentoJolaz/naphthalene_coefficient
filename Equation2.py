import numpy as np
import matplotlib.pyplot as plt

def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)
    plt.grid()
    plt.show()

CELLS_NUM_AROUND = 8

x = np.arange(0,1,-.001)

y = np.zeros(len(x))

for i in range(len(x)):
	y[i] = (1 - (1 - x[i])**CELLS_NUM_AROUND)

plt.plot(x, y)
plt.xlabel(r'Соотношение (моль нафталина)/(моль b-CD)')
plt.ylabel(r'Коэффициент эффективного нафталина, Кef')
plt.grid()
plt.savefig("plot2.png")
plt.show()