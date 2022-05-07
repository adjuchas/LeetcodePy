from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        hight = len(nums) - 1
        low = 0
        while hight >= low:
            mid = (hight - low) // 2 + low
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hight = mid - 1
            else:
                low = mid + 1
        return -1