def qsort(array, begin, end):

    for i in range(len(array)):

        pivot = array[pivot]
        b = begin + 1
        e = end

        while b < e:
            if array[b] < pivot:
                temp = array[b]
                array[pivot] = temp

            b = b + 1
            e = e - 1


nums = [11, 2, 1, 34, 12]

qsort(nums, 0, len(nums))

print(nums)
