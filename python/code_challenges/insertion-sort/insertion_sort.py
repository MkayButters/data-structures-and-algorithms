def insertion_sort(arr):

    if len(arr) == 0:
        return "empty array"

    elif len(arr) == 1:
            return "only one number bud"

    else:
        for i in range(1, len(arr)):

            key = arr[i]

            j = i-1
            while j >=0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
