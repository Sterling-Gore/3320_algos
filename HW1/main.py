
import MergeSort
import random
import timeit
import quicksort




def array_creator(type, n):
    arr = []
    if type == "reverse":
        while n > 0:
            arr.append(n)
            n -= 1
    elif type == "oddeven":
        for i in range(1, n+1, 2):
            arr.append(i)
        for i in range(2, n+1, 2):
            arr.append(i)
    elif type == "random":
        for i in range(1, n+1):
            arr.append(i)
        arr = random.sample(arr, n)
    return arr



def main():
    type = "oddeven"
    size = 32
    arr = array_creator(type, size)
    





    #mergesort
    start_time = timeit.default_timer()   #10:05
    MS_arr = MergeSort.mergesort(arr)
    final_time = timeit.default_timer() - start_time   #10:08 - 10:05  =  3 minutes

    print(f"MergeSort time for {type} array of size {size}: \n {final_time:0.7f}  \n")





    #random quicksort
    start_time = timeit.default_timer()
    QS_Rand_arr = quicksort.quicksort(arr, True)
    final_time = timeit.default_timer() - start_time

    print(f"Random QuickSort time for {type} array of size {size}: \n {final_time:0.7f} \n ")





    #standard quicksort
    start_time = timeit.default_timer()
    QS_arr = quicksort.quicksort(arr, False)
    final_time = timeit.default_timer() - start_time

    print(f"Standard QuickSort time for {type} array of size  {size}: \n {final_time:0.7f} \n ")


if __name__ == "__main__":
    main()