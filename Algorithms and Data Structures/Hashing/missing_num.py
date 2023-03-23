# algo needs to loop over a range of numbers
# if loop finds all numbers in a set print nothing
# if loop finds a missing number in a set, we need to print that number

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        # declares a set #
        seen = set(nums)
        # declares the movement through the set #
        n = len(nums) + 1

        # the loop checks if number has been seen...if not will print Number #
        for number in range(n):
            if number not in seen:
                return number