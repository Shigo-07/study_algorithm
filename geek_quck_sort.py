# https://www.geeksforgeeks.org/problems/quick-sort/1
from typing import List
N = 5 
arr= [ 4, 1, 3, 9, 7]

def partition(numbers:List[int],low,high) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low,high):
        if numbers[j] < pivot:
            i += 1
            numbers[j],numbers[i] = numbers[i],numbers[j]
    numbers[i+1],numbers[high] = numbers[high],numbers[i+1]
    return i + 1

def quick_sort(numbers:List[int]) -> List[int]:

    def _quick_sort(numbers:List[int],low,high) -> None:
        if low < high:
            partition_index = partition(numbers,low,high)
            _quick_sort(numbers,low,partition_index-1)
            _quick_sort(numbers,partition_index+1,high)

    _quick_sort(numbers,0,len(numbers)-1)
    return numbers

if __name__ == "__main__":
    print(quick_sort(arr))