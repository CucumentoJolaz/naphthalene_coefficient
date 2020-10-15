import numpy as np


# функция призвана удалять те единицы, которые являются частью острова. Проще говоря, удалять все острова целиком.
# первый аргумент - массив с которым мы работаем, второй и третий - координата в которой мы нашли единицу и вызвали функию

def island_check(arr, x, y):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]

    assert arr[x][y] == 1

    for i in range(len(dx)):
        for j in range(len(dy)):
            if dx[i] == dy[j] == 0:
                continue

            x1 = x + dx[i]
            y1 = y + dy[j]

            if (x1 >= 0 and x1 < len(arr) and y1 >= 0 and y1 < len(arr[0])):
                if arr[x1][y1] == 1:
                    # Мы убедились в том, что имеем дело с островом
                    return True

    return False # Если мы дошли до этой точки функции, то мы не обнаружили ни одной единицы вокруг рассматриваемой


def delete_island(arr, x, y):

    dx = [-1, 0, 1]
    dy = [-1, 0, 1]

    assert arr[x][y] == 1

    arr[x][y] = 0

    for i in range(len(dx)):
        for j in range(len(dy)):
            if dx[i] == dy[j] == 0:
                continue

            x1 = x + dx[i]
            y1 = y + dy[j]

            if (x1 >= 0 and x1 < len(arr) and y1 >= 0 and y1 < len(arr[0])):
                if arr[x1][y1] == 1:
                    # Мы убедились в том, что имеем дело с островом

                    delete_island(arr, x1, y1)



ARR_SIZE = 1000  # линейный размер матрицы
NUM_OF_NAPH = 350000  # количество нафталина в ячейках

x = np.zeros((ARR_SIZE * ARR_SIZE), dtype=int)
x[0:NUM_OF_NAPH:] = 1
np.random.shuffle(x)
a = np.reshape(x, (-1, ARR_SIZE))

# print(x, "\n")

b = np.copy(a)

island_num = 0
for i in range(ARR_SIZE):
    for j in range(ARR_SIZE):
        if a[i][j] == 1:
            if island_check(a, i, j):
                delete_island(a, i, j)
                island_num += 1

unique, counts = np.unique(a, return_counts=True) # подсчитывает количество оставшихся нулей и единиц для дальнейшего использования
arr_dict = dict(zip(unique, counts))

K = (NUM_OF_NAPH - arr_dict[1])/NUM_OF_NAPH # коэффициент показывающий какое количество нафталина находится внутри островков

print(arr_dict, K, sep = "; ")
#print(a, island_num, sep="\n")