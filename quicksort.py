from random import randrange


def quicksort(list):
    if len(list) > 1:
        pivot = randrange(len(list))
        left = []
        right = []
        for index, i in enumerate(list):
            if index != pivot:
                if i < list[pivot]:
                    left.append(i)
                else:
                    right.append(i)
        left = quicksort(left)
        right = quicksort(right)
        return left + [list[pivot]] + right
    else:
        return list


def partition(list,low,high):


def cppquicksort(list, low, high):
    if low < high:
        pivot = partition(list, low, high)
        cppquicksort(list, low, pivot-1)
        cppquicksort(list, pivot+1, high )


            




def main():
    list = [7,8,3,1,4,2,6,5]
    print(quicksort(list))


main()