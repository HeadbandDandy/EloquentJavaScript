class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # identify range
        n = len(nums)
        # i is where we track position of first zero
        i = 0
        # loop to iterate through range of numbers and tracking position of
        # non zero with j
        for j in range(n):
            # if j is not equal to zero it will switch positions
            if (nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                # eventually reaching the end of array
                i += 1