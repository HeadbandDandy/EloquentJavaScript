class Solution:
    # prefix creates an array with the first value
    # for loop is to iterate over the rest of the array...will accumulate
    def waysToSplitArray(self, nums: list[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

# set answer to zero and loop over possible splits...can not split at last index
# left section has a sum equal to the prefix of that index
# right section has sum of all elements minus prefix at current index
# if left is greater than right we can increment and return ans at the end
        ans = 0
        for i in range(len(nums) - 1):
            left_section = prefix[i]
            right_section = prefix[-1] - prefix[i]
            if left_section >= right_section:
                ans += 1

        return ans
    
    
# Second implementation below
# this implementation improves the space complexity of the algorithm above

class Solution:
    def secondWayToSplitArray(self, nums: list[int]) -> int:
        ans = left_section = 0
        total = sum(nums)

        for i in range(len(nums) - 1):
            left_section += nums[i]
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return ans