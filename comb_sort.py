from typing import List

def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True
    
    while gap != 1 or swapped == True:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        
        swapped = False

        for i in range(0,len_numbers - gap):
            if numbers[i] > numbers[i+gap]:
                numbers[i],numbers[i+gap] = numbers[i+gap],numbers[i]
                swapped = True
    
    return numbers

if __name__ == "__main__":
    nums = [2,9,1,8,7,3,5]
    print(comb_sort(nums))