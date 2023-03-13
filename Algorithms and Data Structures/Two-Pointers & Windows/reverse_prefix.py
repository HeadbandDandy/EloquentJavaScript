# below method works by using slice mthod to break string upto a certain character
# after that the string is reversed, then the rest of the string is added

class Solution:
    
    def reversePrefix(self, word: str, ch: str) -> str:
        return word[:word.find(ch) + 1][::-1] + word[word.find(ch) + 1:] 


