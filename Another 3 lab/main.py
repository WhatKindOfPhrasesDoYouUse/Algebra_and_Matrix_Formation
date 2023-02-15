import numpy as np
import random
import matplotlib.pyplot as plt
import time

sizeMatrix = 100

def formation(sizeMatrix):
    matrix1 = np.random.uniform(0, 10, size=(sizeMatrix, sizeMatrix))
    matrix2 = np.random.uniform(0, 10, size=(sizeMatrix, sizeMatrix))
    for i in range (0, sizeMatrix):
        for j in range (0, sizeMatrix):
            if i > j:
                matrix1[i,j] = 0
    for i in range (0 ,sizeMatrix):
        for j in range (0 ,sizeMatrix):
            if i < j:
                matrix2[i,j] = 0
    result = np.dot(matrix1,matrix2)
    return result

def timeСosts(sizeMatrix):
    t1 = time.time()
    formation(sizeMatrix)
    t2 = time.time()
    t = t2 - t1
    return t


def check(res):
    print("Проверка тз")
    det = np.linalg.det(res)
    if det != 0:
        print("Матрица неособенная")
    else:
        print("Матрица особенная")
    return

def chart():
    a = []
    g = []
    for i in range (0,sizeMatrix):
       a.append(timeСosts(i))
       g.append(i)
    fig, ax = plt.subplots()
    plt.xlim(0,sizeMatrix)
    plt.plot(g,a,"r")
    plt.legend(["Неособенная матрица"])
    plt.show()
    return

print("Сформированная матрица")
res = formation(sizeMatrix)
print(res)
check(res)
print(timeСosts(sizeMatrix))
chart()





