# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# First Attempt
def removeDuplicates(nums: list[int]) -> int:
    k: int = len(nums)
    i: int = 0
    while i < k - 1:
        while nums[i] == nums[i + 1]:
            nums = _leftShiftArrElements(nums, i)
            k -= 1
        i += 1
    return k

def _leftShiftArrElements(arr: list[int], subarr_start: int) -> list[int]:
    for i in range(subarr_start, len(arr) - 1):
        arr[i] = arr[i+1]
    arr[len(arr) - 1] = None
    return arr

# Final Solution (Claude.ai)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1530734734
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        # Position where we'll place the next unique element
        write_pos = 1
        
        # Iterate through array starting from second element
        for i in range(1, len(nums)):
            # If current element is different from previous element
            if nums[i] != nums[i-1]:
                # Place current element at write_pos
                nums[write_pos] = nums[i]
                write_pos += 1
                
        return write_pos

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    #print(removeDuplicates(nums))
    #print(nums)