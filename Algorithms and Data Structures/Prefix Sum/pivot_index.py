# need to set a prefix for array
# also need to determine left and right sides
# if left and right sides are equal we need to print an output
# if they are not equal, algo needs to iterate through loop to determine if any sides are equal

class Solution:
    # need to set side and prefix for algo below
    def pivotIndex(self, nums: list[int]) -> int:
        left = 0
        right = sum(nums)

        for i, num in enumerate(nums):
            # attemptin to reduce size of right index to determine pivot index
            right -= num
            #next we compare left and right to determine pivot index
            if left == right:
                # if anything is returned it is required
                return i 
                # then we have to add the number iteratively/incrementally
            left += num
        
        return -1 