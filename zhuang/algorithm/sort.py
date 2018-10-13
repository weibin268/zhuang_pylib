import time


def qsort(array, begin, end):
    if (end - begin) == 1:
        if array[end] > array[begin]:
            temp = array[begin]
            array[begin] = array[end]
            array[end] = temp

        return 0

    for i in range(begin, end):

        pIndex = begin
        pValue = array[pIndex]
        a = begin + 1
        b = end

        while a <= b:
            if array[a] < pValue:
                temp = array[a]
                array[a] = array[pIndex]
                array[pIndex] = temp
                pIndex = a

            if array[b] < pValue:
                temp = array[b]
                array[b] = array[pIndex]
                array[pIndex] = temp
                pIndex = b

            a = a + 1
            b = b - 1

    time.sleep(0.5)
    print(array)

    if begin < (pIndex - 1):
        qsort(array, begin, pIndex - 1)
    if (pIndex + 1) < end:
        qsort(array, pIndex + 1, end)


import random

nums = []
for i in range(10):
    nums.append(random.randint(0, 100))

print(nums)

qsort(nums, 0, len(nums) - 1)

# print(nums)
