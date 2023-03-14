# first thing to do is initiate sliding window within array
# if numbers within window have a sum equal or greater than the target 
# we need to print result

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        left = 0
        curr = 0

        for i, num in enumerate(nums):
            curr += num
            while curr >= target:
                min_len = min(min_len, i - left + 1)
                curr -= nums[left]
                left += 1
        
        return min_len if min_len != float('inf') else 0