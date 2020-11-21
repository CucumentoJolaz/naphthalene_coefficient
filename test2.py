import numpy as np


ARR_SIZE = 4  # линейный размер матрицы
NUM_OF_NAPH = 35  # количество нафталина в ячейках

arr_1d = np.zeros((ARR_SIZE * ARR_SIZE * ARR_SIZE), dtype=int)
for i in range(ARR_SIZE**3):
    arr_1d[i] = i

arr_1d[0:NUM_OF_NAPH:] = 1
np.random.shuffle(arr_1d)
arr_3d = arr_1d.reshape((ARR_SIZE,ARR_SIZE,ARR_SIZE)).transpose()

print(arr_3d)