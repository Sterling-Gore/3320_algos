#include <iostream>
#include <vector>
#include <random>

int partition(std::vector<int> &arr, int low, int high){
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(low,high);
    int pivot = dist(rng);

    //this swaps the random pivot with the last element
    int temp = arr[pivot];
    arr[pivot] = arr[high];
    arr[high] = temp;

    int i = low;
    int j = high - 1;
    while( i <= j)
    {
        if(arr[i] < arr[high])
        {
            if( arr[j] > arr[high])
            {
                //swap values at array i and j
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
            else   
            {
                j--;  //decrement until I find a j that is larger than our selected pivot
            }
        }
        else
        {
            i++;  //incremenet until I ifnd a i that is smaller than out selected pivot
        }
    }

    temp = arr[i];
    arr[i] = arr[high];
    arr[high] = temp;
    return i;
}

void quicksort(std::vector<int> &arr, int low, int high)
{
    if(low < high)
    {
        int pivot = partition(arr, low, high);
        quicksort(arr, low, pivot-1);
        quicksort(arr, pivot+1, high);
    }
}

int main()
{
    
    std::vector<int> arr = {4,1,2,6,8,10,31};
    quicksort(arr,0,arr.size()-1);
    for(int i = 0; i < arr.size(); i++)
    {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
    

    return 0;
}
