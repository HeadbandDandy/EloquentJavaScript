class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # variable initialized at 1 this time since we are doing multiplication#
        if k <= 1:
            return 0

        ans = left = 0
        curr = 1
# iterate over the input and add at each element window #
# above is done by multiplying element #
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                # if above loop works we need to remove by division
                curr //= nums[left]
                left += 1
            ans += right - left + 1

        return ans