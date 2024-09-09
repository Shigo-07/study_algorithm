# https://www.geeksforgeeks.org/problems/merge-sort/1
from typing import List
N = 5
arr = [4,1,3,9,7]

def merge_sort(numbers:List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    
    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    left_idx = right_idx = merge_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            numbers[merge_idx] = left[left_idx]
            left_idx += 1
        else:
            numbers[merge_idx] = right[right_idx]
            right_idx += 1
        merge_idx += 1
    
    while left_idx < len(left):
        numbers[merge_idx] = left[left_idx]
        left_idx += 1
        merge_idx += 1

    while right_idx < len(right):
        numbers[merge_idx] = right[right_idx]
        right_idx += 1
        merge_idx += 1

    return numbers

print(merge_sort(arr))