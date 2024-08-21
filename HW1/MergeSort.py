
def merge(array1, array2):
    i, j = 0, 0
    size1, size2 = len(array1), len(array2)
    temp = []
    while i < size1 and j < size2:
        if array1[i] < array2[j]:
            temp.append(array1[i])
            i += 1
        else:
            temp.append(array2[j])
            j += 1

    if i == size1:
        while j < size2:
            temp.append(array2[j])
            j += 1
    else:
        while i < size1:
            temp.append(array1[i])
            i += 1
    return temp
    

#auxilory mergesort
def mergesort(arr):
    size = len(arr)
    if size <= 1:
        return arr
    else:
        left = mergesort(arr[0:int(size/2)])
        right = mergesort(arr[int(size/2):size])
        return merge(left, right)


