import numpy as np


# функция призвана удалять те единицы, которые являются частью острова. Проще говоря, удалять все острова целиком.
# первый аргумент - массив с которым мы работаем, второй и третий - координата в которой мы нашли единицу и вызвали функию
# четвёртый аргумент это флаг, который определяет кто вызвал эту функцию. Если её вызвали из кода, то её вызвали на единицу,
# про которую нужно ещё понять является ли она частью острова или нет.
# А вот если функцию вызвала рекурсивно сама функция, то тут уже очевидно что единица является куском острова
#Возможно, у пайтона есть другие, более подходящие инструменты для подобного, но я их пока что не знаю.
class island_class():

    def delete_island(arr, x, y, IS_ISLAND = False):

        dx = [-1, 0, 1]
        dy = [-1, 0, 1]

        assert arr[x][y] == 1

        if IS_ISLAND:
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
                        arr[x][y] = 0
                        THIS_IS_ISLAND = True
                        delete_island(arr, x1, y1, THIS_IS_ISLAND)




ARR_SIZE = 7 # линейный размер матрицы
NUM_OF_NAPH = 10 # количество нафталина в ячейках

x = np.zeros((ARR_SIZE*ARR_SIZE), dtype=int)
x[0:NUM_OF_NAPH:] = 1
np.random.shuffle(x)
a = np.reshape(x, ( -1, ARR_SIZE))

#print(x, "\n")
print(a)

island_number = 0

for i in range(ARR_SIZE):
    for j in range(ARR_SIZE):
        if a[i][j] == 1:
            delete_island(a, i, j)
            island_number += 1

print(a, island_number, sep = "\n")