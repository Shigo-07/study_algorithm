from typing import List

def shell_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers // 2
    while gap > 0:
        for i in range(gap,len_numbers):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j-gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
    
    return numbers

if __name__ == "__main__":
    nums = [5,6,9,2,3]
    print(shell_sort(nums))
