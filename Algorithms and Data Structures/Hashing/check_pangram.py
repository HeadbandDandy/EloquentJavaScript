 # add every letter of sentence to hash set 'seen'
 # if the size of 'seen' is 26, then 'sentence' is a pangram

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

       
        seen = set(sentence)

       
        return len(seen) == 26
