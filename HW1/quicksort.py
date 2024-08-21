import random

def quicksort(arr, rand):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        if rand:
            pivot = random.randint(1, n) - 1
        else:
            pivot = 0
        left = []
        right = []
        for i in arr:
            if i != arr[pivot]:
                if i < arr[pivot]:
                    left.append(i)
                else:
                    right.append(i)
        return quicksort(left, rand) + [arr[pivot]] + quicksort(right, rand)
