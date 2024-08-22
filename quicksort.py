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

'''
def partition(list,low,high):
    pivot = randrange(low,high+1)

    #this swaps the random pivot with the last element
    temp = list[pivot]
    list[pivot] = list[high]
    list[high] = temp

    i = low
    j = high -1
    while i < j:
        if list[i] > list[high]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            j -= 1
        else:
            i += 1
    
    if(list[i] < list[high]):
        temp = list[i+1]
        list[i+1] = list[high]
        list[high] = temp
        return i+1
    else:
        temp = list[i]
        list[i] = list[high]
        list[high] = temp
        return i
'''

def partition(list,low,high):
    pivot = randrange(low,high+1)

    #this swaps the random pivot with the last element
    temp = list[pivot]
    list[pivot] = list[high]
    list[high] = temp

    i = low
    j = high -1
    while i <= j:
        if list[i] < list[high]:
            if list[j] > list[high]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
                j -= 1
                i += 1
            else:
                j -= 1
        else:
            i += 1
    
    
    temp = list[i]
    list[i] = list[high]
    list[high] = temp
    return i


def cppquicksort(list, low, high):
    if low < high:
        pivot = partition(list, low, high)
        cppquicksort(list, low, pivot-1)
        cppquicksort(list, pivot+1, high )


            




def main():
    list = [7,8,3,1,4,2,6,5]
    cppquicksort(list, 0, 7)
    print(list)


main()