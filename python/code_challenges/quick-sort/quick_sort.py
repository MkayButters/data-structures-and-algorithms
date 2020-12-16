def partition(arr, low, high):

    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):

        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]

    return (i+1)

def quick_sort(arr, low, high):

    if len(arr) == 0:
        return "no bueno, lista es no provechoso"

    elif len(arr) == 1:
        return arr

    else:
        if low < high:

            pi = partition(arr, low, high)
            #Separately sort elements before partition and after partition
            quick_sort(arr, low, pi-1)
            quick_sort(arr, pi+1, high)
