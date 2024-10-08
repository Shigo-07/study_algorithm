from typing import List

def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            index = index + 1
        if numbers[index] >= numbers[index - 1]:
            index += 1
        else:
            numbers[index],numbers[index - 1] = numbers[index - 1],numbers[index] 
            index -= 1
    return numbers

if __name__ == "__main__":
    nums = [2,1,5,8,7,3]
    print(gnome_sort(nums))