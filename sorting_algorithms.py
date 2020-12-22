def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            # if jth val is smaller than min_indexth value
            # change the min_index to j index
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]
        yield arr
    yield arr

def insertion_sort(arr):
    for i in range(len(arr)):
        # THis loop moves backwards!
        # It will start at i, end at 0 and move backwards
        for j in range(i, 0, -1):
            if arr[j] < arr[j -1]:
                # swap
                arr[j], arr[j -1] = arr[j -1], arr[j]
                # For visualization
                yield arr
            else:
                # if the jth el is not smaller than j-1th el
                # then there's no need to continue the j for loop
                break
    yield arr

