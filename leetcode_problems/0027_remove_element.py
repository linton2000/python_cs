# https://leetcode.com/problems/remove-element/
from typing import List

# Final Solution (after hints)
# https://leetcode.com/problems/remove-element/submissions/1530777604
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = 0
        i: int = 0

        while i < len(nums):
            if nums[i] == val:
                nums[i] = None
            else:
                nums[k] = nums[i]
                k += 1
            i += 1
        return k