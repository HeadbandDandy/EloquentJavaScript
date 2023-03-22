#  Solution below builds hash map and pairs values with their index
# At each index i, where num = nums[i], we can check our hash map for target - num.
# Adding key-value pairs and checking for target - num are all 0(1), time complexity becomes 0(N) with solution below



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic: # This operation is O(1)!
                return [i, dic[complement]]
            
            dic[num] = i
        
        return [-1, -1]