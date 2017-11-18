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

    if begin<(pIndex-1):
        qsort(array, begin, pIndex - 1)
    if (pIndex+1)<end:
        qsort(array, pIndex + 1, end)


nums = [11, 2, 1, 34, 12, 34, 134, 566, 11, 3234, 123, 44, 51]

qsort(nums, 0, len(nums) - 1)

print(nums)
