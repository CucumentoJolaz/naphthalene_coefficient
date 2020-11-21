import numpy as np
import sys

sys.setrecursionlimit(1500)

ARR_SIZE = 100  # линейный размер матрицы
NUM_OF_NAPH = 200000  # количество нафталина в ячейках
MAX_ITER_NUM = 1400
iter_num = 0


# функция призвана удалять те единицы, которые являются частью острова. Проще говоря, удалять все острова целиком.
# первый аргумент - массив с которым мы работаем, второй и третий - координата в которой мы нашли единицу и вызвали функию

def island_check(arr, x, y, z):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    dz = [-1, 0, 1]
    assert arr[x][y][z] == 1

    for i in range(len(dx)):
        for j in range(len(dy)):
            for k in range(len(dz)):
                if dx[i] == dy[j] == dz[k] == 0:
                    continue

                x1 = x + dx[i]
                y1 = y + dy[j]
                z1 = z + dz[k]

                if (x1 >= 0 and x1 < len(arr) and y1 >= 0 and y1 < len(arr[0]) and z1 >= 0 and z1 < len(arr[0][0])):
                    if arr[x1][y1][z1] == 1:
                        # Мы убедились в том, что имеем дело с островом
                        return True

    return False  # Если мы дошли до этой точки функции, то мы не обнаружили ни одной единицы вокруг рассматриваемой


def delete_island(arr, x, y, z):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    dz = [-1, 0, 1]
    assert arr[x][y][z] == 1

    global iter_num #данная конструкция предназначена для подсёта того, какое количества раз в рекурсии вызывается данная функция. Для предотвращения переполнения стека
    iter_num += 1
    if iter_num > MAX_ITER_NUM:
        return 0

    arr[x][y][z] = 0

    for i in range(len(dx)):
        for j in range(len(dy)):
            for k in range(len(dz)):
                if dx[i] == dy[j] == dz[k] == 0:
                    continue

                x1 = x + dx[i]
                y1 = y + dy[j]
                z1 = z + dz[k]

                if (x1 >= 0 and x1 < len(arr) and y1 >= 0 and y1 < len(arr[0]) and z1 >= 0 and z1 < len(arr[0][0])):
                    if arr[x1][y1][z1] == 1:
                        # Мы убедились в том, что имеем дело с островом
                        # arr[x1][y1][z1] = 2
                        delete_island(arr, x1, y1, z1)

arr_1d = np.zeros((ARR_SIZE * ARR_SIZE * ARR_SIZE), dtype=int)
arr_1d[0:NUM_OF_NAPH:] = 1

np.random.shuffle(arr_1d)

arr_3d = arr_1d.reshape((ARR_SIZE, ARR_SIZE, ARR_SIZE)).transpose()

# del arr_1d


arr_3d_copy = np.copy(arr_3d)

island_num = 0
for i in range(ARR_SIZE):
    for j in range(ARR_SIZE):
        for k in range(ARR_SIZE):
            if arr_3d[i][j][k] == 1:
                if island_check(arr_3d, i, j, k):
                    delete_island(arr_3d, i, j, k)
                    island_num += 1
                    iter_num = 0

unique, counts = np.unique(arr_3d,
                           return_counts=True)  # подсчитывает количество оставшихся нулей и единиц для дальнейшего использования
arr_dict = dict(zip(unique, counts))

K = (NUM_OF_NAPH - arr_dict[
    1]) / NUM_OF_NAPH  # коэффициент показывающий какое количество нафталина находится внутри островков

print("Naphthalene concentration - mole(naph)/mole(b-CD) = ", round(NUM_OF_NAPH / ARR_SIZE ** 3, 4))
print("Total quantity of naphthalene = ", NUM_OF_NAPH)
print("Total quantity of single naphthalene = ", arr_dict[1])
print("Island quantity = {}".format(island_num), "K = {}".format(round(K, 4)), sep="; ")
