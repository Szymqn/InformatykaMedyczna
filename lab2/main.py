import numpy as np


def convolution(array1, array2):
    array1_l, array2_l = len(array1), len(array2)
    temp = np.zeros(array1_l + array2_l - 1)

    for i in range(array1_l):
        for j in range(array2_l):
            temp[i + j] += array1[i] * array2[j]
    return temp


m = [2, 1, 3]
n = [5, 1, 2]

print(convolution(m, n))
