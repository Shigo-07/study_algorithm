# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def _search(nums: List[int],target: int, left:int,right :int) -> int:
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return _search(nums,target,mid+1,right)
            else:
                return _search(nums,target,left,mid-1)
    
        return _search(nums,target,0,len(nums)-1)

