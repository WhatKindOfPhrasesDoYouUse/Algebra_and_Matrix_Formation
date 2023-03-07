import math
import time
import numpy as np
import matplotlib.pyplot as plt

# рандомное формирование 2 матриц
def randomFilling(size):
    matrix1 = np.random.randint(1, 9, size = (size, size))
    matrix2 = np.random.randint(1, 9, size = (size, size))
    return [matrix1, matrix2]

matrix1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [4, 3, 2, 1],[4, 3, 2, 1]], int)
matrix2 = np.array([[6, 5, 3, 1], [5, 3, 2, 1], [4, 2, 2, 1],[9, 8, 7, 5]], int)

# алгоритм формирования неособенной матрицы, с передачей размерности в функцию
def formation1(size):
    matrix1 = np.random.uniform(0, 10, size = (size, size))
    matrix2 = np.random.uniform(0, 10, size = (size, size))
    for i in range(0, size):
        for j in range(0, size):
            if i > j:
                matrix1[i,j] = 0
    for i in range(0, size):
        for j in range(0, size):
            if i < j:
                matrix2[i,j] = 0
    return [np.dot(matrix1,matrix2), size]

# алгоритм формирования неособенной матрицы, с передачей матрицы в функцию
def formation2(matrix1, matrix2):
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1)):
            if i > j:
                matrix1[i,j] = 0
    for i in range(0, len(matrix2)):
        for j in range(0, len(matrix2)):
            if i < j:
                matrix2[i,j] = 0
    result = np.dot(matrix1, matrix2)
    return [result, len(result)]

matr1, matr2 = randomFilling(100)

a = formation1(10)[0]
print(a)



# временные затраты для formation1
def t1(size):
    t1 = time.time()
    formation1(size)
    t2 = time.time()
    return t2 - t1

# временные затраты для formation2
def t2(matrix1,matrix2):
    t1 = time.time()
    formation2(matrix1, matrix2)
    t2 = time.time()
    return t2 - t1

# проверка определителя
def determinant(res):
    print("Проверка определителя: ")
    det = np.linalg.det(res)
    if det != 0:
        print("Матрица неособенная")
    else:
        print("Матрица особенная")
    return

def chart1():
    a = []
    g = []
    for i in range (10,300):
       a.append(t1(i))
       g.append(i)
    fig, ax = plt.subplots()
    plt.xlim(10,300)
    plt.plot(g,a,"r")
    plt.legend(["Неособенная матрица"])
    plt.show()

#chart1()



