# Need to set vowels 'aeiouy' as well as initiate variables for sliding window
# algo needs to iterate through array and determine the maximum length of vowels within a given set then print results
# Determine Maximum vowels i.e. ans
# Determine Vowels in current window
# set a String of vowels
# Using sliding window technique to 
# calculate number of vowels in each window and 
#  update the count
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        ans: int = 0
            
        
        currCount: int = 0
            
        
        vowels: str = "aeiouy"
            

        for i, v in enumerate(s):
            if i >= k:
                if s[i-k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                currCount += 1
            ans = max(currCount, ans)
        return ans