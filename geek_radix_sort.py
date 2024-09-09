# https://www.geeksforgeeks.org/problems/radix-sort/1
from typing import List

N = 4
arr = [1, 9, 345, 2]

def countin_sort(numbers:List[int], place:int) -> List[int]:
    counts = [0] * 10
    result = [0] * len(numbers)

    for num in numbers:
        index = int(num /place) % 10
        counts[index] += 1
    
    for i in range(1,10):
        counts[i] += counts[i-1]
    
    i = len(numbers) - 1
    while i >= 0:
        index = int(numbers[i] / place) % 10
        result[counts[index]-1] = numbers[i]
        counts[index] -= 1
        i -= 1
    
    return result

def radix_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    place = 1
    while max_num > place:
        numbers = countin_sort(numbers,place)
        place *= 10
    return numbers

if __name__ == "__main__":
    print(radix_sort(arr))